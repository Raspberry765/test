import sys
import numpy as np
import matplotlib.pyplot as plt # library for plotting
from scipy.fftpack import fft, ifft
np.set_printoptions(formatter={"float_kind":lambda x: "%g" % x})

A=0.5
fc=10
phase=30
fs=32*fc
t=np.arange(start=0,stop=2,step=1/fs)
x=A*np.cos(2*np.pi*fc*t)


# fig,(ax1,ax2,ax3,ax4) = plt.subplots(nrows=4, ncols=1)
plt.subplot(3,1,1)
plt.plot(t,x)
plt.title("$x[n]=0.5cos(2 \pi 10 t)$")
plt.xlabel("time")
plt.ylabel("x(t)")
# plt.plot(t,x,marker="o", color = "blue", linestyle = "-") # plot using pyplot library from matplotlib package
# plt.title('Sine wave f='+str(fc)+' Hz') # plot title 
# plt.xlabel('Time (s)') # x-axis label
# plt.ylabel('Amplitude') # y-axis label
# plt.show() # disply the figure

N=256
X=fft(x,N)

df=fs/N
sampleIndex= np.arange(start=0,stop=N)
f=sampleIndex*df

plt.subplot(3,1,2)
plt.stem(sampleIndex,abs(X),use_line_collection=True)
plt.title("abs(x[k])")
plt.xlabel("k")
plt.ylabel("amplitude")

plt.subplot(3,1,3)
plt.stem(f,abs(X),use_line_collection=True)
plt.title("abs(x[k])")
plt.xlabel("frequency")
plt.ylabel("amplitude")

plt.show() # disply the figure



