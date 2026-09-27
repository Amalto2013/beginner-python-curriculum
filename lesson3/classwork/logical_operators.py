age = int(input("What's your age "))
has_ticket = input("Do you have a ticket?  (yes/no) ")
if age >= 13 and has_ticket == "yes":
    print("You can watch the movie! Have fun!")
else:
    print("Leave!")

has_pass= input("Do you have a buss pass? (yes/no) ")
has_coins= input("Are you able to pay the fare? (yes/no) ")
if has_pass == "yes" or has_coins == "yes":
 print("Go on and board kiddo!")
else:
   print("What are you here for? Scram!")

Hw_done = input("Have you done your homework? (yes/no) ")
if Hw_done == "yes":
   print("Good.")
else:
   print("Go do your homework!")