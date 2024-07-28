from src.get_img import imgArr
import numpy as np
from const import *
from src.MemAlgorithms.first_fit import firstFit
import time

if __name__ == '__main__':
  
  # Main Loop to get to every Image
  tic = time.perf_counter()
  for i in range(1, 1168):
    file_name = f'imagesData/kirmizi {i}.jpg'
    arr = imgArr(file_name)
    val = firstFit(arr, memory_blocks)
    print(f'Done with {i}')
  
  toc = time.perf_counter()

  print(f'It took {toc - tic:0.4f} to complete')
