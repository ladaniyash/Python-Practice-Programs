#EASY PROGRAMS

#1. write a program to take two num as input and print their sum
#num1 = eval(input("Enter number: "))
#num2 = eval(input("Enter number: "))
#ans=num1+num2
#print("sum of given two number is : ",ans)

#2. to check whether a given number is odd or even
#num = eval(input("Enter number: "))
#if(num % 2 == 0):
 #print("Even")
#else:
 #   print("Odd")
    
    
#3. to take string as input  and print its length
#name= input("Enter your name")
#length=len(name)
#print(length)

#4. to calculate the square of a given number
#num1= eval(input("enter number"))
#ans = num1 * num1
#print(ans)

#5. to find thethe greater of two number using if-else
#n1 = eval(input("enter first number"))
#n2 = eval(input("enter second number"))
#if n1 > n2:
 #   print(n1,"is greater than",n2)
#else:    
 #   print(n2,"is greater than",n1)



#6. use for loop to print number from 1 to 
#for i in range(1, 6):
 #   print(i)


#7. use a while loop to calculate the sum of the first 10 natural num   

# i = 1
# sum = 0
# while i <= 10:
#     sum += i
#     i += 1
# print("Sum of the first 10 natural numbers is:", sum)


#8. take a string input and print it in reverse
# name = input("Enter a string: ")
# print("Reverse of the string is:", name[::-1])


#9. to check if a number is positive,negative or zero
# num = eval(input("Enter a number: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")


#10. print the multiplication table of anumber using a for loop
#for i in range(1, 11):
#    print("5 x",i,"=",5*i)

#MEDIUM PROGRAMS

#1. Write a program to calculate factorial using a for loop.
#a= eval(input("Enter first number: "))
#ans= 1
#for i in range(1, a + 1):
#    ans= a * i
#    print(ans)
#print("Factorial of", a, "is:", ans)

#2. sum all the even number from 1 to n
#n = eval(input("Enter the value of n: "))
#sum = 0
#for i in range(2, n + 1, 2):
#    sum += i
#print("Sum of even numbers from 1 to", n, "is:", sum)

#3. take a string input and count the vowels
# name = input("Enter a string: ")
# vowel = 'aeiouAEIOU'
# count = 0
# for a in name:
#     if a in vowel:
#         count += 1     
# print("Number of vowels in the string is: ", count)

#4. check if number is prime or not
# n = eval(input("Enter a number: "))       
# if n > 1:
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             print(n, "is not a prime number.")
#             break
#     else:
#         print(n, "is a prime number.")
# else:
#     print(n, "is not a prime number.")

#5. print all the numbers between 10 to 50  divisible by 3 using a loop
# print("Numbers divisible by 3 from 1 to 50:")
# for i in range(10, 51):
#     if i % 3 == 0:
#         print(i)

#6. take three numbers as input and print the largest using if-else if.
# n1 = eval(input("Enter first number: "))
# n2 = eval(input("Enter second number: "))
# n3 = eval(input("Enter third number: "))
# if n1 >= n2 and n1 >= n3:
#     print(n1, "is the largest number.")
# elif n2 >= n1 and n2 >= n3:
#     print(n2, "is the largest number.")
# else:
#     print(n3, "is the largest number.")

#7. print the first n term of the fibonacci series.
# n = eval(input("Enter the number of terms: "))
# a, b = 0, 1 
# count = 0
# print("Fibonacci sequence up to", n, ":")
# while count < n:
#     print(a)
#     a, b = b, a + b
#     count += 1

#8. write a a program to calculate thwe su
# m of the digit of a number
# n = eval(input("Enter a number: "))
# sum = 0
# while n > 0:
#     digit = n % 10
#     sum += digit
#     n //= 10    
# print("Sum of digits:", sum)

#9. Take a number as input in a loop and break when a negative number is entered. print the sum of all numbers entered before negative.
# sum = 0
# while True    
#     n = eval(input("Enter a number: "))
#     if n < 0:
#         break
#     sum = sum + n
# print("Sum of numbers entered before negative:", sum) 

#10. print numbers 1 to 20 , but skip multiple of 5 using continue
# for i in range(1, 21):
#    if i % 5 == 0:      
#        continue
#    print(i)

# HARD PROGRAMS

#1.check weather a given string is palindrom
# str1 = input("Enter a string: ")
# if str1 == str1[::-1]:    
#    print("The string is a palindrome.")
# else:
#   print("The string is not a palindrome.")
 
#2.calculate the GCD using loops and if else statment greatest common diviser

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# gcd = 1
# for i in range(1, min(num1, num2) + 1): 
#     if num1 % i == 0 and num2 % i == 0:
#         gcd = i
# print("GCD:", gcd)


#3. Take a string and count the number of words.
# str1 = input("Enter a string: ")
# words = str1.split()
# count = len(words)
# print("Number of words in the string is:", count)
  
#4. print the following patterns for N=5.
# for i in range(1, 6):
#     print("*" * i)  


#5. reverse a given integer without converting it to a string.
# num = eval(input("enter a number: "))
# reverse = 0 
# while num> 0:
#     digit = num % 10 
#     reverse = reverse * 10 + digit
#     num //= 10
# print("Reverse of the number is:", reverse)

