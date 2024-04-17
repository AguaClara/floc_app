#Script to size the flocs in an image and store in our database
from ultralytics import YOLO
import numpy as np
import db
import os
import base64

MODEL_FILE_PATH = os.path.join(os.path.dirname(__file__), 'model.pt')
model = YOLO(MODEL_FILE_PATH)

def size_image(img_path, session, db_ops):
  #img_id is 1 more than the last img id, or 0 if the database is empty 
  img_id = db_ops.get_current_image_id()
  img_id = 0 if img_id == -1 else img_id + 1

  # Read image file from disk
  with open(img_path, "rb") as f:
      image_data = f.read()
    
  # Encode image data to base64
  image_base64 = base64.b64encode(image_data).decode("utf-8")
  print("img_path = " + img_path)
  img = db_ops.add_image(img_path, image_base64)
  predict = model.predict(img_path , save = False)

  length = len(predict[0].masks.data)
  for i in range(length):
    mask = (predict[0].masks.data[i].numpy() * 255).astype("uint8")
    size = float(np.sum(mask == 255))
    print(size)
    db_ops.add_floc(img.id, size)