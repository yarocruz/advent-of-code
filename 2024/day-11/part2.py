from collections import Counter

def solve(input_srt):
  initial_stone_arrangement = input_srt.strip().split(" ")
  
  # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
  # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
  # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
  current_counts = Counter(initial_stone_arrangement)
  total_counts = sum(current_counts.values())
  print(total_counts)

  for _ in range(75):
    new_counts = Counter()
    for number, count in current_counts.items():
      
      transformed = transform_number_counts(number, count)
      new_counts.update(transformed)
      
    current_counts = new_counts
    total_counts = sum(new_counts.values())
    
  return str(total_counts)

def split_in_half(stone):
  mid_point = len(stone) // 2
  #print(mid_point)
  left = stone[:mid_point]
  right = stone[mid_point:]

  return [str(int(left)), str(int(right))]

def transform_number_counts(n, count):
  result = Counter()
  
  if len(n) % 2 == 0:
    left, right = split_in_half(n)
    result[left] += count
    result[right] += count
  elif n == '0':
    result['1'] += count
  else:
    result[str(int(n) * 2024)] += count

  return result
