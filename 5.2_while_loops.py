"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user's answer to whether a marketing campaign is approved.
# 2. Process: Ask repeatedly using a while loop, normalize spaces and capitals,
#    and stop when the user answers yes or the attempt limit is reached.
# 3. Out: A summary showing the number of attempts and whether approval was given.
# 4. My stop condition, my attempt limit, my summary:
#    Stop when the answer is 'yes' (including 'Yes' or ' yes ') or after 3 tries.
#    The summary shows attempts used and the final approval status.
#    If all 3 attempts are used without 'yes', report that approval was not given.


# Your code below
max_attempts = 3
attempts = 0
approved = False

while attempts < max_attempts and not approved:
    answer = input("Is the marketing campaign approved? (yes/no): ")
    attempts += 1
    if answer.strip().lower() == "yes":
        approved = True

print(f"Attempts used: {attempts}")
if approved:
    print("Summary: Campaign approved.")
else:
    print("Summary: Campaign not approved; attempt limit reached.")