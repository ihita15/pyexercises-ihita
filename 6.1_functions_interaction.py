"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
#    A list of monthly budgets.
#
# 2. Process, function by function:
#    - get_total() calculates the total budget.
#    - get_average() calculates the average budget.
#    - get_highest() finds the highest monthly budget.
#    - budget_summary() combines the three functions.
#
# 3. Out:
#    Total, average and highest monthly budget.
#
# 4. The question my fourth function answers:
#    What is the overall summary of my monthly budgets?
#    Splitting the work into three functions makes each
#    calculation easier to test and check.

monthly_budgets = [200, 450, 600, 300, 500, 250, 150, 350]


# Function 1: Calculate total budget
def get_total(budgets):
    return sum(budgets)


# Function 2: Calculate average budget
def get_average(budgets):
    if len(budgets) == 0:
        return 0
    return sum(budgets) / len(budgets)


# Function 3: Find highest monthly budget
def get_highest(budgets):
    if len(budgets) == 0:
        return 0
    return max(budgets)


# Testing each function separately

# Test 1: Input [100, 200, 300], expected output: 600
print("Test total:", get_total([100, 200, 300]))

# Test 2: Input [100, 200, 300], expected output: 200
print("Test average:", get_average([100, 200, 300]))

# Test 3: Input [100, 200, 300], expected output: 300
print("Test highest:", get_highest([100, 200, 300]))


# Function 4: Combine the three functions
def budget_summary(budgets):
    total = get_total(budgets)
    average = get_average(budgets)
    highest = get_highest(budgets)

    return total, average, highest


# Display results using the monthly_budgets list
result = budget_summary(monthly_budgets)

print("\nMonthly Budget Summary")
print("Total budget:", result[0])
print("Average budget:", result[1])
print("Highest monthly budget:", result[2])
