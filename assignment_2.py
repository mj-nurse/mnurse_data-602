# Marlon Nurse - Assignment 2 Submission
# DATA 602 - Advanced Programming Techniques



# Q1
# What will the following code display?
# Debug the code so that it returns the entire list.

numbers = [1, 2, 3, 4, 5]

# The original slice returns an empty list.
print(numbers[1:-5])

# Answer: Using [:] returns the entire list.
print(numbers[:])



# Q2
# Ask the user to enter a store's sales for each day
# of the week. Store the amounts in a list and use a
# loop to calculate the total sales.


sales = []

for day in range(1, 8):
    amount = float(input(f"Enter sales for day {day}: $"))
    sales.append(amount)

total_sales = 0

for amount in sales:
    total_sales += amount

print(f"Total sales for the week: ${total_sales:.2f}")



# Q3
# Create a list of at least five places I would like
# to travel. Print the original list, sort it, and then
# sort it in reverse order.


places = [
    "Houston",
    "Japan",
    "Paris",
    "Toronto",
    "Australia"
]

print("\nOriginal list:")
print(places)

places.sort()

print("\nAlphabetical order:")
print(places)

places.sort(reverse=True)

print("\nReverse alphabetical order:")
print(places)



# Q4
# Create dictionaries containing course numbers,
# room numbers, instructor names, and meeting times.
# Ask the user for a course number and display its
# information.


rooms = {
    "DATA602": "Room 115",
    "DATA606": "Room 227",
    "DATA607": "Room 903"
}

instructors = {
    "DATA602": "Professor Schettini",
    "DATA606": "Professor Lui",
    "DATA607": "Professor Catlin"
}

meeting_times = {
    "DATA602": "5:00 PM",
    "DATA606": "8:00 PM",
    "DATA607": "6:15 PM"
}

course = input("\nEnter a course number: ").upper()

if course in rooms:
    print("Room:", rooms[course])
    print("Instructor:", instructors[course])
    print("Meeting Time:", meeting_times[course])
else:
    print("Course not found.")


# Q5
# Create a dictionary that stores names and email
# addresses as key-value pairs.
#
# Allow the user to:
# 1. Look up an email address
# 2. Add a new name and email
# 3. Change an existing email
# 4. Delete a name and email

emails = {
    "John": "john@email.com",
    "Mary": "mary@email.com",
    "David": "david@email.com"
}

choice = ""

while choice != "5":

    print("\nEmail Address Menu")
    print("1. Look up an email address")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete an existing name and email address")
    print("5. Quit")

    choice = input("Enter your choice: ")

    # Look up an email address
    if choice == "1":
        name = input("Enter the person's name: ")

        if name in emails:
            print(name, ":", emails[name])
        else:
            print("Name not found.")

    # Add a new name and email address
    elif choice == "2":
        name = input("Enter the person's name: ")

        if name not in emails:
            email = input("Enter the email address: ")
            emails[name] = email
            print("Name and email address added.")
        else:
            print("That name already exists.")

    # Change an existing email address
    elif choice == "3":
        name = input("Enter the person's name: ")

        if name in emails:
            email = input("Enter the new email address: ")
            emails[name] = email
            print("Email address updated.")
        else:
            print("Name not found.")

    # Delete a name and email address
    elif choice == "4":
        name = input("Enter the person's name: ")

        if name in emails:
            del emails[name]
            print("Name and email address deleted.")
        else:
            print("Name not found.")

    elif choice == "5":
        print("Program ended.")

    else:
        print("Invalid choice.")
