TICKET_PRICE = 10

tickets_remaining = 100

# Run this code continuously until we run out of tickets
while tickets_remaining > 0:
    # Output how many tickets are remaining using the tickets_remaining variable
    print("\nThere are currently {} tickets remaining.".format(tickets_remaining))

    # Gather the user's name and assign it to a new variable
    name = input("What is your name?   ")

    # Prompt the user by name and ask how many tickets they would like
    ticket_quantity = int(input("Hey {}! How many tickets would you like?    ".format(name)))

    # Calculate the price (num of tickets * price) and assign it to a variable
    amount_due = ticket_quantity * TICKET_PRICE

    # Output the price to the screen
    print("\nAlright {}, your total is going to be ${}!".format(name, amount_due))

    # Prompt user if they want to proceed. Y/N?
    to_proceed = input("Is this amount ok?  (Y/N)    ").lower()

    # If they want to proceed
    if to_proceed == "y":
        # Print out to the screen "SOLD!" to confirm purchase
        print("SOLD!")
        # and then decrement the tickets remaining by the num of tix purchased
        tickets_remaining -= ticket_quantity
    # Else ...
    else:
        # Thank them by name
        print("Thanks anyways {}.".format(name))

# Notify user that the tickets are sold out
print("We're out of tickets!")