import cv2
import numpy as np

def spatial_average(image):
    
     # function to define the custom size kernal to perform spatial average 
     def average_kernel(size):
          return np.ones((size, size), dtype=np.float32) / (size * size)

     # using filter2D method to iterate the kernal as a filter, through out the image
     spatial_avg_3x3 = cv2.filter2D(image, -1, average_kernel(3))
     spatial_avg_10x10 = cv2.filter2D(image, -1, average_kernel(10))
     spatial_avg_20x20 = cv2.filter2D(image, -1, average_kernel(20))

     cv2.imshow('Original Image', image)
     cv2.imshow('3x3 Average', spatial_avg_3x3)
     cv2.imshow('10x10 Average', spatial_avg_10x10)
     cv2.imshow('20x20 Average', spatial_avg_20x20)

     cv2.imwrite('3x3 Average.jpg', spatial_avg_3x3)
     cv2.imwrite('10x10 Average.jpg', spatial_avg_10x10)
     cv2.imwrite('20x20 Average.jpg', spatial_avg_20x20)

     cv2.waitKey(0)
     cv2.destroyAllWindows()

def main():
     image_path = str(input("Enter the relative path of the image: "))
     image = cv2.imread(image_path)
     if image is None:
        raise FileNotFoundError(f"Image not found at path: {image_path}")
     
     spatial_average(image);

if __name__ == "__main__":
     main()


