def solve(input_srt):
  initial_stone_arrangement = input_srt.strip().split(" ")

  # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
  # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
  # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.

  print(initial_stone_arrangement)

  for _ in range(25):
    new_stones = []
    for i, stone in enumerate(initial_stone_arrangement):
      if len(stone) % 2 == 0:
        left, right = split_in_half(stone)
        new_stones.append(left)
        new_stones.append(right)
      elif stone == '0':
        new_stones.append('1')
      else:
        new_stones.append(str(int(stone) * 2024))
    
    initial_stone_arrangement = new_stones

  #print(initial_stone_arrangement)
    
  return str(len(initial_stone_arrangement))

def split_in_half(stone):
  mid_point = len(stone) // 2
  #print(mid_point)
  left = stone[:mid_point]
  right = stone[mid_point:]

  return [str(int(left)), str(int(right))]
  