#SIMPLE PROGRAMS

#1.Take a string input and print each character on a new line.
# str = input("Enter a string: ")
# for char in str:  
#     print(char)

#2.Count the number of spaces in a given string.
# str = input("Enter a string: ")
# count = 0
# for i in str:
#     if i == " ":
#         count += 1
# print("Number of spaces in the string: ", count)

#3.Reverse a string without using slicing ([::-1]).
# str = input("Enter a string: ")
# reversed_str = ""
# for i in str:
#     reversed_str = i + reversed_str
# print("Reversed string: ", reversed_str)

#4.Create a list of 5 numbers and print the sum of all elements.
# l1= [1, 2, 3, 4, 5]
# print("Sum of all elements: ", sum(l1))

#5.Take a list of numbers and print only the positive numbers.
# l1= [-1, 2, -3, 4, -5]
# positive_numbers = []   
# for num in l1:
#     if num > 0:
#         positive_numbers.append(num)
# print("Positive numbers: ", positive_numbers)

#6.Take two strings and concatenate them with a space in between.
# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")
# concatenated_str = str1 + " " + str2
# print("Concatenated string: ", concatenated_str)

#7.Print the first and last character of a given string.
# str = input("Enter a string: ")
# first_char = str[0]
# last_char = str[-1]     
# print("First character: ", first_char)
# print("Last character: ", last_char)

#8.Create a list of 10 integers and print the maximum and minimum values.
# l1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# max_value = max(l1)   
# min_value = min(l1)
# print("Maximum value: ", max_value) 
# print("Minimum value: ", min_value)

#9.Take a number n and print a list of the first n even numbers.
# n = int(input("Enter a number: "))
# even_numbers = []
# for i in range(n):
#     even_numbers.append(2 * i)            
# print("First n even numbers: ", even_numbers)

#10.Take a string input and check if it starts with a vowel.
# str = input("Enter a string: ")
# vowel ="aeiouAEIOU"
# if str[0] in vowel:
#     print("The string starts with a vowel.")
# else:
#     print("The string does not start with a vowel.")

#INTERMEDIATE PROGRAMS

#1.Count the number of uppercase and lowercase letters in a given string.
# str = input("Enter a string: ")
# uppercase_count = 0   
# lowercase_count = 0
# for char in str:
#     if char.isupper():
#         uppercase_count += 1
#     elif char.islower():
#         lowercase_count += 1
# print("Number of uppercase letters: ", uppercase_count)
# print("Number of lowercase letters: ", lowercase_count) 

#2.Remove all vowels from a given string.
# str = input("Enter a string: ")
# vowel = "aeiouAEIOU"
# result = ""
# for c in str:
#     if c not in vowel:
#         result += c
# print("String without vowels: ", result)

#3.Take a list of numbers and return a list of only the prime numbers.
# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# prime_numbers = []
# for num in l1:
#     if num > 1:
#         is_prime = True
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:      
#                 is_prime = False
#                 break
#         if is_prime:
#             prime_numbers.append(num)
# print("Prime numbers: ", prime_numbers)


#4.Given a list of strings, print all strings with length greater than 3.
# l1 = ["apple", "hi", "banana", "ok", "grape"]
# for s in l1:
#     if len(s) > 3:
#         print(s)

#5.Replace all spaces in a string with underscores.
# str = input("Enter a string: ")
# result = str.replace(" ","_")
# print("String with spaces replaced: ", result)

#6.Take a list of numbers and create a new list with each number squared.
# l1 = [1,2,3,4,5]
# l2 = [x**2 for x in l1]
# print("List with squared numbers: ", l2)

#7.Given a string, print it in reverse word order.
# str = input("Enter a string: ")
# word = str.split()
# reversed_word = word[::-1]
# reversed_str = " ".join(reversed_word)
# print("Reversed word order: ", reversed_str)

#8.Merge two lists element-wise into a list of tuples. 
# l1 = [1, 2, 3]
# l2 = ['a', 'b', 'c']
# merged_list = list(zip(l1, l2))
# print("Merged list of tuples: ", merged_list)

