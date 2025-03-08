#Script to size the flocs in an image and store in our database
from ultralytics import YOLO
import numpy as np
import db

MODEL_FILE_PATH = "src/model.pt"
model = YOLO(MODEL_FILE_PATH)

def size_image(img_path, session, db_ops):
  #img_id is 1 more than the last img id, or 0 if the database is empty 
  img_id = db_ops.get_current_image_id()
  img_id = 0 if img_id == -1 else img_id + 1
  img = db_ops.add_image(img_path)
  predict = model.predict(img_path , save = False)
  length = len(predict[0].masks.data)
  for i in range(length):
    mask = (predict[0].masks.data[i].numpy() * 255).astype("uint8")
    size = np.sum(mask == 255)
    db_ops.add_floc(img.id, size)
