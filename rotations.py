import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the images
players_image_path = 'frames/frame_1.jpg'  # Player positions
erangel_map_path = 'erangle-map.webp'  # Erangel map

# Load images
players_img = cv2.imread(players_image_path)
erangel_map = cv2.imread(erangel_map_path)

# Resize Erangel map to match the grid dimensions if necessary
erangel_map = cv2.resize(erangel_map, (players_img.shape[1], players_img.shape[0]))

# Step 2: Define player coordinates manually or use color detection
# For simplicity, we'll manually mark coordinates (replace with actual values)
player_positions = {
    'player1': (300, 500),  # Example coordinates (x, y)
    'player2': (400, 600),
    'player3': (600, 800),
    # Add more players as needed
}

# Step 3: Define the safe zone circle (from player image)
safe_zone_center = (650, 400)  # Example safe zone center coordinates
safe_zone_radius = 300  # Example safe zone radius in pixels

# Step 4: Draw player positions and trajectories
output_img = erangel_map.copy()

# Draw player starting positions
for player, pos in player_positions.items():
    cv2.circle(output_img, pos, 10, (0, 255, 0), -1)  # Green circle for player

# Draw player trajectories (moving toward the safe zone)
for player, pos in player_positions.items():
    cv2.line(output_img, pos, safe_zone_center, (255, 0, 0), 2)  # Blue lines for paths

# Draw the safe zone
cv2.circle(output_img, safe_zone_center, safe_zone_radius, (0, 0, 255), 2)  # Red circle for safe zone

# Step 5: Display the output map
output_img_rgb = cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(12, 8))
plt.imshow(output_img_rgb)
plt.title("Player Positions and Trajectories on Erangel Map")
plt.axis('off')
plt.show()

# Optionally save the output
cv2.imwrite("output_erangel_map_with_paths.jpg", output_img)