# 9. Take a list of integers and move all zeros to the end.
# l1 = [1, 0, 2, 0, 3, 0, 4]
# l1 = [x for x in l1 if x != 0] + [0] * l1.count(0)
# print("List with zeros at the end: ", l1)

# 10. Take a string and print a dictionary with the count of each character.
# str = input("Enter a string: ")
# char_count = {}
# for char in str:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
# print("Character count: ", char_count)

#ADVANCE PROGRAMS

#1. Take a string and return the longest word in the string.
# str = input("Enter a string: ")
# words = str.split()
# longest_word = max(words, key=len)
# print("Longest word: ", longest_word)


#2. Implement a basic calculator that takes a string input like "5 + 3" and returns the result.
# def calculator(expression):
#     num1, operator, num2 = expression.split() 
#     num1 = float(num1)
#     num2 = float(num2)    
#     if operator == "+":
#         return num1 + num2
#     elif operator == "-":
#         return num1 - num2    
#     elif operator == "*":
#         return num1 * num2
#     elif operator == "/":
#         if num2 != 0:
#             return num1 / num2
#         else:
#             return "Error: Division by zero"    
#     else:
#         return "Error: Invalid operator"
# expression = input("Enter an expression (e.g., '5 + 3'): ")
# result = calculator(expression)
# print("Result: ", result)

#3. Flatten a nested list (list containing sublists of arbitrary depth) into a single list.
# def flatten(nested_list):
#     flat_list = []
#     for item in nested_list:
#         if isinstance(item, list):
#             flat_list.extend(flatten(item))
#         else:
#             flat_list.append(item)
#     return flat_list
# nested_list = [1, [2, [3, 4], 5], 6]
# flat_list = flatten(nested_list)
# print("Flattened list: ", flat_list)

#4. Given a list of numbers, generate a dictionary with numbers as keys and their factorial as values.
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# numbers = [0, 1, 2, 3, 4, 5]
# factorial_dict = {num: factorial(num) for num in numbers}
# print("Factorial dictionary: ", factorial_dict)

#5. Implement a function that checks if a string is a palindrome (ignoring spaces and cases).
# def is_palindrome(s):
#     cleaned_str = s.replace(" ", "").lower()
#     return cleaned_str == cleaned_str[::-1]
# str = input("Enter a string: ")
# if is_palindrome(str):
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

#6. Given a list of strings, create a new list containing only strings that are anagrams of the first string.
# def are_anagrams(str1, str2):
#     return sorted(str1) == sorted(str2)
# strings = ["listen", "silent", "enlist", "inlets", "google"]
# anagrams = [s for s in strings if are_anagrams(strings[0], s)]
# print("Anagrams of the first string: ", anagrams)

#7. Print a pattern of numbers in pyramid shape for n rows:
#    1
#    1 2
#    1 2 3
#  ...  
# n = int(input("Enter the number of rows: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print() 

#8. Take a sentence and return a dictionary where keys are words and values are the length of each word.
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# word_lengths = {word: len(word) for word in words}
# print("Word lengths: ", word_lengths)

#9. Simulate a queue system using a list and implement enqueue and dequeue operations for user inputs.
# queue = []
# def enqueue(item):
#     queue.append(item)
# def dequeue():
#     if len(queue) > 0:
#         return queue.pop(0)
#     else:
#         return "Queue is empty"
# while True:
#     action = input("Enter 'enqueue' to add to queue, 'dequeue' to remove from queue, or 'exit' to quit: ")
#     if action == "enqueue":
#         item = input("Enter an item to enqueue: ")
#         enqueue(item)
#         print("Current queue: ", queue)
#     elif action == "dequeue":
#         removed_item = dequeue()
#         print("Dequeued item: ", removed_item)
#         print("Current queue: ", queue)

#10. Given a list of numbers, generate all possible pairs (a, b) where a < b and sum of pair is even.
# numbers = [1, 2, 3, 4, 5]
# pairs = []
# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if (numbers[i] + numbers[j]) % 2 == 0:
#             pairs.append((numbers[i], numbers[j]))
# print("Pairs with even sum: ", pairs)
