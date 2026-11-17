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

 1. In:
# A list of numbers.

# 2. Process, function by function:
# Function 1 calculates the sum.
# Function 2 finds the maximum number.
# Function 3 finds the minimum number.
# Function 4 combines the three functions.

# 3. Out:
# The total, maximum and minimum numbers.

# 4. The question my fourth function answers:
# What are the total, highest and lowest numbers?
# Splitting the code makes each function easier to test.


# Function 1: Calculate the sum

def calculate_sum(numbers):
    return sum(numbers)


# Function 2: Find the maximum
def find_maximum(numbers):
    return max(numbers)


# Function 3: Find the minimum
def find_minimum(numbers):
    return min(numbers)


# Function 4: Combine all three functions
def analyse_list(numbers):
    if len(numbers) == 0:
        return 0, None, None

    total = calculate_sum(numbers)
    maximum = find_maximum(numbers)
    minimum = find_minimum(numbers)

    return total, maximum, minimum


# Test each function separately

# Test 1: Input [10, 20, 30], expected output 60
print(calculate_sum([10, 20, 30]))

# Test 2: Input [10, 20, 30], expected output 30
print(find_maximum([10, 20, 30]))

# Test 3: Input [10, 20, 30], expected output 10
print(find_minimum([10, 20, 30]))


# Test the fourth function
numbers = [10, 20, 30, 40, 50]

print("Analysis:", analyse_list(numbers))

# Test an empty list
print("Empty list:", analyse_list([]))