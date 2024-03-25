## Image To Cartoon Using OpenCV

This repository hosts Python code designed to transform images into cartoon-like versions using the OpenCV library. The script employs a series of image processing techniques to achieve the desired effect.

Firstly, the script utilizes Gaussian Pyramid to downscale the image, creating a series of progressively smaller versions. Next, bilateral filtering is applied to preserve edges while reducing noise, enhancing the cartoon effect.

Subsequently, the script performs pyramid upsampling to reconstruct the image to its original size. Then, various image processing steps are applied, including grayscale conversion, median blur to smooth out details, and adaptive thresholding to highlight edges.

Finally, bitwise operations are used to combine the processed image with the original image, resulting in a cartoon-like representation. The generated cartoon image is then displayed and saved for further use.

Feel free to customize it further to better reflect the unique features and aspects of your project.
