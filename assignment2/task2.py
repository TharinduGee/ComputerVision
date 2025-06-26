import cv2
import numpy as np
from collections import deque

seed_points = []

# function to define seed point with mouse click
def select_seed_point(event, x, y, flags, param):
     if event == cv2.EVENT_LBUTTONDOWN:
          seed_points.append((x, y))
          print(f"Seed point selected at: ({x}, {y})")

def region_grower(image, seed_points, threshold):
     h, w, channels = image.shape
     visited = np.zeros((h, w), dtype=np.bool_)
     segmented = np.zeros((h, w), dtype=np.uint8)
     neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 4 adjacent neighbors

     queue = deque(seed_points)

     # initialize visited and segmented
     for x, y in seed_points:
          visited[y, x] = True
          segmented[y, x] = 255

     while queue:
          x, y = queue.popleft()
          current_color = image[y, x].astype(np.int32)

          for dx, dy in neighbors:
               nx, ny = x + dx, y + dy
               if 0 <= nx < w and 0 <= ny < h and not visited[ny, nx]:
                    # extract the color of the neighbor
                    neighbor_color = image[ny, nx].astype(np.int32)

                    # calculate the eucledian distance between current and neighbor color
                    color_dist = np.linalg.norm(current_color - neighbor_color)

                    # check wheather the neighbor is within the threshold
                    if color_dist <= threshold:
                         segmented[ny, nx] = 255
                         visited[ny, nx] = True
                         queue.append((nx, ny))

     return segmented

def main():
     image_path = input("Enter image path: ")
     image = cv2.imread(image_path)
     if image is None:
          raise FileNotFoundError(f"Image not found at path: {image_path}")

     print("Instructions:\n")
     print(" - Left-click to select seed points.\n")
     print(" - Press any key when done selecting.")

     image_copy = image.copy()
     cv2.namedWindow("Select Seed Points")
     cv2.setMouseCallback("Select Seed Points", select_seed_point)

     # wait until user selects the seeds
     while True:
          cv2.imshow("Select Seed Points", image_copy)
          if cv2.waitKey(1) != -1:
               break
     cv2.destroyWindow("Select Seed Points")

     if not seed_points:
          print("No seed points selected.")
          return

     threshold = float(input("Enter color distance threshold (e.g., 0–100): "))
     mask = region_grower(image, seed_points, threshold)

     # Display and save output
     cv2.imshow("Segmented Region", mask)
     cv2.imwrite(f"region_growing_segementation_{threshold}.png", mask)

     cv2.waitKey(0)
     cv2.destroyAllWindows()

if __name__ == "__main__":
     main()
