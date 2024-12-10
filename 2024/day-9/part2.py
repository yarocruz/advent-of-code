import numpy as np
from itertools import combinations

def solve(input_srt):
  disk_map = input_srt
  ids = []
  id = 0

  file_positions = {}

  # create the id list
  for i, val in enumerate(disk_map):
    
    # if we are at even idx number
    if i % 2 == 0:
      for _ in range(int(val)):
        ids.append(id)
      id += 1
    else:
      for _ in range(int(val)):
        ids.append('.')

  print(ids)
 
  # build the file positions dict
  for i, block in enumerate(ids):
     if block == '.':
        continue
     else:
        file_id = block
        if file_id not in file_positions:
           file_positions[file_id] = [i, i]
        else:
           file_positions[file_id][1] = i

  # Convert lists to tuples for consistency
  for file_id in file_positions:
      start, end = file_positions[file_id]
      file_positions[file_id] = (start, end)
        
  max_file_id = max(file_positions.keys())
  print(max_file_id)

  # Iterate over files in descending order of their IDs
  for file_id in range(max_file_id, -1, -1):
      start_idx, end_idx = file_positions[file_id]
      file_length = end_idx - start_idx + 1

      # Find a segment of free space to the left of start_idx that can fit the entire file
      free_segment_start = find_free_segment(ids, file_length, start_idx)

      if free_segment_start is not None:
          # Move the entire file:
          # 1. Mark old file position as '.'
          for i in range(start_idx, end_idx + 1):
              ids[i] = '.'
          
          # 2. Move file blocks into the chosen free segment
          for i in range(file_length):
              ids[free_segment_start + i] = file_id
          
          # Update file_positions to reflect the new location of the file
          new_start = free_segment_start
          new_end = free_segment_start + file_length - 1
          file_positions[file_id] = (new_start, new_end)

  result = 0
  for idx, id in enumerate(ids):
    if id != '.':
      result += idx * id  

  print(result)
    
  return str(result)

# A helper function to find a suitable free segment for a given file length L
# to the left of a given index limit (the start of the file).
def find_free_segment(disk, length_needed, right_limit):
    # Search from the start of the disk up to right_limit - 1
    # for a contiguous run of '.' of at least length_needed.
    count = 0
    start = 0
    best_start = None
    
    for i in range(right_limit):
        if disk[i] == '.':
            if count == 0:
                start = i
            count += 1
            if count == length_needed:
                # We found a suitable segment
                best_start = start
                break
        else:
            # Reset count if we hit a non-free block
            count = 0
    
    return best_start
