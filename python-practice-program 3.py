#EASY PROGRAMS

# 1.Create a tuple of 5 fruits and print the first and last fruit.
# tuple = ["apple", "banana", "cherry", "lameon", "grapes"]
# print("First fruit:", tuple[0])
# print("Last fruit:", tuple[4])

#2.Create a set of 10 numbers and remove all duplicates.
# set = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
# print("unique numbers:", set)

# 3.Create a dictionary of 3 students with their marks and print the marks of a given student. 
# dict = {"Alice": 85, "Bob": 90, "Charlie": 75}
# name = input("Enter the name of the student: ")
# if name in dict:
#     print(f"{name}'s marks: {dict[name]}")
# else:   
#      print("Student not found.")

# 4.Write a function greet_user(name) that prints a greeting for the given name.
# def greet_user(name):
#     print(f"hello, {name}! welcome to python programming.")
# greet_user("Alice")

# 5. Create a list of 5 numbers and print their squares using a lambda function and map() -
# num = [1,2,3,4,5]
# squares = list(map(lambda x: x**2, num))
# print("squares of the numbers:", squares)

# 6. Create a dictionary of names and ages; update the age of one person and print the dictionary.
# dict = {"Alice": 25, "Bob": 30, "Charlie": 35}
# dict["Bob"] = 31
# print("Updated dictionary:", dict)

# 7. Use a generator function to yield the first 5 even numbers.
# def even_numbers(n):
#     for i in range(2, n*2 + 1, 2):
#         yield i
# for even in even_numbers(5):
#     print(even)

# 8. Create a set of 5 colors and check if a color "blue" exists in it.
# color = {"red", "green", "blue", "yellow", "purple"}
# if "blue" in color:
#     print("blue exists in the set.")
# else:
#     print("blue does not exist in the set.")

# 9. Create a tuple of numbers and count how many times a particular number occurs.
# tuple= (1,2,2,2,2,3,4,5,3,2)
# num= 2
# count = tuple.count(num)
# print(f"{num} occurs {count} times in the tuple.")

#10.Use a for loop to iterate over a dictionary of fruits and their prices, printing each key and value.
# dict = {"apple": 1.5, "banana": 0.5, "cherry": 2.0}
# for fruit, price in dict.items():
#     print(f"{fruit}: ${price}")

#INTERMEDIATE PROGRAMS

#1.Create a dictionary comprehension where keys are numbers 1–10 and values are cubes of the keys.
# dict ={"yash" : 10, "sachin" : 20, "rohit" : 30}
# cubes= list(map(lambda x: x**3, dict.values())) 
# print("cubes are:", cubes)

#2.Write a function that accepts variable-length arguments and returns their sum.
# def sum_all(*num):
#     sum = 0
#     for n in num:
#         sum += n
#     print("sum of all numbers:", sum)

# sum_all(1,2,3,4,5,6,7,8,9,10)


#3.Create a generator function that yields the Fibonacci sequence up to n terms.
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
# n = 10
# for num in fibonacci(n):
#     print(num)

#4.Use filter() to select all odd numbers from a list of 1–20.
# list1 = [1, 2, 3, 4, 5]
# odd = list(filter(lambda x: x % 2 != 0, list1))
# print("odd numbers are:", odd)

#5.Use reduce() to multiply all numbers in a list of 1–5.
# from functools import reduce
# list1 = [1, 2, 3, 4, 5]
# mul = reduce(lambda x, y: x * y, list1)
# print("result is:", mul)

#6.Write a lambda function that checks if a number is prime, and use it with filter() on a list of numbers 1–20.
# num = 5
# prime = list(filter(lambda x: x % 2 != 0, range(2, num + 1)))
# print("prime numbers are:", prime)

#7.Merge two dictionaries using dictionary comprehension.
# dict1 = {"yash": 10, "sachin" : 20, "rohit" : 30}
# dict2 = {"y": 10, "s" : 20, "t" : 30}
# print("merge of dict1 and dict2:", {**dict1, **dict2})

#8.Create a set of numbers 1–10 and print numbers that are common with another set {5, 6, 7, 8}.
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# intersection = set1.intersection(set2)
# print("intersection of set1 and set2:", intersection)

#9.Create a nested dictionary to store 3 students with their marks in 2 subjects each. Print total marks for each student.
# students = { "Alice": {"Math": 85, "Science": 90},
#              "Bob": {"Math": 75, "Science": 80},
#              "Charlie": {"Math": 90, "Science": 85} }
# for student, subjects in students.items():
#     total = sum(subjects.values())
#     print(f"{student}'s total marks: {total}")

