import sys
import numpy as np
import matplotlib.pyplot as plt # library for plotting
from scipy.signal import chirp
from scipy.fftpack import fft, ifft, fftshift, ifftshift
from DigiCommPy.essentials import analytic_signal
from scipy.signal import hilbert
from DigiCommPy.chapter_1.demo_scripts import hilbert_phase_demod

fc=210
fm=10
alpha=1
theta=np.pi/4
beta=np.pi/5

receiverKnowsCarrier=False
fs=8*fc
duration=0.5
t=np.arange(start=0,stop=duration, step=1/fs)

#Phase Modulation
m_t=alpha*np.sin(2*np.pi*fm*t+theta)
x=np.cos(2*np.pi*fc*t+beta+m_t)



mu=0; sigma=0.1
n=np.random.normal(loc=0.0, scale=0.1,size=len(t))
r=x+n

print(n)

z=hilbert(r)
inst_phase=np.unwrap(np.angle(z))

if receiverKnowsCarrier:
    offsetTerm= 2*np.pi*fc*t+beta
else:
    p=np.polyfit(x=t,y=inst_phase,deg=1)
    estimated=np.polyval(p,t)
    offsetTerm= estimated

demodulated = inst_phase- offsetTerm

fig1, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
ax1.plot(t,m_t)
ax1.set_title("Modulating signal")
ax1.set_xlabel("t")
ax1.set_ylabel("m(t)")

ax2.plot(t,x)
ax2.set_title("Modulated Signal")
ax2.set_xlabel("t");ax2.set_ylabel('x(t)')
plt.show()

fig2, ax3 = plt.subplots()
ax3.plot(t,demodulated)
ax3.set_title("Demodulated signal")
ax3.set_xlabel("n")
ax3.set_ylabel(r"$\hat{m(t)}$");
plt.show()