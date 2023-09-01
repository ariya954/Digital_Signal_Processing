input_image = imread('img.jpg');

Blurring_Filter = fspecial('disk', 10);
Blurred_Image = imfilter(input_image, Blurring_Filter, 'replicate'); 


imshow(Blurred_Image)

figure
subplot(2, 1, 1)
imshow(Blurred_Image)
subplot(2, 1, 2)
Blurring_Filter = fspecial('disk', 30);
imshow(imfilter(input_image, Blurring_Filter, 'replicate'));

figure
Blurred_Image = rgb2gray(Blurred_Image);
imagesc(abs(fftshift(fft2(Blurred_Image))));
colorbar;
%% 
[row, column, colors] = size(input_image);
Gaussian_Filter = fspecial('gaussian', [row, column], 0.5);
Gaussian_Filtered_Image = imfilter(input_image, Gaussian_Filter, 'replicate');
imshow(Gaussian_Filtered_Image);

figure
subplot(2, 1, 1)
imshow(Gaussian_Filtered_Image)
subplot(2, 1, 2)
Gaussian_Filter = fspecial('gaussian', [row, column], 0.1);
imshow(imfilter(input_image, Gaussian_Filter, 'replicate'));

figure
Gaussian_Filtered_Image = rgb2gray(Gaussian_Filtered_Image);
imagesc(abs(fftshift(fft2(rgb2gray(input_image)))));
colorbar;
%% 
Laplacian_Filter = fspecial('laplacian', 0.2);
Laplacian_Filtered_Image = imfilter(input_image, Laplacian_Filter, 'replicate');
imshow(Laplacian_Filtered_Image);

figure
subplot(2, 1, 1)
imshow(Laplacian_Filtered_Image);
subplot(2, 1, 2)
Laplacian_Filter = fspecial('laplacian', 0.9);
imshow(imfilter(input_image, Laplacian_Filter, 'replicate'));

figure
Laplacian_Filtered_Image = rgb2gray(Laplacian_Filtered_Image);
imagesc(abs(fftshift(fft2(Laplacian_Filtered_Image))));
colorbar;
%% 
Sobel_Filter = fspecial('sobel');
Sobel_Filtered_Image = imfilter(input_image, Sobel_Filter, 'replicate');
imshow(Sobel_Filtered_Image);

figure
Sobel_Filtered_Image = rgb2gray(Sobel_Filtered_Image);
imagesc(abs(fftshift(fft2(Sobel_Filtered_Image))));
colorbar;
%% 
Average_Filter = fspecial('average', 10);
Averaged_Image = imfilter(input_image, Average_Filter, 'replicate'); 
imshow(Averaged_Image);

figure
subplot(2, 1, 1)
imshow(Averaged_Image);
subplot(2, 1, 2)
Average_Filter = fspecial('average', 30);
imshow(imfilter(input_image, Average_Filter, 'replicate')); 

figure
Averaged_Image = rgb2gray(Averaged_Image);
imagesc(abs(fftshift(fft2(Averaged_Image))));
colorbar;
