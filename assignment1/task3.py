import cv2
import numpy as np

def rotate_image(image, angle):
    # extract height, width and channel from the image
    height, width, channels = image.shape
    image_center = (width / 2, height / 2)

    # define rotation matrix
    rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)

    # Compute new bounding dimensions
    abs_cos = abs(rotation_mat[0, 0])
    abs_sin = abs(rotation_mat[0, 1])
    new_width = int(height * abs_sin + width * abs_cos)
    new_height = int(height * abs_cos + width * abs_sin)

    # Adjust the rotation matrix according to new dimensions
    rotation_mat[0, 2] += new_width / 2 - image_center[0]
    rotation_mat[1, 2] += new_height / 2 - image_center[1]

    rotated_image = cv2.warpAffine(image, rotation_mat, (new_width, new_height))
    return rotated_image

def main():
    image_path = input("Enter image path: ")
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Image not found at path: {image_path}")

    rotated_45 = rotate_image(image, 45)
    rotated_90 = rotate_image(image, 90)

    cv2.imshow("Original image", image)
    cv2.imshow("45 degree rotated image", rotated_45)
    cv2.imshow("90 degree rotated image", rotated_90)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
