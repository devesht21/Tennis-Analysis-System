from ultralytics import YOLO

IMG_PATH = "inputs/image.png"
VID_PATH = "inputs/input_video.mp4"

TENNIS_BALL_DETECTOR_MODEL_PATH = "training/tennis-balls/last.pt"

# model = YOLO("yolov8x")

# result = model.predict(IMG_PATH, save=True)
# result = model.predict(VID_PATH, save=True)


# model = YOLO(TENNIS_BALL_DETECTOR_MODEL_PATH)

# result = model.predict(VID_PATH, save=True)
