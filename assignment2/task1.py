import numpy as np
import matplotlib.pyplot as plt
import cv2
from scipy.ndimage import gaussian_filter

def create_synthetic_image(shape=(1000, 1000)):

     image = np.zeros(shape, dtype=np.uint8)

     # assign value 85 for first object
     image[100:300, 100:600] = 85
     # assign value 170 for second object 
     image[450:900, 800:900] = 170

     return image

# mean and std can be define to add gaussian noise
def add_gaussian_noise(image, mean=127, std=20):

     noise = np.random.normal(mean, std, image.shape)
     # add noise to image
     noisy_image = image.astype(np.float32) + noise
     # clip value to the 8-bit range
     return np.clip(noisy_image, 0, 255).astype(np.uint8)

def otsu_threshold(image):
     # compute histogram for all 256 value range
     histogram, bins = np.histogram(image.flatten(), bins=256, range=(0, 256))
     total = image.size
     sum_total = np.dot(np.arange(256), histogram)

     sumB = 0
     weightB = 0
     max_var = 0
     threshold = 0

     for t in range(256):
          # update background class weight
          weightB += histogram[t]
          if weightB == 0:
               continue
        
          # compute foreground class weight 
          weightF = total - weightB
          if weightF == 0:
               break

          # compute class means    
          sumB += t * histogram[t]
          meanB = sumB / weightB
          meanF = (sum_total - sumB) / weightF

          # compute between class varaince
          between_var = weightB * weightF * (meanB - meanF) ** 2

          # update maximum threshold 
          if between_var > max_var:
               max_var = between_var
               threshold = t

     return threshold

# binarize image using theshold
def binary_image(image, threshold):
     return (image > threshold).astype(np.uint8) * 255

def main():
     try:
          mean = float(input("Enter mean of Gaussian noise: "))
          std = float(input("Enter std deviation of Gaussian noise: "))
     except ValueError:
          print("Invalid input : Please enter numeric values.")
          return

     original_image = create_synthetic_image()

     noisy_image = add_gaussian_noise(original_image, mean, std)
     otsu_thresh = otsu_threshold(noisy_image)
     binary_img = binary_image(noisy_image, otsu_thresh)

     print(f"Otsu Threshold Value: {otsu_thresh}")

     cv2.imshow("Original Image", original_image)
     cv2.imshow("Noisy Image", noisy_image)
     cv2.imshow(f"Binarized Image - Otsu threshold {otsu_thresh}", binary_img)

     cv2.imwrite("generated_image.jpg", original_image)
     cv2.imwrite("noisy_image.jpg", noisy_image)
     cv2.imwrite(f"binarized_otsu_{otsu_thresh}.jpg", binary_img)

     cv2.waitKey(0)
     cv2.destroyAllWindows()

if __name__ == "__main__":
     main()
