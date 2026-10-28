"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The eight marketing channels and their monthly budgets from exercise 4.0.
# 2. Process: Use a for loop to visit each channel, find its position, and
#    calculate its percentage share of the total monthly budget.
# 3. Out: Exactly eight lines, each showing position, channel, budget and share.
# 4. I compute each channel's percentage of the total budget so the reader can
#    compare how much of the marketing budget is spent on each channel.


# Your code below
marketing_channels = [
    "Email", "Social media", "Search ads", "Influencers",
    "Events", "SEO", "Print ads", "Affiliate marketing"
]
monthly_budgets = [200, 450, 600, 300, 500, 250, 150, 350]

total_budget = sum(monthly_budgets)

for position, (channel, budget) in enumerate(zip(marketing_channels, monthly_budgets), start=1):
    percentage = budget / total_budget * 100
    print(f"{position}. {channel}: EUR {budget} ({percentage:.2f}% of total)")
