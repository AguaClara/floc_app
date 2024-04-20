#Script to size the flocs in an image and store in our database
from ultralytics import YOLO
import numpy as np
import os

MODEL_FILE_PATH = os.path.join(os.path.dirname(__file__), 'model.pt')
model = YOLO(MODEL_FILE_PATH)

def size_image(img_path):

  predict = model.predict(img_path , save = False)
  
  if not predict[0].masks:
    print("no flocs detected in this image")
    return []

  length = len(predict[0].masks.data)
  flocs = []
  for i in range(length):
    mask = (predict[0].masks.data[i].numpy() * 255).astype("uint8")
    size = float(np.sum(mask == 255))
    print(size)
    flocs.append(size)

  return flocs 