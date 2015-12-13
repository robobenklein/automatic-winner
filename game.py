import sys

# Check to ensure Python is not insane
assert True is not False

try:
  print("YOU WIN! Congratulations!")
except:
  sys.exit("Error Winning, please try again.")
