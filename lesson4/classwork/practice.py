import random

# Problem 1
# Create a list of 4 car brands.
# Print the first and last.
# Then add another brand using append() and print the updated list.
car_brands = ["Toyota", "Honda", "Ford", "BMW"]
print("First car brand:", car_brands[0])
print("last car brand", car_brands[3])


# Problem 2
# Create a list of 5 numbers.
# Print the number at index 2.
# Then insert a new number at index 2 and print the updated list.
n=[1, 3, 4, 5, 6]
print("Before Update:", n)
n.insert(2, 2)
print("Num in I-2", n[1])
print("Final list:", n)


# Problem 3
# Create a list of 3 cities.
# Print the length of the list.
# Then use a for loop to print each city.
cities = ["New Yowk", "Los Angeles", "Chicago"]
print("Length of list:", len(cities))
for i in range(len(cities)):
    print("City:", cities[i])

               



# Problem 4
# Create a list of 6 file extensions.
# Print a random one.
# Then pop one at index 3 and print the updated list.
list=[".png", ".jpg", ".gif", ".exe", "pdf", ".mp3"]
print("Random extension:", random.choice(list))
list.pop(3)
print("Upd list:", list)


# Problem 5
# Create a list of 8 names.
# Print the one at the middle index using len().
# Then use a for loop to print all the names.
names = ["John", "Gabriel", "Daniel", "Michael", "James", "David", "Simon"]
print("Middle:", names[len(names) // 2])
for i in names:
    print("Name:", i)


