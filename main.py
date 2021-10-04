# Assignment:
# Write a program that generates and prints out 5 random integers between 50 and 100.
# Write a function that will return the average of these numbers.
# Write another function that will return a letter grade for a given numeric grade 
# (Less than 60 is an F, 60 to less than 70 is a D, 70 to less than 80 is a C, 80 to less than 90 is a B, 90 or more is an A.)
# Print out each of the 5 integers, their average, and all 6 corresponding letter grades.
# Use comments wherever your code isn't obvious, and remember to start with a comment with your name, date, and program title.

# Was instructed to redo with optimized code. So here it is:

# Import libraries
import random

# Create empty list to fill later
gradelist = []

# Calculare grade letter function
def grade_letter(grade):
    if grade >= 90:
        return 'A'
    elif 89 > grade >= 80:
        return 'B'
    elif 79 > grade >= 70:
        return 'C'
    elif 69 > grade >= 60:
        return 'D'
    else:
        return 'F'


# Create grades and add them to empty list
for i in range(0, 5):
    randomgrade = random.randint(50, 100)
    gradelist.append(randomgrade)
    print(f'Grade: {randomgrade} {grade_letter(randomgrade)}')

# Get average of the grades
average = sum(gradelist) / len(gradelist)

# Print finished data
print(f'Grade Average: {average} {grade_letter(randomgrade)}')

# Comment with name, date, and assignment name redacted
