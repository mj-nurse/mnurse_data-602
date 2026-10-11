# Marlon Nurse Assignment 3 Submission
# DATA 602 - Advanced Programming Techniques



# Q1
# Ask the user to enter breakfast, lunch, or dinner.
# Recommend a meal using if/elif/else statements.


meal = input("Enter breakfast, lunch, or dinner: ").lower()

if meal == "breakfast":
    print("How about a bacon and egg sandwhich?")
elif meal == "lunch":
    print("How about a chicken ceasar salad?")
elif meal == "dinner":
    print("How about some ground beef and rice?")
else:
    print("Please enter breakfast, lunch, or dinner.")


# Q2
# Calculate a student employee's gross pay.
# Any hours over 20 are paid at 1.5 times the normal rate.


hours = float(input("Enter the number of hours worked: "))
pay_rate = float(input("Enter the hourly rate of pay: $"))

if hours > 20:
    regular_pay = 20 * pay_rate
    overtime_hours = hours - 20
    overtime_pay = overtime_hours * pay_rate * 1.5
    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = hours * pay_rate

print(f"Gross pay: ${gross_pay:.2f}")


# Q3
# Create a function named times_ten.
# The function accepts an argument and displays that
# argument multiplied by 10.


def times_ten(number):
    result = number * 10
    print(result)


number = float(input("Enter a number to multiply by 10: "))
times_ten(number)



# Q4
# Find the errors, debug the program, and show the output.


def main():
    calories1 = float(input("How many calories are in the first food? "))
    calories2 = float(input("How many calories are in the second food? "))
    showCalories(calories1, calories2)


def showCalories(calories1, calories2):
    total_calories = calories1 + calories2
    print("The total calories you ate today is {:.2f}".format(total_calories))


main()



# Q5
# Use a loop to calculate:
# 1/30 + 2/29 + 3/28 + ... + 30/1


total = 0

for numerator in range(1, 31):
    denominator = 31 - numerator
    total += numerator / denominator

print("The total of the series is:", total)


# Q6
# Create a function that calculates the area of a triangle.
# Area = 1/2 * base * height


def triangle_area(base, height):
    area = 0.5 * base * height
    print(area)


triangle_area(5, 4)
