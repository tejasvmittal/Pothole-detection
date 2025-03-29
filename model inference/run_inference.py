import os
import matplotlib.pyplot as plt
import cv2
from ultralytics import YOLO

# images_path = 'C:/Users/tejas/Desktop/pothole detector/test images/normal'
best_model = YOLO("C:/Users/tejas/Desktop/pothole detector/yolo model/best.pt")

# image_files = [file for file in os.listdir(images_path) if file.endswith('.jpg')]

# Perform inference on each selected image and display it
# for path in image_files:
#     image_path = os.path.join(images_path, path)
#     results = best_model.predict(source=image_path, imgsz=640)
#     annotated_image = results[0].plot()
#     cv2.imwrite(images_path + path + "_out.jpg", annotated_image)

# DELETE BELOW FOR BATCH INFERENCE   
results = best_model.predict(source="C:/Users/tejas/Desktop/pothole detector/downloads/gsv_0.jpg", imgsz=640)
annotated_image = results[0].plot()
# annotated_image_rgb = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
cv2.imwrite("C:/Users/tejas/Desktop/pothole detector/downloads/gsv_0_out.jpg", annotated_image)
