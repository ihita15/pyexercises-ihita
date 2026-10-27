"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: using float input option to add numbers
# 2. Process: performed basic arethmatic functions on the two numbers
# 3. Out: got the results of two numbers
# 4. What happens when the second number is zero, and why: division cannot be performed 


# Your code below
number1 = float(input("enter the first number:")) 
number2 = float(input("enter the second number:"))
print(number1, number2)
# sum of the two number 
sum = number1 + number2
print("the sum of two numbers is:", sum)

# subtraction
diff = number2 - number1
print("the differnce between two numbers is:", diff)

# multiplication 
product = number1 * number2 
print("the product of the two numbers is:", product)

#division
if number2 == 0:
    print("the division cannot be performed")
else:
    print("division:", number1/number2)
