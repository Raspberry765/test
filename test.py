import sys
import numpy as np
import matplotlib.pyplot as plt # library for plotting
from scipy.fftpack import fft, ifft, fftshift, ifftshift
np.set_printoptions(formatter={"float_kind":lambda x: "%g" % x})

A=0.5
fc=10
phase=30*np.pi/180
fs=32*fc
t=np.arange(start=0,stop=2,step=1/fs)
x=A*np.sin(2*np.pi*fc*t+phase)

N=256
X=fftshift(fft(x,N))
X_dft=1/N*X

phase_info=np.arctan2(np.imag(X_dft),np.real(X_dft))*180/np.pi
X_zero=X_dft
threshold=max(abs(X))/10000
X_zero[abs(X)<threshold]=0 # maskout values below the threshold
phase_info_zero=np.arctan2(np.imag(X_zero),np.real(X_zero))*180/np.pi

x_recon= N*ifft(ifftshift(X),N)
t_axis_recon=np.arange(start=0, stop=len(x_recon))/fs

df=fs/N
sampleIndex= np.arange(start=-N/2,stop=N/2)
f=sampleIndex*df
# fig,(ax1,ax2,ax3,ax4) = plt.subplots(nrows=4, ncols=1)
plt.subplot(4,1,1)
plt.plot(t,x)
plt.title("$x[n]=0.5cos(2 \pi 10 t + \pi/6)$")
plt.xlabel("time")
plt.ylabel("x(t)")
# plt.plot(t,x,marker="o", color = "blue", linestyle = "-") # plot using pyplot library from matplotlib package
# plt.title('Sine wave f='+str(fc)+' Hz') # plot title 
# plt.xlabel('Time (s)') # x-axis label
# plt.ylabel('Amplitude') # y-axis label
# plt.show() # disply the figure


plt.subplot(4,1,2)
plt.stem(f,abs(X_dft),use_line_collection=True)
plt.xlim(-30,30)
plt.title("abs(x[k])")
plt.xlabel("frequency")
plt.ylabel("amplitude")

plt.subplot(4,1,3)
plt.plot(f,phase_info_zero)
plt.title("Phase spectrum")
plt.xlabel("k")
plt.ylabel("$ \theta $")

plt.subplot(4,1,4)
plt.plot(t_axis_recon,x_recon)
plt.title("$x[n]=0.5cos(2 \pi 10 t + \pi/6)$")
plt.xlabel("time")
plt.ylabel("x(t)")
# plt.plot(sampleIndex,ifft(X,256))
# plt.title("reconstruction $x[n]=0.5cos(2 \pi 10 t)$")
# plt.xlabel("time")
# plt.ylabel("x(t)")

plt.show() # disply the figure



