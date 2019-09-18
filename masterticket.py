TICKET_PRICE = 10

tickets_remaining = 100

# Output how many tickets are remaining using the tickets_remaining variable
print("There are currently {} tickets remaining.".format(tickets_remaining))

# Gather the user's name and assign it to a new variable
name = input("What is your name?   ")

# Prompt the user by name and ask how many tickets they would like
ticket_quantity = int(input("Hey {}! How many tickets would you like?    ".format(name)))

# Calculate the price (num of tickets * price) and assign it to a variable
amount_due = ticket_quantity * TICKET_PRICE

# Output the price to the screen
print("\nAlright {}, your total is going to be ${}!".format(name, amount_due))