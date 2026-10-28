"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

## 1. In: The eight marketing channels from exercise 4.0.
# 2. Process: Make reordered copies using slicing, sorted(), and list methods.
# 3. Out: Four different orders, then the unchanged original list.
# 4. My four orders are: original order, reversed order, alphabetical order,
#    and reverse alphabetical order. None modifies the original list.
#    Slicing and sorted() create new lists. reverse() and sort() change a list
#    in place, so they are only used on copies, never on the original.

# Your code below
marketing_channels = [
    "Email", "Social media", "Search ads", "Influencers",
    "Events", "SEO", "Print ads", "Affiliate marketing"
]

original_snapshot = marketing_channels.copy()

original_order = marketing_channels.copy()
reversed_order = marketing_channels.copy()
reversed_order.reverse()
alphabetical_order = sorted(marketing_channels)
reverse_alphabetical_order = marketing_channels.copy()
reverse_alphabetical_order.sort(reverse=True)

print("1. Original order:", original_order)
print("2. Reversed order:", reversed_order)
print("3. Alphabetical order:", alphabetical_order)
print("4. Reverse alphabetical order:", reverse_alphabetical_order)

assert marketing_channels == original_snapshot, "The original list was changed!"
# The final line displays the original list so it can be compared with 4.0.
print("Original list (unchanged):", marketing_channels)