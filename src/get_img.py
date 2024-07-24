from PIL import Image
import numpy as np

def imgArr(imgPath: str): 
  img = Image.open(imgPath)

  return np.ravel(np.array(img))