import cv2
import numpy as np

# Mouse callback function to pick a color
def pick_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button click
        pixel = hsv[y, x]
        print(f"Selected HSV Color: {pixel}")
        
        lower_bound = np.array([max(0, pixel[0] - 15), max(100, pixel[1] - 40), max(100, pixel[2] - 40)])
        upper_bound = np.array([min(179, pixel[0] + 15), min(255, pixel[1] + 40), min(255, pixel[2] + 40)])

        print(f"Lower HSV: {lower_bound}, Upper HSV: {upper_bound}")

# Load an image or video frame
image = cv2.imread("frames/frame_0.jpg")  # Change to your video frame
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Display the image
cv2.imshow("Pick a Color", image)
cv2.setMouseCallback("Pick a Color", pick_color)

cv2.waitKey(0)
cv2.destroyAllWindows()
