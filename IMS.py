# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 10:32:59 2020

@author: Allan
"""

import numpy as np
import matplotlib.pyplot as plt

#%%
#No optimization parameter (i.e) m is constant
m=5
#y_filt=y_filt[1000:5000]
#split signal into segments
nseg=np.int16(np.floor(len(y_filt)/m))#np. of segments
seg=0 #segment counter
z=0  #Line counter
segLine=0 #Line controller
linez=np.zeros([nseg,2],dtype=np.int16) # Line segment interval
linez[0,:]=[1,m]
#Find slope of line
ab=np.zeros([nseg,1])
def slope(y_filt,interval):
    start=linez[0,0]
    stop=linez[0,1]
    #out=np.sum(np.diff(y_filt[start:stop]))/(stop-start)
    out=np.median(np.gradient(y_filt[start:stop]))
    return out

ab[0]=slope(y_filt,linez[0,:])
#Classify line segment according to slope
linezSeg=np.zeros([nseg,1],dtype=np.int8)
linezSeg[0]=np.sign(ab[0])
#start loop over segments
z=z+1
seg=seg+1
for i in np.arange(1,nseg):
    linez[z,:]=[(seg-1)*m+1,seg*m]
    try:
        ab[z]=slope(y_filt,linez[z,:])
    except:
        ab=1       
            #ab=ab.flatten()
    linezSeg[z]=np.sign(ab[z])
    if np.sign(ab[z])==np.sign(ab[z-1]):
        linez[z-1,:]=[(seg-1-segLine)*m+1,seg*m]
        seg=seg+1
        segLine=segLine+1
    else:
        z=z+1
        seg=seg+1
        segLine=1
print(linezSeg)

