

def solve(input_srt):
  disk_map = input_srt
  ids = []
  id = 0

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
  pointer = 0
  # # build the new order start from the end
  for _, id in enumerate(ids[::-1]):
    while pointer < len(ids) - 1:
      if ids[pointer] == '.':
        ids[pointer] = id
        
        ids.pop()
        break
      pointer += 1

  print(ids)
  # do the checksum
  result = 0
  for idx, id in enumerate(ids):
    result += idx * id  

  print(result)
    
  return str(result)