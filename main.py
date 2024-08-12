#!/usr/bin/env python3
# GitHub 06.2: Returning a Rocket Launch

# Task 1. Modify the function countdown()
def countdown(secs):

  # Initialize count down message
  msg = None

  # Return the count down message
  return msg


def main():
  # Task 2. Manually test by taking input for seconds variable
  seconds = int(input("Enter Seconds to Launch: "))
  
  # Tip, if positive number entered convert to a negative for start of count
  if seconds > 0:
    seconds = seconds * -1

  # Task 3. Modify Loop Condition and Call Count Down Function
  while False:
    print()


# DO NOT MODIFY BELOW
if __name__ == "__main__":
  main()