[input_audio, Fs] = audioread('y.wav');

N = length(input_audio);
DTFT_input_audio = fftshift(fft(input_audio));
freq_axis = -Fs/2 : Fs/N : Fs/2 - Fs/N;
DTFT_input_audio = DTFT_input_audio / max(abs(DTFT_input_audio));

plot(freq_axis, abs(DTFT_input_audio));
title('input audio DTFT');

[Rmm, lags] = xcorr(input_audio, 'unbiased');
Rmm = Rmm(lags > 0);
lags = lags(lags > 0);

figure
plot(lags/Fs, Rmm)
xlabel('Lag (s)')
title('Xcorr');
[peaks, locations_of_peaks] = findpeaks(Rmm, lags, 'MinPeakHeight', 0.002);

delays = zeros(1, max(locations_of_peaks) + 1);
delays(1) = 1;
delays(locations_of_peaks(1) + 1) = peaks(1) / Rmm(1);
delays(locations_of_peaks(2) + 1) = peaks(2) / Rmm(1);

Non_echo_audio = filter(1, delays, input_audio);

%soundsc(Non_echo_audio, Fs)

audiowrite('Non_echo.wav', Non_echo_audio, Fs);

freqz(Kiaser_Coefficients)

filtered_sound = filter(Kiaser_Coefficients, Non_echo_audio);

figure
t = 1 : length(filtered_sound);
subplot(2,1,1);
plot(t, Non_echo_audio);
title('Non echo audio');
subplot(2,1,2);
plot(t, filtered_sound);
title('filtered sound(x)');

soundsc(filtered_sound, Fs)