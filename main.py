from ultralytics import YOLO
import cv2

best = 'runs/detect/train2/weights/best.pt'
test = 'yolo11n.pt'
confidence_threshold = 0.5
model = YOLO(best)


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive video")
        break

    # Run inference
    results = model.predict(source=frame, conf=confidence_threshold)
    annotated_frame = results[0].plot()

    # Show
    cv2.imshow("Pre-trained YOLO Detection", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows() #