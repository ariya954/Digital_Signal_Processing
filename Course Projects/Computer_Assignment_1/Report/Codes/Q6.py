import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#reading images
image_file_1 = "D:/DSP/CA1/cat.jpg"
image_1 = Image.open(image_file_1)
iq = plt.imread(image_file_1)
image_file_2 = "D:/DSP/CA1/horse.jpg"
image_2 = Image.open(image_file_2)
image_2 = image_2.resize(image_1.size)


#defining 2d fft of images and their real and imaginary parts
DTFT_image_1 = np.fft.fft2(image_1)
amplitude_of_DTFT_image_1 = np.real(DTFT_image_1)
phase_of_DTFT_image_1 = np.imag(DTFT_image_1)

DTFT_image_2 = np.fft.fft2(image_2)
amplitude_of_DTFT_image_2 = np.real(DTFT_image_2)
phase_of_DTFT_image_2 = np.imag(DTFT_image_2)

#swapping amplitudes of images's DTFTs
DTFT_image_1 = amplitude_of_DTFT_image_2 + 1j * phase_of_DTFT_image_1
DTFT_image_2 = amplitude_of_DTFT_image_1 + 1j * phase_of_DTFT_image_2

#showing swaped images
image_1 = np.fft.ifft2(DTFT_image_1)
image_1 = np.array(image_1.real, dtype = int)
image_2 = np.fft.ifft2(DTFT_image_2)
image_2 = np.array(image_2.real, dtype = int)

plt.imshow(image_1)
plt.show()

plt.imshow(image_2)
plt.show()
