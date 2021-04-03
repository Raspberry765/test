import sys
import numpy as np
import matplotlib.pyplot as plt # library for plotting

sys.path.append('path_where_digicommpy_resides')
from DigiCommPy.chapter_1.signalgen import sine_wave
f=10
overSampRate=30
phase = 1/2*np.pi
nCyl = 1000
(t,g) = sine_wave(f,overSampRate,phase,nCyl)
plt.plot(t,g,marker="o", color = "blue", linestyle = "-") # plot using pyplot library from matplotlib package
plt.title('Sine wave f='+str(f)+' Hz') # plot title 
plt.xlabel('Time (s)') # x-axis label
plt.ylabel('Amplitude') # y-axis label
plt.show() # disply the figure