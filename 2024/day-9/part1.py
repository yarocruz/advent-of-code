import numpy as np
from itertools import combinations

def solve(input_srt):
  disk_map = input_srt
  ids = []
  id = 0

  # create the id list
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

  # start from the end
  for end_idx, id in enumerate(ids[::-1]):
    idx = ids.index('.')
    print(idx)
    # swap
    ids[idx] = id
    ids[end_idx] = '.'

  print(ids)
    
  return str("")
