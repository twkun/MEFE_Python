# -*- coding: utf-8 -*-
from pyaudio import PyAudio, paInt16 
import numpy as np 
from datetime import datetime 
import wave 
import thread

class Wave():
    def __init__(self):
        self.NUM_SAMPLES = 512*4      # pyAudio�ڲ�����Ŀ�Ĵ�С
        self.SAMPLING_RATE = 8000    # ȡ��Ƶ��
        self.LEVEL = 800            # �����������ֵ
        self.COUNT_NUM = 10          # NUM_SAMPLES��ȡ��֮�ڳ���COUNT_NUM������LEVEL��ȡ�����¼����
        self.START = False           #�Ƿ�ʼ¼��
        self.save_buffer = [] 
        self.pa = PyAudio() 
        self.po = PyAudio() 
        self.sm = self.pa.open(format = 8,channels = 1,rate = 8000,output = True)
    # ��data�е����ݱ��浽��Ϊfilename��WAV�ļ���
    def Save(self,filename): 
        wf = wave.open(filename, 'wb')
        wf.setnchannels(1) 
        wf.setsampwidth(2) 
        wf.setframerate(self.SAMPLING_RATE) 
        wf.writeframes("".join(self.save_buffer)) 
        wf.close() 
    def Clear(self):
        self.save_buffer = [] 
    def Record(self):
        self.Clear()
        # ������������
        self.START = True
        self.stream = self.pa.open(format=paInt16, channels=1, rate=self.SAMPLING_RATE, input=True, 
                    frames_per_buffer=self.NUM_SAMPLES) 
        print(paInt16)
        thread.start_new_thread(self.__start,())
    def Say(self,data):
        if type(data) == str:
            self.sm.write(data)
        elif type(data) == np.ndarray:
            self.sm.write(data.tostring())
        elif type(data) == list:
            self.sm.write(np.array(data).tostring())
        else:
            pass
    def GetData(self):
        dt = "".join(self.save_buffer)
        dt = np.fromstring(dt,dtype=np.short)
        return dt
    def Stop(self):
        self.START=False
    def __start(self):
        save_count = 0 
        while True: 
            # ����NUM_SAMPLES��ȡ��
            string_audio_data = self.stream.read(self.NUM_SAMPLES) 
            # �����������ת��Ϊ����
            audio_data = np.fromstring(string_audio_data, dtype=np.short) 
            # �������LEVEL��ȡ���ĸ���
            large_sample_count = np.sum( audio_data > self.LEVEL ) 
            #print np.max(audio_data) 
            # �����������COUNT_NUM�������ٱ���SAVE_LENGTH����
            if large_sample_count > self.COUNT_NUM: 
                save_count = 2 
            else: 
                save_count -= 1 

            if save_count < 0: 
                save_count = 0 
            if save_count > 0: 
                # ��Ҫ��������ݴ�ŵ�save_buffer��
                self.save_buffer.append(string_audio_data) 
                #print(len(self.save_buffer))
            if self.START == False:
                break
        self.stream.stop_stream()
        self.stream.close()
    def __del__(self): 
        self.sm.close()
        self.pa.terminate()

