from ultralytics import YOLO
import cv2
import numpy as np
import os
import pandas as pd

MODEL_FILE_PATH = "model.pt"
IMAGES = "images"

model = YOLO(MODEL_FILE_PATH)

# iterate through images 
img_id = 1
df = pd.DataFrame(columns=["id", "floc_id", "size"])

for image in os.listdir(IMAGES):
    PATH = os.path.join(IMAGES , image)
    predict = model.predict(PATH , save = True , save_txt = True)

    length = len(predict[0].masks.data)
    for i in range(length):
        mask = (predict[0].masks.data[i].numpy() * 255).astype("uint8")
        size = np.sum(mask == 255)
        cv2.imwrite(f"masks/masks_{img_id}/{i}.jpg" , mask)
        df = df.append({"id": img_id, "floc_id": i, "size": size}, ignore_index=True)

    img_id += 1

df.to_csv("masks.csv", index=False)