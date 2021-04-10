import sys
import numpy as np
import matplotlib.pyplot as plt # library for plotting
from scipy.signal import chirp
from scipy.fftpack import fft, ifft, fftshift, ifftshift
from DigiCommPy.essentials import analytic_signal

fs=600
t=np.arange(start=0,stop=1,step=1/fs)
a_t=1+0.7*np.sin(2*np.pi*3*t)
c_t=chirp(t,f0=20,t1=t[-1],f1=80,phi=0,method='linear')
x=a_t*c_t

fig, (ax1, ax2) = plt.subplots(nrows=2,ncols=1)
ax1.plot(x)
z=analytic_signal(x)
inst_amplitude=abs(z)
inst_phase=np.unwrap(np.angle(z))
inst_freq=np.diff(inst_amplitude)/(2*np.pi)*fs

extracted_carrier= np.cos(inst_phase)
ax1.plot(inst_amplitude,"r")
ax1.set_title("Modulated signal and extracted envelope")
ax1.set_xlabel("n");ax1.set_ylabel(r'x(t) and $|z(t)|$')
ax2.plot(extracted_carrier)
ax2.set_title("Extracted carrier of TFS")
ax2.set_xlabel("n");ax2.set_ylabel(r'$cos[\omega(t)]$')
plt.show()