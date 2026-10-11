# Marlon Nurse Assignment 4 Submission 
# DATA 602 - Advanced Programming Techniques


# Q1 - BankAccount Class


class BankAccount:

    def __init__(self, bankname, firstname, lastname, balance=0):
        self.bankname = bankname
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    # Add money to the account
    def deposit(self, amount):
        self.balance += amount
        print("Deposited: $", amount)

    # Withdraw money only if enough money is available
    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrew: $", amount)
        else:
            print("Withdrawal denied. Insufficient funds.")

    # Display the account information
    def __str__(self):
        return (
            "Bank: " + self.bankname +
            "\nOwner: " + self.firstname + " " + self.lastname +
            "\nBalance: $" + format(self.balance, ".2f")
        )


# Test the BankAccount class
account1 = BankAccount("Chase Bank", "Marlon", "Nurse")

print("\nQ1 - BANK ACCOUNT")
print(account1)

# Make a series of deposits and withdrawals
account1.deposit(500)
print(account1)

account1.deposit(250)
print(account1)

account1.withdrawal(200)
print(account1)

account1.withdrawal(100)
print(account1)

# Test a withdrawal that exceeds the balance
account1.withdrawal(1000)
print(account1)



# Q2 - Box Class


class Box:

    # Constructor
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Print a box made of asterisks
    def render(self):
        for row in range(self.width):
            print("*" * self.length)

    # Switch the length and width
    def invert(self):
        temp = self.length
        self.length = self.width
        self.width = temp

    # Return the area
    def get_area(self):
        return self.length * self.width

    # Return the perimeter
    def get_perimeter(self):
        return 2 * (self.length + self.width)

    # Double the dimensions of the box
    def double(self):
        self.length = self.length * 2
        self.width = self.width * 2
        return self

    # Compare two boxes
    def __eq__(self, other):
        return (
            self.length == other.length
            and self.width == other.width
        )

    # Print the dimensions
    def print_dim(self):
        print("Length:", self.length, "Width:", self.width)

    # Return dimensions as a tuple
    def get_dim(self):
        return (self.length, self.width)

    # Add another box's dimensions to this box
    def combine(self, other):
        self.length = self.length + other.length
        self.width = self.width + other.width

    # Return the diagonal length of the box
    def get_hypot(self):
        return (self.length ** 2 + self.width ** 2) ** 0.5



# Box Testing


print("\nQ2 - BOX CLASS")

# Instantiate three boxes
box1 = Box(5, 10)
box2 = Box(3, 4)
box3 = Box(5, 10)


# Print dimensions for all three boxes
print("\nOriginal box dimensions:")

print("Box 1:")
box1.print_dim()

print("Box 2:")
box2.print_dim()

print("Box 3:")
box3.print_dim()


# Compare box1 and box2
print("\nIs box1 equal to box2?")
print(box1 == box2)


# Compare box1 and box3
print("\nIs box1 equal to box3?")
print(box1 == box3)


# Demonstrate area and perimeter
print("\nBox 1 area:")
print(box1.get_area())

print("Box 1 perimeter:")
print(box1.get_perimeter())


# Demonstrate get_dim()
print("\nBox 1 dimensions as a tuple:")
print(box1.get_dim())


# Demonstrate get_hypot()
print("\nBox 1 diagonal:")
print(box1.get_hypot())


# Demonstrate render()
print("\nRendering box2:")
box2.render()


# Demonstrate invert()
print("\nBox 2 before invert:")
box2.print_dim()

box2.invert()

print("Box 2 after invert:")
box2.print_dim()

# Invert it again so it returns to its original 3 x 4 dimensions
box2.invert()


# Combine box3 into box1
print("\nCombining box3 into box1:")
box1.combine(box3)
box1.print_dim()


# Double the size of box2
print("\nDoubling box2:")
box2.double()
box2.print_dim()


# Combine box2 into box1
print("\nCombining box2 into box1:")
box1.combine(box2)
box1.print_dim()
