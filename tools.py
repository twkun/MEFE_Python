# -*- coding: utf-8 -*-
import wave
import pylab as pl
import numpy as np
import scipy.signal as sig

def data_weight(dt):
    temp = [dt[x] for x in xrange(len(dt))]
    temp = [0]+temp[:len(temp)-1]
    return dt-temp
def data_w_hamm(dt,frame=256):
    temp = []
    _t = sig.hamming(frame)
    fx = frame*0.5
    #temp = [sum(np.array(dt[x*fx:x*fx+frame]*_t)**2) for x in range(int(len(dt)/fx -1))]
    temp = [np.log(sum(np.abs(dt[x*fx:x*fx+frame]*_t))) for x in range(int(len(dt)/fx -1))]
    return temp
def data_w_hann(dt,frame=256):
    temp = []
    _t = sig.hann(frame)
    fx = frame*0.5
    #temp = [sum(np.array(dt[x*fx:x*fx+frame]*_t)**2) for x in range(int(len(dt)/fx -1))]
    temp = [np.log(sum(np.abs(dt[x*fx:x*fx+frame]*_t))) for x in range(int(len(dt)/fx -1))]
    return temp
def data_ave(dt):
    return np.average(np.abs(dt))
#得到不为零的连续帧个数和起始地址
def data_up_count(dt,index):
    start = -1
    sum = 0
    for x in range(index,len(dt)):
        if dt[x] > 0:
            if start == -1:
                start = x
        if start != -1:
            if dt[x] > 0:
                sum += 1
            else:
                break
    return start,sum
def sgn(x,y):
    if x * int(y) <0:
        return 1
    else:
        return 0
def data_w_zero(dt,frame=256):
    fx = frame*0.5
    ds = [dt[x*fx:x*fx+frame] for x in range(int(len(dt)/fx -1))]
    de = []
    for x in range(len(ds)):
        su= 1
        for s in range(1,len(ds[x])):
            su = su+ sgn(ds[x][s],ds[x][s-1])
        de.append(su)
    
    #temp = [sum(np.array(dt[x*fx:x*fx+frame]*_t)**2) for x in range(int(len(dt)/fx -1))]
    return de
def show(dts):
    for x in range(1,len(dts)+1):
        print("%d,%d,%d" % (len(dts),1,x))
        pl.subplot(len(dts),1,x)
        pl.plot(dts[x-1])
    pl.show()
def data_en(dw):
    ave = np.average(dw)
    dw_l = np.average([x for x in dw if x < ave])
    ave = dw_l*1.0287
    d_low = lambda x : x > ave and x or 0
    dw_l = [d_low(x) for x in dw]
    return dw_l
def data_point(dt,de):
    sss = 0
    dw_s,dw_c = 0,0
    point = []
    while dw_s != -1:
        sss = dw_s+dw_c
        dw_s,dw_c = data_up_count(de,sss)
        if dw_c > 8:
            point.append([dw_s*128,(dw_s+dw_c)*128])
    dsound = [dt[x[0]:x[1]] for x in point]
    print(point)
    return dsound
