# import cv2
# import numpy as np

# # Define the HSV range for the team's color (e.g., pink)
# lower_OG_esports = np.array([85, 107, 190])  # Lower HSV values
# upper_OG_esports = np.array([85, 115, 200])  # Upper HSV values

# # Initialize variables
# player_positions = []

# # Process each frame
# for count in range(0, 40):  # Adjust for the number of frames
#     frame_path = f"frames/frame_{count}.jpg"
#     frame = cv2.imread(frame_path)

#     # Convert to HSV and create a mask for pink color
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     mask = cv2.inRange(hsv, lower_OG_esports, upper_OG_esports)

#     # Find player positions (bounding boxes)
#     contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     frame_positions = []
#     for contour in contours:
#         x, y, w, h = cv2.boundingRect(contour)
#         frame_positions.append({"x": x, "y": y, "w": w, "h": h})

#     player_positions.append({"frame": count, "positions": frame_positions})

# # Save positions to a JSON file
# import json
# with open('player_positions.json', 'w') as f:
#     json.dump(player_positions, f)
# print("Player positions saved to JSON.")

import cv2
import numpy as np
import json

# Define the HSV range for the team's color (e.g., pink)
# lower_OG_esports = np.array([84, 140, 190])  # Lower HSV values
# upper_OG_esports = np.array([86, 170, 210])  # Upper HSV values
lower_numen_esports = np.array([107, 204, 133])  # Lower HSV values
upper_numen_esports = np.array([109, 224, 153])  # Upper HSV values

# Initialize variables
player_positions = []

# Function to check if contour is approximately circular
def is_circle(contour, circularity_thresh=0.7):
    area = cv2.contourArea(contour)
    if area == 0:  # Prevent division by zero
        return False
    perimeter = cv2.arcLength(contour, True)
    circularity = (4 * np.pi * area) / (perimeter * perimeter)
    return circularity > circularity_thresh

# Process each frame
for count in range(0, 261):  # Adjust for the number of frames
    frame_path = f"frames/frame_{count}.jpg"
    frame = cv2.imread(frame_path)

    # Convert to HSV and create a mask for the team color
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_numen_esports, upper_numen_esports)

    # Find contours of the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    frame_positions = []

    for contour in contours:
        # Check if the contour is a circle
        if is_circle(contour):
            x, y, w, h = cv2.boundingRect(contour)
            frame_positions.append({"x": x, "y": y, "w": w, "h": h})

    player_positions.append({"frame": count, "positions": frame_positions})

# Save positions to a JSON file
with open('player_positions.json', 'w') as f:
    json.dump(player_positions, f)
print("Player positions saved to JSON.")
