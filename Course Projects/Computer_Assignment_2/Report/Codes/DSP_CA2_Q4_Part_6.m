[input_audio, Fs] = audioread('NoisySound.wav');
%sound(input_audio, Fs);

freqz(BS_Coefficients); %open DSP_CA2_Q4_Filter.fda - go to files menu at top of the page - click on Export... - type Coefficeints in Num part(Export as object)
freqz(HighPass_Coefficients);

filtered_sound = filter(BS_Coefficients, input_audio);

audiowrite('bs_filtered_sound.wav', filtered_sound, Fs);

filtered_sound = filter(HighPass_Coefficients, filtered_sound);

sound(filtered_sound, Fs)

N = length(input_audio);
DTFT_input_audio = fftshift(fft(input_audio));
freq_axis = 0 : Fs/(2 * N) : Fs/2 - Fs/(2 * N);
plot(freq_axis, abs(DTFT_input_audio) / max(abs(DTFT_input_audio)));
title('Original Signal DTFT')

figure
DTFT_filtered_sound = fftshift(fft(filtered_sound));
plot(freq_axis, abs(DTFT_filtered_sound) / max(abs(DTFT_filtered_sound)));
title('Filtered Signal DTFT')

figure
t = 1 : length(input_audio);
plot(t, input_audio(t));
title('Original Signal')

figure
plot(t, filtered_sound(t));
title('Filtered Signal')