#10.Write a function with default arguments to calculate the area of a rectangle, defaulting to 1 if width is not provided.
# def area_rectangle(height,width=1):
#     area = width * height
#     print("area of rectngle:", area)
# area_rectangle(height=5)

#HARD PROGRAMS
 
#1.Write a generator that produces an infinite sequence of prime numbers; use next() to get the first 10 primes.
# def prime_generator():
#     num = 2   
#     while True:
#         is_prime = True
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             yield num
# primes = prime_generator()
# for _ in range(10):
#     print(next(primes))

#2.Create a dictionary comprehension to invert keys and values of a given dictionary, handling duplicate values by storing them in a list.
# original_dict = {"A": 85, "B": 90, "C": 75, "D": 85}
# inverted_dict = {}
# for key, value in original_dict.items():
#     if value not in inverted_dict:
#         inverted_dict[value] = key
#     else:
#         if isinstance(inverted_dict[value], list):
#             inverted_dict[value].append(key)
#         else:
#             inverted_dict[value] = [inverted_dict[value], key]
# print("Inverted dictionary:", inverted_dict)

#3.Write a function that accepts a list of dictionaries (each representing a student with marks) and returns the student with the highest total marks.
# students = [
#     {"name": "Alice", "Math": 85, "Science": 90},
#     {"name": "Bob", "Math": 75, "Science": 80},
#     {"name": "Charlie", "Math": 90, "Science": 85}
# ]
# def highest_marks(students):
#     highest_student = None
#     highest_total = 0
#     for student in students:
#         total = student["Math"] + student["Science"]
#         if total > highest_total:
#             highest_total = total
#             highest_student = student["name"]
#     return highest_student, highest_total
# name, total = highest_marks(students)
# print(f"Student with highest total marks: {name} with {total} marks.")

#4.Use map() and a lambda function to normalize a list of numbers between 0 and 1.
# numbers = [10, 20, 30, 40, 50]
# max_num = max(numbers)
# min_num = min(numbers)
# normalized = list(map(lambda x: (x - min_num) / (max_num - min_num), numbers))
# print("normalized numbers:", normalized)

#5.Create a tuple of tuples representing (name, score). Sort it by score using a lambda function.
# scores = (("Alice", 85), ("Bob", 90), ("Charlie", 75))
# sorted_scores = sorted(scores, key=lambda x: x[1])
# print("sorted scores:", sorted_scores)

#6.Write a generator to yield all palindromic numbers between 1 and 1000.
# def palindrome_generator():
#     for num in range(1, 1001):
#         if str(num) == str(num)[::-1]:
#             yield num
# for palindrome in palindrome_generator():
#     print(palindrome)

#7.Write a function that accepts another function as a parameter and applies it to a list of numbers (demonstrating higher-order functions).
# def apply_function(func, numbers):
#     return [func(num) for num in numbers]
# def square(x):
#     return x ** 2
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = apply_function(square, numbers)
# print("squared numbers:", squared_numbers)

#8.Create two sets of strings and use set operations to find words unique to the first set, common words, and words unique to the second set.
# set1 = {"apple", "banana", "cherry", "date"}
# set2 = {"banana", "cherry", "date", "fig"}
# unique_to_set1 = set1 - set2
# common_words = set1 & set2
# unique_to_set2 = set2 - set1
# print("Unique to set1:", unique_to_set1)
# print("Common words:", common_words)
# print("Unique to set2:", unique_to_set2)

#9.Write a recursive function to flatten a nested dictionary (keys can be nested dictionaries) into a single-level dictionary with tuple keys representing the path.
# def flatten_dict(d, parent_key=()):
#     items = {}
#     for k, v in d.items():
#         new_key = parent_key + (k,)
#         if isinstance(v, dict):
#             items.update(flatten_dict(v, new_key))
#         else:
#             items[new_key] = v
#     return items
# nested_dict = {
#     "Alice": {"Math": 85, "Science": 90},
#     "Bob": {"Math": 75, "Science": 80},
#     "Charlie": {"Math": 90, "Science": 85}
# }
# flat_dict = flatten_dict(nested_dict)
# print("Flattened dictionary:", flat_dict)

#10.Write a function to calculate the factorial of a number using a generator to yield intermediate factorial values, and use reduce() to compute the final result.
# from functools import reduce
# def factorial_generator(n):
#     factorial = 1
#     for i in range(1, n + 1):
#         factorial *= i
#         yield factorial
# n = 5
# factorials = factorial_generator(n)
# final_factorial = reduce(lambda x, y: y, factorials)
# print(f"Factorial of {n} is: {final_factorial}")
