import cv2
import numpy as np

def block_average(image, block_size):
     height, width, channels = image.shape
     output = image.copy()

     # traversing vertical and horizaontal without overlapping blocks
     for i in range(0, height - height % block_size, block_size):
          for j in range(0, width - width % block_size, block_size):
               block = image[i:i + block_size, j:j + block_size]
               # calculate the average color of each block
               avg_color = block.mean(axis=(0, 1), dtype=int)
               output[i:i + block_size, j:j + block_size] = avg_color
     return output

def main():
     image_path = input("Enter image path: ")
     image = cv2.imread(image_path)
     if image is None:
          raise FileNotFoundError(f"Image not found at path: {image_path}")

     block_avg_3x3 = block_average(image, 3)
     block_avg_5x5 = block_average(image, 5)
     block_avg_7x7 = block_average(image, 7)

     cv2.imshow("Original", image)
     cv2.imshow("3x3 Block Averaged", block_avg_3x3)
     cv2.imshow("5x5 Block Averaged", block_avg_5x5)
     cv2.imshow("7x7 Block Averaged", block_avg_7x7)

     cv2.waitKey(0)
     cv2.destroyAllWindows()

if __name__ == "__main__":
     main()