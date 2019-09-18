TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100

def calculate_price(ticket_quantity):
    return (ticket_quantity * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining > 0:
    print("\nThere are currently {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name?   ")
    try:
        ticket_quantity = int(input("Hey {}! How many tickets would you like?    ".format(name)))
        if ticket_quantity > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("\nOops! We ran into an issue. {}. Try again...".format(err))
    else:
        amount_due = calculate_price(ticket_quantity * TICKET_PRICE)
        print("\nAlright {}, your total is going to be ${}!".format(name, amount_due))
        to_proceed = input("Is this amount ok?  (Y/N)    ").lower()

        if to_proceed == "y":
            print("SOLD!")
            tickets_remaining -= ticket_quantity
        else:
            print("Thanks anyways {}.".format(name))
print("We're out of tickets!")