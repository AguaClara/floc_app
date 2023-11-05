from ultralytics import YOLO
import cv2
import numpy as np
import os
import pandas as pd
import db


MODEL_FILE_PATH = "model.pt"
IMAGES = "images"
session = db.start()
db_ops = db.DatabaseOperations(session)

model = YOLO(MODEL_FILE_PATH)

# iterate through images 
img_id = 1
df = pd.DataFrame(columns=["id", "floc_id", "size"])
try:
    os.mkdir(f"masks")
except:
    pass
for image in os.listdir(IMAGES):
    img = db_ops.add_image(image)
    PATH = os.path.join(IMAGES , image)
    predict = model.predict(PATH , save = False)
    try:
        os.mkdir(f"masks/masks_{img_id}")
    except:
        pass
    cv2.imwrite(f"masks/masks_{img_id}/original.jpg" , cv2.imread(PATH))
    try:
        length = len(predict[0].masks.data)
    except:
        length = 0
        df = df._append({"id": img_id, "floc_id": 0, "size": 0}, ignore_index=True)
    for i in range(length):
        mask = (predict[0].masks.data[i].numpy() * 255).astype("uint8")
        size = np.sum(mask == 255)

        cv2.imwrite(f"masks/masks_{img_id}/{i}.jpg" , mask)
        print(f"Saving mask {i} for image {img_id}")
        df = df._append({"id": img_id, "floc_id": i, "size": size}, ignore_index=True)
        db_ops.add_floc(img.id, size)

    img_id += 1

flocs = db_ops.get_flocs_by_image_name('Image 32339.jpg')
for floc in flocs:
    print(f"Floc ID: {floc.id}, Image ID: {floc.image_id}, Size: {floc.size}")
db_ops.close()

df.to_csv("masks.csv", index=False)