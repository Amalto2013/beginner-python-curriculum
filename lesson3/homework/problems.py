# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."
ts= int(input("Enter your first score on the test.: "))
ts2= int(input("Enter your second score.: "))
if ts >=50 and ts2 >=50:
    print("Nice one, you passed on both!")
else:
    print("You failed at least one.")



# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."
l= input("Did you like bring lunch? (yes/no): ")
w= input("what about water, did you bring it? (yes/no): ")
if l == "yes" and w == "yes":
    print("Fantastic, lets eat!")
elif l == "yes" and w == "no":
    print("You have lunch yet no water, Don't worry, I'll share.")
elif l == "no" and w == "yes":
    print("How did you forget your lunch and not your water? It's alright, I'll share my lunch.")
else:
 print("You forgot your lunch and water. What a pity. I'll share though.")






# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."

n = int(input("Enter a number: "))
if n < 1 or n > 10:
    print("Not in the range.")
else:
    print("Number in range.")



# Problem 4
# Ask the user for a test score (0-100).
# Print the grade based on score:
#   90 and above: "A"
#   80 to 89: "B"
#   70 to 79: "C"
#   60 to 69: "D"
#   below 60: "F"
ts = int(input("Heya kiddo! Let me see your recent test score!: "))
if ts >= 90:
    print("Nice one! You passed with flying colors and got an A!")
elif ts >= 80:
    print("Nice one! You passed with a B!")
elif ts >= 70:
    print("Alright, You passed with a C.")
elif ts >= 60:
    print("You barely passed with a D.")
else:
    print("You failed. With an F.")



# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."

n1 = int(input("Hey user, Give me 2 numbers! Enter the first one: "))
n2 = int(input("Alright, now the second one: "))
if n1 % 5 == 0 and n2 % 2 != 0:
    print("Interesting pair...")
else:
    print("Nothing special with this pair...")