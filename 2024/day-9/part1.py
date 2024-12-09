import numpy as np
from itertools import combinations

def solve(input_srt):
  disk_map = input_srt
  ids = []
  id = 0

  for i, val in enumerate(disk_map):
    print(i, val)
    
    # if we are at even idx number
    if i % 2 == 0:
      for _ in range(int(val)):
        ids.append(id)
      id += 1
    else:
      for _ in range(int(val)):
        ids.append('.')

  print(ids)
    
  return str("")
