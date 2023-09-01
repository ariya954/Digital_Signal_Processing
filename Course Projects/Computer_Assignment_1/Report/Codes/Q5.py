import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

def M_down_sample(M, input_signal):
    output_signal = np.zeros(int(len(input_signal) / M))
    for i in range(len(output_signal)):
        output_signal[i] = input_signal[M * i]
    return output_signal

def L_up_sample(L, input_signal):
    output_signal = np.zeros(int(len(input_signal) * L))
    for i in range(len(input_signal)):
        output_signal[L * i] = input_signal[i]
    return output_signal

#part a
file_name = "test.wav"
sample_rate, data = wavfile.read(file_name, mmap = False)
print(sample_rate)

#part b
wavfile.write("test result.wav", sample_rate, data[60 * sample_rate : 71 * sample_rate])

#part p
wavfile.write("test result(fs).wav", sample_rate, data[60 * sample_rate : 71 * sample_rate])
wavfile.write("test result(2fs).wav", 2 * sample_rate, data[60 * sample_rate : 71 * sample_rate])
wavfile.write("test result(0.5fs).wav", int(0.5 * sample_rate), data[60 * sample_rate : 71 * sample_rate])

#part t
voice = data[60 * sample_rate : 71 * sample_rate]
voice = voice[:,0]

#defining frequency domain
N = len(voice)
n = np.arange(-N/2, N/2)
T = N/sample_rate
w = n/T

DTFT_voice = np.fft.fft(voice)
DTFT_voice = np.fft.fftshift(DTFT_voice)

plt.plot(w, abs(DTFT_voice / max(abs(DTFT_voice))))
plt.legend()
plt.show()

#part g M = 2
DTFT_voice_2_down_sample = np.fft.fft(M_down_sample(2, voice))
DTFT_voice_2_down_sample = np.fft.fftshift(DTFT_voice_2_down_sample)

N2 = N / 2
n = np.arange(-N2/2, N2/2)
T = N2/sample_rate
w = n/T

plt.plot(w, abs(DTFT_voice_2_down_sample / max(abs(DTFT_voice_2_down_sample))))
plt.legend()
plt.show()

#part g M = 5
DTFT_voice_5_down_sample = np.fft.fft(M_down_sample(5, voice))
DTFT_voice_5_down_sample = np.fft.fftshift(DTFT_voice_5_down_sample)

N3 = N / 5
n = np.arange(-N3/2, N3/2)
T = N3/sample_rate
w = n/T

plt.plot(w, abs(DTFT_voice_5_down_sample / max(abs(DTFT_voice_5_down_sample))))
plt.legend()
plt.show()

#part g M = 6
DTFT_voice_6_down_sample = np.fft.fft(M_down_sample(6, voice))
DTFT_voice_6_down_sample = np.fft.fftshift(DTFT_voice_6_down_sample)

N6 = N / 6
n = np.arange(-N6/2, N6/2)
T = N6/sample_rate
w = n/T

plt.plot(w, abs(DTFT_voice_6_down_sample / max(abs(DTFT_voice_6_down_sample))))
plt.legend()
plt.show()

#part h L = 2
DTFT_voice_2_up_sample = np.fft.fft(L_up_sample(2, voice))
DTFT_voice_2_up_sample = np.fft.fftshift(DTFT_voice_2_up_sample)

N2 = N * 2
n = np.arange(-N2/2, N2/2)
T = N2/sample_rate
w = n/T

plt.plot(w, abs(DTFT_voice_2_up_sample / max(abs(DTFT_voice_2_up_sample))))
plt.legend()
plt.show()

#part h L = 5
DTFT_voice_5_up_sample = np.fft.fft(L_up_sample(5, voice))
DTFT_voice_5_up_sample = np.fft.fftshift(DTFT_voice_5_up_sample)

N3 = N * 5
n = np.arange(-N3/2, N3/2)
T = N3/sample_rate
w = n/T

plt.plot(w, abs(DTFT_voice_5_up_sample / max(abs(DTFT_voice_5_up_sample))))
plt.legend()
plt.show()

#part h L = 6
DTFT_voice_6_up_sample = np.fft.fft(L_up_sample(6, voice))
DTFT_voice_6_up_sample = np.fft.fftshift(DTFT_voice_6_up_sample)

N6 = N * 6
n = np.arange(-N6/2, N6/2)
T = N6/sample_rate
w = n/T

plt.plot(w, abs(DTFT_voice_6_up_sample / max(abs(DTFT_voice_6_up_sample))))
plt.legend()
plt.show()
