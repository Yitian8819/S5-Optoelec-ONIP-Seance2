import numpy as np
import matplotlib.pyplot as plt

# Exercice 1
def fonction_sin(t,a,f):
    return (a * np.sin(t * 2 * np.pi))

T = np.linspace(0,499,500)

sin_a = fonction_sin(T,1,200)
sin_b = fonction_sin(T,2,287)
plt.figure(1)
plt.plot(T,sin_a,'r',T,sin_b,'b',label = 'sin_b')

sin_c = sin_a + sin_b
plt.figure(2)
plt.plot(T,sin_c,'b',label = 'sin_c')

FFT_sin_c = np.fft.fft(sin_c)
Freq = np.fft.fftfreq(500,T[1])
plt.figure(3)
plt.plot(Freq,np.real(FFT_sin_c),label = 'FFT_sin_c')
plt.legend()
plt.show()