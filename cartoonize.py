import cv2
import numpy as np

n_gpd = 5
n_bf = 15

img = cv2.imread("image.jpg")
img = cv2.resize(img, (400, 250))

# Gaussian Pyramid
gpArray = [img.copy()]
for i in range(n_gpd):
    gpArray.append(cv2.pyrDown(gpArray[-1]))

# Bilateral Filtering
for i in range(n_bf):
    gpArray[-1] = cv2.bilateralFilter(gpArray[-1], d=15, sigmaColor=15, sigmaSpace=15)

# Pyramid Upsampling
for i in range(n_gpd):
    gpArray.append(cv2.pyrUp(gpArray[-1]))

# Image Processing
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred_img = cv2.medianBlur(grayscaled_img, 7)
edged_img = cv2.adaptiveThreshold(blurred_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 5)
colored_img = cv2.cvtColor(edged_img, cv2.COLOR_GRAY2RGB)
cartoonized_img = cv2.bitwise_and(img, colored_img)

# Display Images
stack = np.hstack([img, cartoonized_img])
cv2.imshow("Original vs. Cartoonized", stack)

# Generate Cartoon Image
cartoonized_img = cv2.resize(cartoonized_img,(800,500))
cv2.imwrite("cartoon.jpg", cartoonized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()