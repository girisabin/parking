#return type funcyion example

# def add_numbers(a,b):
#     sum = a+b
#     return sum

# result = add_numbers(5,4)
# print("The sum between 5 and 4 is",result)

# non return type

# def addition(a,b):
#     sum = a + b
#     print("Sum is", sum)

# addition(1,2)  

# returning mulytiple value from function
# using Tuple

# def get_stats(numbers):
#     min_value = min(numbers)
#     max_value = max(numbers)  
#     sum_value = sum(numbers)

#     return min_value, max_value, sum_value

# # calling the function
# numbers = [1,2,3,4,5]
# min_value, max_value, total_sum = get_stats(numbers)

# print("Minimum:", min_value)
# print("Maximum:", max_value)
# print("Sum:", total_sum)

# default arguments

# def addition(a,b=2):
#     sum = a + b
#     print("Sum is", sum)

# addition(1)

# Global and local variables

# Local variable

# def my_function():
#     # local variable
#     x=10
# print("Inside function:",x)

# my_function() 

# using global keyword

# z= 30

# def update_global():
#     global z
#     z = z + 5
#     print("Inside function:",z)

# update_global()

# print("Outside function:",z)

# using *args and **kwargs

# def my_function(*kids):
#     print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")   

# def my_function(*args, **kwargs):
#     for arg in args:
#         print(arg)

#     for key ,value in kwargs.items()  :
#         print(f"{key}: {value}")  

# # calling the function with both positional and keyword arguments
# my_function('apple', 'banana', fruit = 'cherry', price = 1.99)        

# Python lambda

# x = lambda a : a+ 10
# print(x(5)) 

# recursion -> function call by itself repetively
# def fact(a):
#     if a == 0 or a == 1:
#         return 1
#     return a* fact(a-1)

# print(fact(4))

# using lambda 

# 1 square number
# square = lambda a : a**2
# print(square(3))

#2 check if number is even

# even_check = lambda a : a%2 == 0
# print(even_check(5))

 

# print(y(3))     

# Fibonacci solve by using recursive function  

# first two terms
# n1, n2 = 0, 1
# count = 0
# nterms = int(input("Enter how many terms : "))

# # check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer")
# # if there is only one term, return n1
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# # generate fibonacci sequence
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1  

# Fabionacci seies using recursive function.
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# n = int(input("Enter the terms you want in series: "))
# print("The fibonacci series:")
# for i in range(n):
#     print(fibonacci(i), end=" ")

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fib_series(n):
    for i in range(n):
        print(fibonacci(i), end=" ")

n=5
print(f"fibonacci series upto {n} term")    
fib_series(n)    





        







