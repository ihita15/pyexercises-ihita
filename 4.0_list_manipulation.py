"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Eight example monthly marketing-channel budgets, in euros.
# 2. Process: Display the budgets, select one, sort them, and calculate their total.
# 3. Out: The original list, one budget, the sorted list, and the total budget.
# 4. My list is about example monthly marketing budgets for eight channels.
#    I computed the total to show how much all channels cost together.


# Your code below
marketing_channels = [
    "Email", "Social media", "Search ads", "Influencers",
    "Events", "SEO", "Print ads", "Affiliate marketing"
]
monthly_budgets = [200, 450, 600, 300, 500, 250, 150, 350]

print("Marketing channels:", marketing_channels)
print("Monthly budgets (EUR):", monthly_budgets)
print("Chosen channel:", marketing_channels[2])
print("Its budget (EUR):", monthly_budgets[2])
print("Budgets sorted (EUR):", sorted(monthly_budgets))
print("Total monthly budget (EUR):", sum(monthly_budgets))
# Check by hand: the first three budgets are 200 + 450 + 600 = 1250.
# The program should give the same result for these three values.
print("First three budgets total (EUR):", sum(monthly_budgets[:3]))
