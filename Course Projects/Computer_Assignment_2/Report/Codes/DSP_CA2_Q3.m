[input_audio, Fs] = audioread('Arnold.wav');
[censoring_voice, Fs] = audioread('California.wav');

[Rmm, lags] = xcorr(input_audio, censoring_voice);
Rmm = Rmm(lags > 0);
Rmm = Rmm / max(Rmm);
lags = lags(lags > 0);

figure
plot(lags/Fs, Rmm)
xlabel('Lag (s)')

[peaks, locations_of_peaks] = findpeaks(Rmm, lags, 'MinPeakProminence', 1);
for i = 1 : length(locations_of_peaks)
    for j = 1 : length(censoring_voice)
        input_audio(locations_of_peaks(i) + j) = sin(1000 * j);
    end
end
sound(input_audio, Fs);
audiowrite('censored.wav', input_audio, Fs);