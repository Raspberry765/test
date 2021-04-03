import sys
import numpy as np
import matplotlib.pyplot as plt # library for plotting
from scipy.fftpack import fft, ifft
A=0.5
fc=10
phase=30
fs=32*fc
t=np.arange(start=0,stop=2,step=1/fs)

phi= phase*np.pi/180
x=A*np.cos(2*np.pi*fc*t*phi)
# fig,(ax1,ax2,ax3,ax4) = plt.subplots(nrows=4, ncols=1)
plt.subplot(3,1,1)
plt.plot(t,x)
plt.title("0.5cos")
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
plt.title("x[k]")
plt.xlabel("k")
plt.ylabel("|x[k]|")

plt.subplot(3,1,3)
plt.stem(f,abs(X),use_line_collection=True)
plt.title("x[f]")
plt.xlabel("f")
plt.ylabel("|x[f]|")

plt.show() # disply the figure



