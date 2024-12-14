import numpy as np
import re

def solve(input_srt):
  lines = input_srt.splitlines()
  # build out the machines
  machines = []
  current_group = []
  for line in lines:
      if not line.strip():
          if current_group:
              machines.append(current_group)
              current_group = []
      else:
          current_group.append(line)
  if current_group:
      machines.append(current_group)

  token_count = 0
    
  # for each machine:
  # create vector A coeficient, vector b for constants,
  for machine in machines:
      # extract the numbers from button a and b
      btn_a = re.findall(r"\d+", machine[0])
      btn_b = re.findall(r"\d+", machine[1])

      A = np.array([[int(n) for n in btn_a], [int(n) for n in btn_b]]).T
      constants = re.findall(r"\d+", machine[2])
      b = np.array([10000000000000 + int(const) for const in constants])
      print(b)

      if np.linalg.det(A) == 0:
        print("The system has no unique solution.")
      else:
          solution = solve_and_check(A, b)
          if solution:
              button_A, button_B = solution
              token_count += (button_A * 3) + (button_B * 1)          

  print(token_count)

  return str(token_count)

def solve_and_check(A, b):
  try:
      # Solve the system of equations
      solution = np.linalg.solve(A, b)
      
      # Check if each solution is close to an integer
      integer_solution = []
      is_integer = True
      for sol in solution:
          if is_whole_number(sol):  # Close to an integer
              integer_solution.append(int(round(sol)))
          else:
              integer_solution.append(sol)
              is_integer = False
      
      # Print the result
      if is_integer:
          print(f"The solution is integers: {integer_solution}")
      else:
          print(f"The solution includes non-integers: {solution}")
      
      return integer_solution if is_integer else None
  except np.linalg.LinAlgError as e:
      print(f"Error: {e}")
      return None
  
def is_whole_number(value, tol=1e-2):
    """
    Check if a floating-point number is effectively a whole number.
    Args:
    - value (float): The number to check.
    - tol (float): Tolerance for floating-point comparison (default: 1e-9).
    
    Returns:
    - bool: True if the value is a whole number, False otherwise.
    """
    return abs(value - round(value)) < tol

# 10000000000000
# 10000000000000
# 1000000000
# 1000000000
# 10000000008400
# 10000000005400



