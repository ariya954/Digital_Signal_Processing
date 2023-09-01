import numpy as np
import matplotlib.pyplot as plt

def make_sin_function_with_given_parameters(domain, freqency, time, freqency_offset):    
    return domain * np.sin(freqency * time + freqency_offset)

def calculate_normalized_DTFT_of_given_signal_and_plot_it(input_signal, number_of_samples, sampling_rate):
    n = np.arange(-number_of_samples/2, number_of_samples/2)
    T = number_of_samples/sampling_rate
    w = n/(1000 * T)

    DTFT_input_signal = np.fft.fft(input_signal)

    plt.plot(w, abs(input_signal / max(abs(input_signal))))
    plt.legend()
    plt.show()

def aliazing_plotter(signal_frequency, sampling_frequency):
    tstart = -1
    tend = 1
    Ts = 1 / sampling_frequency
    time = np.arange(tstart, tend - Ts, Ts)
    domain = 1
    freqency_offset = 0
    number_of_samples = len(time)
    
    made_signal = make_sin_function_with_given_parameters(domain, signal_frequency, time, freqency_offset)
    
    calculate_normalized_DTFT_of_given_signal_and_plot_it(made_signal, number_of_samples, sampling_frequency)

sampling_frequency = 48000
frquencies = [100, 1000, 10000, 108000]

for i in range(len(frquencies)) :
    aliazing_plotter(frquencies[i], sampling_frequency)
