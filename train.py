from ultralytics import YOLO

model = YOLO("models/yolov8n.pt")  # or yolov5s.pt if using YOLOv5
model.train(data="data.yaml", epochs=50, imgsz=640)
