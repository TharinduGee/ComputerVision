import cv2 
import numpy as np

def reduce_intensity(image, levels):
     # check the constraints using bitwise AND
     if levels <= 1 or levels > 256 or (levels & (levels - 1)) != 0:
        raise ValueError("Levels must be in the range of 2–256 and must be a power of 2.")
     
     factor = 256 // levels
     reduced_image = (image // factor) * factor

     return reduced_image

def main():
     image_path = str(input("Enter the relative path of the image: "))
     image = cv2.imread(image_path)
     if image is None:
        raise FileNotFoundError(f"Image not found at path: {image_path}")

     levels = int(input("Enter the number of intensity levels as power of 2: "))

     reduced_image = reduce_intensity(image, levels)
     output_path = f"reduced_image-{levels}_levels.jpg"
     cv2.imwrite(output_path, reduced_image)
     print(f"Output saved as {output_path}")

     cv2.waitKey(0)
     cv2.destroyAllWindows()

if __name__ == "__main__":
     main()
     


     