# Assignment:
# Write a program that generates and prints out 5 random integers between 50 and 100.
# Write a function that will return the average of these numbers.
# Write another function that will return a letter grade for a given numeric grade 
# (Less than 60 is an F, 60 to less than 70 is a D, 70 to less than 80 is a C, 80 to less than 90 is a B, 90 or more is an A.)
# Print out each of the 5 integers, their average, and all 6 corresponding letter grades.
# Use comments wherever your code isn't obvious, and remember to start with a comment with your name, date, and program title.

# Import Library (random)
import random

# Generate the grades (5 random numbers from 50-100)
random1 = random.randint(50,100)
random2 = random.randint(50,100)
random3 = random.randint(50,100)
random4 = random.randint(50,100)
random5 = random.randint(50,100)

# Give the first grade a grade number (Ex: 100 = A)
if random1 == 60:
  grade1 = "D"
if random1 == 70:
  grade1 = "C"
if random1 == 80:
  grade1 = "B"
if random1 == 90:
  grade1 = "A"
if random1 == 100:
  grade1 = "A"
if random1 < 60:
  grade1 = "F"
if random1 < 70:
  if random1 > 60:
    grade1 = "D"
if random1 < 80:
  if random1 > 70:
    grade1 = "C"
if random1 < 90:
  if random1 > 80:
    grade1 = "B"
if random1 < 100:
  if random1 > 90:
    grade1 = "A"
print(f'Grade 1: {random1} {grade1}')

# Give the second grade a grade number (Ex: 100 = A)
if random2 == 60:
  grade2 = "D"
if random2 == 70:
  grade2 = "C"
if random2 == 80:
  grade2 = "B"
if random2 == 90:
  grade2 = "A"
if random2 == 100:
  grade2 = "A"
if random2 < 60:
  grade2 = "F"
if random2 < 70:
  if random2 > 60:
    grade2 = "D"
if random2 < 80:
  if random2 > 70:
    grade2 = "C"
if random2 < 90:
  if random2 > 80:
    grade2 = "B"
if random2 < 100:
  if random2 > 90:
    grade2 = "A"
print(f'Grade 2: {random2} {grade2}')

# Give the third grade a grade number (Ex: 100 = A)
if random3 == 60:
  grade3 = "D"
if random3 == 70:
  grade3 = "C"
if random3 == 80:
  grade3 = "B"
if random3 == 90:
  grade3 = "A"
if random3 == 100:
  grade3 = "A"
if random3 < 60:
  grade3 = "F"
if random3 < 70:
  if random3 > 60:
    grade3 = "D"
if random3 < 80:
  if random3 > 70:
    grade3 = "C"
if random3 < 90:
  if random3 > 80:
    grade3 = "B"
if random3 < 100:
  if random3 > 90:
    grade3 = "A"
print(f'Grade 3: {random3} {grade3}')

# Give the fourth grade a grade number (Ex: 100 = A)
if random4 == 60:
  grade4 = "D"
if random4 == 70:
  grade4 = "C"
if random4 == 80:
  grade4 = "B"
if random4 == 90:
  grade4 = "A"
if random4 == 100:
  grade4 = "A"
if random4 < 60:
  grade4 = "F"
if random4 < 70:
  if random4 > 60:
    grade4 = "D"
if random4 < 80:
  if random4 > 70:
    grade4 = "C"
if random4 < 90:
  if random4 > 80:
    grade4 = "B"
if random4 < 100:
  if random4 > 90:
    grade4 = "A"
print(f'Grade 4: {random4} {grade4}')

# Give the fifth grade a grade number (Ex: 100 = A)
if random5 == 60:
  grade5 = "D"
if random5 == 70:
  grade5 = "C"
if random5 == 80:
  grade5 = "B"
if random5 == 90:
  grade5 = "A"
if random5 == 100:
  grade5 = "A"
if random5 < 60:
  grade5 = "F"
if random5 < 70:
  if random5 > 60:
    grade5 = "D"
if random5 < 80:
  if random5 > 70:
    grade5 = "C"
if random5 < 90:
  if random5 > 80:
    grade5 = "B"
if random5 < 100:
  if random5 > 90:
    grade5 = "A"
print(f'Grade 5: {random5} {grade5}')

# Calculate average
average = (random1+random2+random3+random4+random5)/5

# Give average a grade letter (Ex: 100 = A)
if average == 60:
  averageletter = "D"
if average == 70:
  averageletter = "C"
if average == 80:
  averageletter = "B"
if average == 90:
  averageletter = "A"
if average == 100:
  averageletter = "A"
if average < 60:
  averageletter = "F"
if average < 70:
  if average > 60:
    averageletter = "D"
if average < 80:
  if average > 70:
    averageletter = "C"
if average < 90:
  if average > 80:
    averageletter = "B"
if average < 100:
  if average > 90:
    averageletter = "A"
print(f'Grade 5: {random5} {grade5}')

# Print average grade & letter
print(f'Average Grade: {average} {averageletter}')

# Comment with name, date, and assignment name redacted



# About 90% of the way done I figured out I could have done

# if 60 < random < 70:
#    print(random)

# instead. Since I was almost done, I just stuck with the non-optimized code.
