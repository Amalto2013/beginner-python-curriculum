import random

# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.
Os = ["Windows", "Mac OS", "Linux"]
print("Last Os:", Os[len(Os) - 1])
Os.reverse()
print("Os but reversed", Os)



# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.
SS = ["Math", "Science", "English", "History"]
print("Second subject:", SS[1])
SS.sort()
print("Sorted subjects:", SS)


# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then use a for loop to print each error code.
EC = [404, 500, 403, 401, 410]
print("Number of error codes:", len(EC))
for i in EC:
    print("Error code:", i)

# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
cpr=["Python", "JS"]
print("Random Programming Language:" , random.choice(cpr))



# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
password=["12345", "76890", "01234", "56789", "abcde", "fghij"]
len(password)
print("Mid Pass:", password[len(password) // 2])
p=password.pop(0)
print("Post password 1 removal:", p)

