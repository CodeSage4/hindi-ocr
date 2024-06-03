from ultralytics import YOLO
import os

model = YOLO("yolov8m.pt")
model.train(data="data.yaml", epochs=25)