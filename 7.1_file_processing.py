"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# Problems found in names.txt:
# 1. Names have inconsistent capitalisation.
# 2. Some names have extra spaces at the beginning.
# 3. There is a blank line in the file.
# 4. First and last names do not follow consistent formatting.
#
# 1. In:
#    Names stored in names.txt.
#
# 2. Process:
#    - Read the original file.
#    - Remove extra spaces.
#    - Remove blank lines.
#    - Correct capitalisation.
#    - Sort names alphabetically by last name.
#
# 3. Out:
#    A new file called cleaned_names.txt.
#
# 4. How I decide which word is the last name:
#    The last word in each line is treated as the last name.
#    The names are sorted alphabetically using that word.

# Open and read the original file
with open("names.txt", "r") as file:
    names = file.readlines()


# Clean the names
cleaned_names = []

for name in names:
    name = name.strip()

    # Skip empty lines
    if name != "":
        # Correct capitalisation
        name = name.title()
        cleaned_names.append(name)


# Sort names by last name
cleaned_names.sort(key=lambda name: name.split()[-1])


# Save the cleaned names in a new file
with open("cleaned_names.txt", "w") as file:
    for name in cleaned_names:
        file.write(name + "\n")


# Display the result
print("Cleaned and sorted names:")

for name in cleaned_names:
    print(name)

print("\nNames successfully saved to cleaned_names.txt!")

