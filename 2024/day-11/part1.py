import numpy as np
from itertools import combinations

def solve(input_srt):
  initial_stone_arrangement = input_srt.strip().split(" ")
  
  new_stones = []

  # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
  # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
  # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.

  for stone in initial_stone_arrangement:
    if len(stone) % 2 == 0:
      left, right = split_in_half(stone)
      new_stones.append(left)
      new_stones.append(right)
    elif stone == '0':
      new_stones.append('1')
    else:
      new_stones.append(str(int(stone) * 2024))

  print(new_stones)
    
  return str("")

def split_in_half(str):
  mid_point = len(str) // 2
  print(mid_point)
  left = str[:mid_point]
  right = str[mid_point:]

  return [remove_leading_zeroes(left), remove_leading_zeroes(right)]
  

def remove_leading_zeroes(str):
  new_str = ""
  for c in str:
    if c != '0':
      new_str += c

  return new_str

