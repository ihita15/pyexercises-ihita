"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Information about a sample marketing campaign.
# 2. Process: Store the campaign in a dictionary, read a field, update a field,
#    remove a field, and loop through the remaining key/value pairs.
# 3. Out: The selected value, updated information, missing-field result,
#    and all remaining campaign fields with their values.
# 4. My object is a marketing campaign. Its fields are name (identifies it),
#    channel (where ads run), budget_eur (spending plan), audience (target group),
#    status (whether it is active), and owner (person responsible).


# Your code below
campaign = {
    "name": "Autumn Awareness",
    "channel": "Social media",
    "budget_eur": 450,
    "audience": "Young adults",
    "status": "Planned",
    "owner": "Marketing team",
}

print("Campaign name:", campaign["name"])

campaign["status"] = "Active"
print("Updated status:", campaign["status"])

removed_owner = campaign.pop("owner")
print("Removed owner:", removed_owner)

# Looking up a missing key using campaign["deadline"] would raise KeyError.
# .get() avoids the error and returns the default message instead.
print("Missing deadline:", campaign.get("deadline", "Not available"))

print("Remaining campaign details:")
for field, value in campaign.items():
    print(f"{field}: {value}")