#6 
# n = int(input("Enter the number of values: "))  
# sum_of_squares = 0
# for _ in range(n):
#     value = int(input("Enter a number: "))
#     sum_of_squares += value ** 2
# print("Sum of squares:", sum_of_squares)

#7.
# num = eval(input("Enter a number: "))
# cube = 0  
# temp = num
# while temp > 0:
#     digit = temp % 10 
#     cube += digit ** 3
#     temp //= 10
# if num == cube:
#     print(num, "is an Armstrong number.")
# else:
#     print(num, "is not an Armstrong number.")

#8 count the frequency of each character in a string
# string = input("Enter a string: ")
# frequency = {}
# for char in string:
#     frequency[char] = frequency.get(char, 0) + 1
# print("Character frequencies:", frequency)
# frequency = {}

# 9.
# for i in range (49,0,-2):
#     print(i)

#10. build a calculatror that takes two numbers and an operator as input and performs the  operation.
# a=int(input(print("enter 1 st no :")))
# b=int(input(print(" 1-> +  2-> - 3-> *  4->/ :")))
# c=int(input(print("enter 2 st no :")))
# if b==1:
#     d=a+c
#     print(d)
# elif b==2:
#     d=a-c
#     print(d)
# elif b==3:
#     d=a*c
#     print(d)
# elif b==4:
#     d=a/c
#     print(d)
# else :
#     print("error")

#EXTRA HARD PROGRAMS

#1.Take two numbers, start and end, and print all prime numbers in that range.
# start = int(input("Enter the start number: "))
# end = int(input("Enter the end number: "))    
# for num in range(start, end + 1):
#     if num > 1:
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 break
#         else:
#             print(num)    

# 2.Print a pattern where each row i contains the number i repeated i times.
# n = int(input("Enter the number of rows: "))  
# for i in range(1, n + 1):
#     print(str(i) * i)

# 3.Take a number and calculate the sum of the factorials of its digits.
# num = int(input("Enter a number: "))
# sum_of_factorials = 0
# temp = num
# while temp > 0:
#     digit = temp % 10
#     factorial = 1
#     for i in range(1, digit + 1):
#         factorial *= i
#     sum_of_factorials += factorial
#     temp //= 10
# print("Sum of factorials of digits:", sum_of_factorials)

# 4.The computer chooses a random number between 1 and 50. User keeps guessing until correct. Give hints if the guess is higher or lower.
# import random
# number_to_guess = random.randint(1, 50)
# guess = None
# while guess != number_to_guess:
#     guess = int(input("Guess the number between 1 and 50: "))
#     if guess < number_to_guess:
#         print("Too low! Try again.")
#     elif guess > number_to_guess:
#         print("Too high! Try again.")
# print("Congratulations! You've guessed the number.")

# 5.Take an integer and count how many digits are even and how many are odd.
# num = int(input("Enter an integer: "))
# even_count = 0
# odd_count = 0             
# while num > 0:
#     digit = num % 10
#     if digit % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
#     num //= 10
# print("Even digits count:", even_count)
# print("Odd digits count:", odd_count)

# 6.Take a string and a character, and count occurrences of that character without using built-in functions.
# string = input("Enter a string: ")
# char_to_count = input("Enter a character to count: ")
# count = 0
# for char in string:
#     if char == char_to_count:
#         count += 1
# print(f"The character '{char_to_count}' occurs {count} times in the string.")

# 7.Take N numbers as input and print the multiplication table for each number.
# n = int(input("Enter the number of values: "))
# numbers = []
# for _ in range(n):
#     num = int(input("Enter a number: "))
#     numbers.append(num)
# for num in numbers:
#     print(f"Multiplication table for {num}:")
#     for i in range(1, 11):
#         print(f"{num} x {i} = {num * i}")

# 8.Take a number and sum all digits that are prime (2, 3, 5, 7).
# num = int(input("Enter a number: "))
# prime_sum = 0
# temp = num
# while temp > 0:
#     digit = temp % 10
#     if digit in [2, 3, 5, 7]:
#         prime_sum += digit
#     temp //= 10
# print("Sum of prime digits:", prime_sum)

# 9.Print a diamond-shaped star pattern for a given odd number N.
# n = int(input("Enter an odd number: "))
# if n % 2 == 0:
#     print("Please enter an odd number.")
# else:
#     for i in range(n):
#         if i <= n // 2:
#             print(" " * (n // 2 - i) + "*" * (2 * i + 1))
#         else:
#             print(" " * (i - n // 2) + "*" * (2 * (n - i) - 1))

# 10.Print a rectangle of size M × N with stars, but replace the diagonal with numbers 1 to min(M,N).
# m = int(input("Enter the number of rows (M): "))
# n = int(input("Enter the number of columns (N): "))
# for i in range(m):
#     for j in range(n):
#         if i == j:
#             print(min(m, n) - i, end="")
#         else:
#             print("*", end="")
#     print()

# Project = Mini Contact Book
# contacts = {}

# while True:
#     print("\n1. Add Contact  2. Search  3. Exit")
#     choice = input("Choose an option: ")
    
#     if choice == '1':
#         name = input("Enter Name: ")
#         phone = input("Enter Phone: ")
#         contacts[name] = phone
#         print(f"Contact {name} saved!")
        
#     elif choice == '2':
#         name = input("Search Name: ")
#         result = contacts.get(name, "Contact not found.")
#         print(f"Result: {result}")
        
#     elif choice == '3':
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice, try again.")