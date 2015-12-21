import sys

# Check to ensure Python is not insane
assert True is not False

try:
  print("YOU WIN! Congratulations!")
except: # If this ever executes there is a real problem!
  print("There was an error winning by Standard output, trying other win methods.")
  try:
    import webbrowser
    webbrowser.open("http://icdn4.digitaltrends.com/image/a_winner_is_you_1024-1024x768.jpg", 2)t
  except:
    print("Could not deliver win message, you technically win still, since you've clearly beat me.")
    print("Congrats!")
