age= int(input("How old are you ")) #if statement
if age >=18:
    print("You can vote")
    print("Vote check done!")

temp=int(input("What's the temperature outside fine sir? "))#If else
if temp < 10:
    print("It's cold, go wear a jacket.")
else: 
    print("Pfft. You don't need a jacket.")

day = input("What day of the week is it kind sir? ")

if day == "monday":
    print("Ugh, it's Monday.")
elif day == "friday":
    print("Yay, it's almost the weekend")
elif day == "saturday":
    print("It's the weekend!")
elif day == "sunday":
    print("It's the weekend.")
else:
    print("Who cares. Its just a weekday...")

score = int(input("What is your score out of 100? "))
if score >= 60:
    print("You passed... Barely... ")
    if score >=90:
        print("Nice one, You passed with flying colors!")
else:
    print("You FAILED.")
print("Grading is complete.")
