import numpy as np
from itertools import combinations

def solve(input_srt):
  lines = input_srt.strip().split("\n")
  grid = np.array([[int(row) for row in line] for line in lines])
    
  return str("")