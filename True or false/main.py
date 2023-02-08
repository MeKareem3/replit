import time

score = 0
name = input("Welcome, What is your name? ")
print("Hello",(name))
print("When answering questions, type 1 for yes, 2 for no ")
time.sleep(2)
using12 = input("Lets test it, are you short? ")
print("Okay, Lets Get Started")
time.sleep(1)

q1 = int(input("Are bananas fruits? "))
if q1 == 2:
  score += 1
  print("Correct, good job")
else:
  print("You got it wrong, estúpido")


q3 = int(input("Are peanuts nuts? "))
if q3 == 2:
  score += 1
  print("Correct, good job - they are actually legumes (like lentils and peas).")
else:
  print("You got it wrong, estúpido - they are actually legumes (like lentils and peas).")

q4 = int(input("Are Mirrors green? "))
if q4 == 1:
  score += 1
  print("Correct, good job")
else:
  print("You got it wrong, estúpido")

q5 = int(input("Are you tall? "))
if q5 == 2:
  score += 1
  print("Correct, good job")
else:
  print("You got it wrong, estúpido")
  
q6 = int(input("Is Percy Jackson Canadian? "))
if q6 == 2:
  score += 1
  print("Correct, good job")
else:
  print("You got it wrong, estúpido")

q7 = int(input("Is polyester hydrophobic? "))
if q7 == 1:
  score += 1
  print("Correct, good job")
else:
  print("You got it wrong, estúpido")

print("You're score was:",score,"/6")