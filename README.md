# GitHub 06.2: Returning a Rocket Launch

## Student Information

* Nhat Phi Hoang
* Spring/2026
* 37239

## Instructions

Create a program that will announce a rocket launch starting between T-Minus 5  seconds to T-Minus 80 seconds using only for loops or if statements allowed. A method will be used to determine the message that should be returned as part of the launch count down announcement. You will be recreating the approximate launch announcements using the a method.

This discussion is considered the **most challenging** of the semester as it is designed to hit all the major areas you need to be competent in before the midterm exam. Make sure you give yourself enough time to complete it.

### Major Tasks

1. Modify the countdown() method to make a decision on what to return based on the sample output.
1. Modify the `while` loop to use a conditional statement in `main()` to allow it to loop through a set of values to get the correct output.
1. Test to ensure the program passes the provided tasks found in the [TESTS.md](TESTS.md) file. 
1. Answer the questions below.
1. Commit your changes and verify the formatting of the README.md file is correct in GitHub.

#### Task 1. Function countdown() Requirements

* Function `countdown()` must be defined with 1 required parameter
* Loops are not allowed inside the function
* You must return the appropriate response or `None` based on your decision
* Only 1 `return` statement is allowed inside the method
* No `print()` statements are allowed inside of the function
* You must use `if elif else` statements to decide which value should be returned
  * The count down will return a series of T Minus messages at T-Minus 15, T-Minus 30, and T-Minus 60 seconds.
  * The count down will not return an individual second except between T-Minus 10 to 1 seconds.
  * The count down will always display positive numbers for individual seconds, even if the number is negative value in the decision calculation.

#### Task 2. Function main() Requirements

* Only one `while` loop is allowed in the main program which is provided but needs modifications to the conditional statement. You must modify the provided `while False:` and cannot use `while True:`.
* A single `print()` statement is inside the main program.
* A single student written `if` statement is inside the main program, excluding the instructor provided `if` statement. You may not use `elif` or `else` inside the main program.
* Test the loop using `input()` anywhere between T-Minus 15 seconds before launch to T-Minus 80 seconds before launch.
* Do not modify the provided input prompt, it is correct.
* The loop should allow for a value to start at -80 seconds before launch and end 10 seconds after launch.

### Tips

* Start with reading the [test_main.py](test_main.py) file as it has tips on how the program will be tested and what the expectations will be.
* Practice incremental development and focus on **one** unit test function in the pytest at a time until you solve the unit tests.
* Utilize what you have learned about the `in` keyword and compound conditional statements to reduce the amount of lines of code needed.
* After solving the unit tests, update the `main()` program to solve the output for the manual testing.
* The while loop inside the `main()` function can be solved in 4-5 statement lines, think about what you need and what was returned. Anything more is overthinking the problem.
* Don't attempt to solve test case 7 in the unit test file until you have solved test cases 1 through 6.

Need help? Contact the [Math, Science, & Engineering Center](https://www.riohondo.edu/mathematics-and-sciences/math-science-center/) for tutoring assistance. Any form of sharing or uploading of this assignment on external websites is strictly prohibited.

### Watch a Real Rocket Launch

The URL below will take you to the the Artemis I Launch. It is queued up at 3 hours 16 minutes before the launch so you can hear what the announcer is saying. This will give you the idea of what a count down for a rocket launch sounds like. Note every launch count is slightly different, but also the same.

[Artemis I Launch to the Moon (Official NASA Broadcast) - Nov. 16, 2022](https://www.youtube.com/live/CMLD0Lp0JBg?feature=share&t=11760)

Note, when the announcer is saying T-Minus 30 seconds they mean they are negative thirty (-30) seconds to launch on the mission clock. Seconds in a launch become a positive number after the rocket has hit zero. So a rocket launch counts down, then counts up on the mission clock.

## Exercise Questions

Do not provide code for any of the questions. Delete the text that says *YOUR ANSWER HERE* and provide answers to each of the questions in normal written language answering each of the questions.

### Question 1

**What are the advantages of returning a value rather than printing it from the function?**

The advantages of returning a value is more flexible way of handling data compared to printing it. The program can then print, save, or use the returned value in condition.

### Question 2

**What do you think is the reason a single value evaluated by the countdown() function then returned rather than using a loop inside of the countdown() function?**

I think the reason the function returns a single value rather than looping is because it is designed to owrk on one input at a time. The main function contrains the loop so it has the power to decide the numbers of repeats of the function. This keeps the function simple and focused, while the main program handles over and over.
