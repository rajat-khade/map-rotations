import cv2

# Video file path
video_path = 'bmps2024-day1-match1-phase1.mp4'
output_dir = 'frames/'

# Open the video
vidcap = cv2.VideoCapture(video_path)

# Parameters
frame_interval = 60  # Extract every 60th frame
frame_count = 0
saved_count = 0

# Loop through the video frames
while True:
    success, image = vidcap.read()
    if not success:
        break  # Exit if video ends

    # Save the frame if it matches the interval
    if frame_count % frame_interval == 0:
        cv2.imwrite(f"{output_dir}frame_{saved_count}.jpg", image)
        saved_count += 1

    frame_count += 1

print(f"Frames extracted: {saved_count}")
vidcap.release()
