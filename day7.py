# s = "12345"
# print(s.isdigit())

# s = "abc"
# print(s.isdigit())

# s = "hello"
# print(s.islower())

#.format():

# s = "hello, {}"
# print(s.format("Python"))

# F-string
# a = 5
# b=10
# sum = f" the sum of {a} and {b} is {a+b}"
# print(sum)

# Escape Characters

txt = "We are the so-called  \" Vikings\ " "from the north."

# creating a list of integer.

numbers = [1,2,3,4,5]
# print(numbers)
# print(type(numbers))

# creating a list of strings

# fruits = ["apple","banana","orange"]
# print(fruits)
# print(type(fruits))

# creating a list of mixed list.
# mixed_list = [10, 'hello', 3.14]

# print(fruits[-1])
# print(numbers[1:4])
# print(fruits[:2])
# print(mixed_list[2:])

# Changing an element

# fruits[1] = "cherry"
# # print(fruits)

# # Adding elements
# fruits.append('grapes')
# # print(fruits)

# # Removing elements

# fruits.remove('apple')
# # print(fruits)

# fruits1 = ["apple","orange","cherry","banana"]

# name = input("Enter the value to replace:")

# for x in range(len(fruits1)):
#     if fruits1[x] == name:
#         print("Index",x)

#         fruits1[x]= input("Enter the new fruits name:")

# print(fruits1)     


# fruits1 = ["apple","orange","cherry","banana"]

# # for x in fruits1:
# #     print(x)

# index=0
# print(len(fruits1))
# while index < len(fruits1):
#     print(fruits1[index])
#     index += 1


fruits1 = ["apple","orange","cherry","banana"]

print("The fruits list are:",fruits1)

name = input("Enter the value to replace:")

for x in range(len(fruits1)):
    if fruits1[x] == name:
        print("Index",x)
    
        fruits1[x]= input("Enter the new fruits name:")

print(fruits1)  
    



 






