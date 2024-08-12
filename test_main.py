#!/usr/bin/env python3
# GitHub 06.2: Returning a Rocket Launch

import main as m, random

# Global Variable for input() of user values
value_input = []

# Global Variable for output of Actual Result of the Program
value_actual = []

def mock_input(prompt):
    "Mock the Input Process"
    global value_input, value_actual
    value_actual.append(prompt)
    return str(value_input.pop(0))

def run_main_program():
    "Run the main() program and capture the results"
    global value_input, value_actual

    # Overwrite the input() function
    m.input = mock_input

    # Overwrite the print() function with 1 argument in the print()
    m.print = lambda r : value_actual.extend([r])

    # Execute the main() function from the code
    m.main()

    return value_actual


def test_case1():
    "Case 1: Tests the T-Minus Messages (4pt)"

    assert m.countdown(-60) == "T-60 Seconds"
    assert m.countdown(-30) == "T-30 Seconds"
    assert m.countdown(-15) == "T-15 Seconds"

def test_case2():
    "Case 2: Test the Seconds where None is returned (4pt)"

    # Between -80 and -61 Seconds
    for x in range(-80,-60):
        assert m.countdown(x) == None

    # Between -59 and -31 Seconds
    for x in range(-59,-30):
        assert m.countdown(x) == None

    # Between -29 and -16 Seconds
    for x in range(-29,-15):
        assert m.countdown(x) == None

    # Between -14 and -11 Seconds
    for x in range(-14,-10):
        assert m.countdown(x) == None

def test_case3():
    "Case 3: Tests the last 10 Seconds of the Count (4pt)"

    for x in range(-10,0):
        if x != -4:
            assert m.countdown(x) == str(x*-1)
        else:
            assert m.countdown(x) == "Four stage engine start."

def test_case4():
    "Case 4: Tests count at ignition (4pt)"

    assert m.countdown(0) == "0\nBooster Ignition\nand lift off of Artemis I."    

def test_case5():
    "Case 5: Test Last Message (4pt)"

    assert m.countdown(2) == "We rise together to the moon and beyond!"

def test_case6():
    "Case 6: Test the Seconds where None is returned After Launch (4pt)"

    assert m.countdown(1) == None
    for x in range(3,10):
        assert m.countdown(x) == None

def test_case7():
    "Case 7: Test for Input with Random Seconds between 10-60 (8pt)"

    global value_input, value_actual
    value_possible = [
        "T-60 Seconds","T-30 Seconds", "T-15 Seconds",
        "10","9","8","7","6","5","Four stage engine start.","3","2","1",
        "0\nBooster Ignition\nand lift off of Artemis I.",
        "We rise together to the moon and beyond!"
    ]

    # Iterate through random second values four times
    for x in range(4):
        value_input = [random.randint(10,81)]
        value_actual = []
        value_expected = ["Enter Seconds to Launch: "]
        if value_input[0] >= 60:
            value_expected.extend(value_possible)
        elif value_input[0] >= 30:
            value_expected.extend(value_possible[1:])
        elif value_input[0] >= 15:
            value_expected.extend(value_possible[2:])
        else:
            value_expected.extend(value_possible[3:])

        # Save Result of Main Program Execution
        value_actual = run_main_program()

        # Test the Actual result equal to the Expected result
        assert value_actual == value_expected