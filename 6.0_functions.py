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

#1. In: A list of monthly budgets (numbers).
#2. Process: Calculate the total and average monthly budget.
#3. Out: The total and average budget.
#4. Function name: calculate_budget_summary.
   #Return is used instead of print because it allows the
   #result to be reused in other parts of the program.

monthly_budgets = [200, 450, 600, 300, 500, 250, 150, 350]


def calculate_budget_summary(budgets):
    if len(budgets) == 0:
        return 0, 0

    total = sum(budgets)
    average = total / len(budgets)

    return total, average


# Calling the function three times with different inputs
result1 = calculate_budget_summary(monthly_budgets)
result2 = calculate_budget_summary([100, 200, 300])
result3 = calculate_budget_summary([500, 700, 900])

print("Monthly budgets:", result1)
print("Second budget list:", result2)
print("Third budget list:", result3)


# Checking the function with an empty list
empty_result = calculate_budget_summary([])

print("Empty list:", empty_result)

# An empty list returns (0, 0), which is acceptable
# because there are no budgets to calculate.