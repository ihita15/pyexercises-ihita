"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In:
#    First name, last name, email and student number.
#
# 2. Process:
#    The program asks the user for their details
#    and saves them in a CSV file.
#
# 3. Out:
#    File name: 7.0_student_data.csv
#    Columns: first_name, last_name, email, student_number
#
# 4. Why these columns:
#    These columns help organise student information.
#    With 200 entries, I could use the file to manage
#    and search for student records.

import csv
import os

filename = "7.0_student_data.csv"

# Collect student information
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
email = input("Enter your email: ")
student_number = input("Enter your student number: ")

# Check if the file exists
file_exists = os.path.isfile(filename)

# Open CSV file in append mode
with open(filename, "a", newline="") as file:
    writer = csv.writer(file, delimiter=";")

    # Add headers only if the file is empty
    if not file_exists or os.path.getsize(filename) == 0:
        writer.writerow([
            "first_name",
            "last_name",
            "email",
            "student_number"
        ])

    # Save student information
    writer.writerow([
        first_name,
        last_name,
        email,
        student_number
    ])

print("Student information saved successfully!")