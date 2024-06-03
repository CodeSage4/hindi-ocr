import cv2
from ultralytics import YOLO
import easyocr
import numpy as np


reader=easyocr.Reader(["hi"])
model = YOLO("best.pt")

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH , 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT , 480) 


i = 1
while cap.isOpened():
    ret, frame = cap.read()

    i += 1


    if not ret:
        break

    try:
        if i % 10 == 0: 
            results = model.predict(frame)
            roi = frame[y1:y2, x1:x2]
            text=reader.readtext(roi)

        for r in results:
            x1, y1, x2, y2 = map(int, r.boxes.xyxy[0][:4])
            conf = float(r.boxes.conf)
            cls = int(r.boxes.cls)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(frame, f"{cls} {conf:.2f}", (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            if text != []:
                print("Text:", text[0][1])

            

    except Exception as e:
        continue

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
