#!/usr/bin/env python3
# GitHub 06.2: Returning a Rocket Launch

# Task 1. Modify the function countdown()
def countdown(secs):

  # Initialize count down message
  msg = None
  if secs == -60:
    msg = "T-60 Seconds"
  elif secs == -30:
    msg = "T-30 Seconds"
  elif secs == -15:
    msg = "T-15 Seconds"
  elif secs == -4:
    msg = "Four stage engine start."
  elif secs >= -10 and secs < 0:
    msg = str(abs(secs))
  elif secs == 0:
    msg = "0\nBooster Ignition\nand lift off of Artemis I."
  elif secs == 2:
    msg = "We rise together to the moon and beyond!"
  # Return the count down message
  return msg


def main():
  # Task 2. Manually test by taking input for seconds variable
  seconds = int(input("Enter Seconds to Launch: "))
  if seconds > 0:
    seconds = seconds * -1
  # Tip, if positive number entered convert to a negative for start of count
    
  while seconds <= 10:
    
    msg = countdown(seconds)
    
    if msg != None:
      print(msg)
    
    seconds = seconds + 1

  # Task 3. Modify Loop Condition and Call Count Down Function



# DO NOT MODIFY BELOW
if __name__ == "__main__":
  main()