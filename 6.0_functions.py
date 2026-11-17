"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

1. In:
# The function receives a list of numbers.

# 2. Process:
# It calculates the total and average of the numbers in the list.

# 3. Out:
# It returns the total and average.

# 4. My function name is calculate_total_and_average.
# Return is used instead of print because the returned result
# can be reused in other parts of the program.

# Your code below
def calculate_total_and_average(numbers):
    if len(numbers) == 0:
        return 0, 0

    total = sum(numbers)
    average = total / len(numbers)

    return total, average


# Calling the function three times with different inputs

result1 = calculate_total_and_average([10, 20, 30])
result2 = calculate_total_and_average([5, 15, 25, 35])
result3 = calculate_total_and_average([100, 200, 300])

print("First result:", result1)
print("Second result:", result2)
print("Third result:", result3)
#Checking with an empty list
empty_result = calculate_total_and_average([])

print("Empty list result:", empty_result)

# The function returns (0, 0) for an empty list.
# This is acceptable because there are no numbers to calculate.