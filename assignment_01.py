# Marlon Nurse Submission 
# Q1
# Fix all the syntax and logical errors in the given source code.
# Add comments to explain your reasoning.

# This program gets three test scores and displays their average.
# It congratulates the user if the average is a high score.
# The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95

# Get the three test scores.
# input() returns a string, so float() converts each score to a number.
test1 = float(input('Enter the score for test 1: '))
test2 = float(input('Enter the score for test 2: '))
test3 = float(input('Enter the score for test 3: '))

# Add all three test scores first, then divide by 3 to calculate the average.
average = (test1 + test2 + test3) / 3

# Print the average.
print('The average score is', average)

# HIGH_SCORE must use the same capitalization as when it was created.
# If the average is 95 or higher, congratulate the user.
if average >= HIGH_SCORE:
    print('Congratulations!')
    print('That is a great average!')


# Q2
# The area of a rectangle is the rectangle's length times its width.
# Ask for the length and width of two rectangles and print their areas.

# Get the measurements for rectangle 1.
length1 = float(input('Enter the length of rectangle 1: '))
width1 = float(input('Enter the width of rectangle 1: '))

# Calculate the area of rectangle 1.
area1 = length1 * width1

# Get the measurements for rectangle 2.
length2 = float(input('Enter the length of rectangle 2: '))
width2 = float(input('Enter the width of rectangle 2: '))

# Calculate the area of rectangle 2.
area2 = length2 * width2

# Print the area of both rectangles.
print('The area of rectangle 1 is', area1)
print('The area of rectangle 2 is', area2)


# Q3
# Ask the user to enter their first name and age.
# name will be stored as a string and age will be stored as an integer.

name = input('Enter your first name: ')
age = int(input('Enter your age: '))

# Print a birthday message using the name and age variables.
print('Happy birthday,', name + '!', 'You are', age, 'years old today!')
