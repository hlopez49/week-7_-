# list comprehension = A concise way to create lists in Python
#  they are Compact and and easier to read than traditional loops 
#  [do a expression for a value in iterable if condition]
# doubles = []
# for x in range(1,11):
#     doubles.append(x*2)
#     print(doubles)
# Iterates throuth 1,10 and multples it by the thing at the beginning wether its *2, *2 or squared
# doubles = [x * 2 for x in range(1,11)]
# print(doubles)

# triples = [y * 3 for y in range(1,11)]
# print(triples)

# squares = [z * z for z in range(1,11)]
# print(squares)

# will iterate through the list and uppercase every term
# fruits = ["apple", "orange", "banana", "coconut"]
# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)

# or 
# you put the list straight into the comprehension
# fruits = [fruit.upper() for fruit in ["apple", "orange", "banana", "coconut"]]
# print(fruits)

# will get every first litter of every term
# fruits = ["apple", "orange", "banana", "coconut"]
# fruit_chars = [fruit[0] for fruit in fruits]
# print(fruit_chars)

# numbers = [1, -2, 3, -4, 5, -6, 8]
# positive_nums = [num for num in numbers if num >= 0]
# negative_nums = [num for num in numbers if num < 0]
# even_nums = [num for num in numbers if num % 2 == 0]
# odd_nums = [num for num in numbers if num % 2 == 1]

# print(positive_nums)
# print(negative_nums)
# print(even_nums)
# print(odd_nums)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)
################################################List comprehension###############################################
# List Comprehensions Practice #1
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# Create a square_values list consisting of the numbers in the values list, squared.

# values = [1, 2, 3, 4, 5, 6, 9.5]




# List Comprehensions Practice #2
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# Create an even_values list consisting of the numbers in the values list that (you guessed it!) are even.

# values = [1, 2, 3, 4, 5, 6, 9.5]




# List Comprehensions Practice #3
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# For the following list of temperatures in degrees Fahrenheit, express these same values in a new list of temperature values in degrees Celsius. The conversion between type of units is as follows:

# °C = (°F - 32) * (5/9)

# or expressed in another way:

# (degrees_fahrenheit-32)*(5/9)

# The list of temperatures is as follows:

# temperature_fahrenheit = [32, 212, 275]

# Store this new list in a variable called degrees_celsius




