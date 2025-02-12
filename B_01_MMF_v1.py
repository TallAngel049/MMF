# Functions fo here
def make_statement(statement, decoration):
    """Emphasises headings by adding
    decoration at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_answers=('yes', 'no'),
                 num_letters=1):
    """Check that users enter the full word
    or the 'n' letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # Check if the response is the entire work
            if response == item:
                return item

            # Check if it's the 'n' letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")


def instructions():
    make_statement("Instructions", "ℹ️")

    print('''
    
For each ticket holder enter ...
- Their name
- Their age
- The payment method (cash / credit)

The program will record the ticket sale and calculate the 
ticket cost (and profit).

Once you have either sold all of the tickets or entered the
exit coe ('xxx'), the program will display the ticket 
sales information and write data to text file.

It will also choose on lucky ticket holder who wins the 
draw (their ticket is free).

    ''')


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry. this can't be blank. Please try again.\n")


def int_check(question, ):
    """Checks users enter an integer"""

    error = f"Oops - please enter an integer"

    while True:

        try:
            # return the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


# Main Routine goes here


# Initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0


# Initialise variables / non-default options for string checker
payment_ans = ('cash', 'credit')

make_statement("Mini-Movie Fundraiser program", "🍿")

print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()

while tickets_sold < MAX_TICKETS:
    print()
    name = not_blank("Name: ")

    # if name is exit code, break out of loop
    if name == "xxx":
        break

    # ask for their age and check it's between 12 and 120
    age = int_check("Age: ")

    # Output error messages / success message
    if age < 12:
        print(f"Sorry you are too young for this movie")
        continue
    elif age > 120:
        print(f"{age}?? That looks like a typo (too old) ")
        continue
    else:
        pass

    # ask user for payment method ( cash / credit / ca / cr )
    pay_method = string_check("Payment method: ", payment_ans, 2)
    print(f"{name} has bought a ticket ( {pay_method} )")

    tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    print(f"You have sold all the tickets (ie; {MAX_TICKETS} tickets")
else:
    print(f"You have sold {tickets_sold} / {MAX_TICKETS} tickets. ")

