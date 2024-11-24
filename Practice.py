# value = input("Enter any number:")

# if value.isdigit():
#     num = int(value)
#     print(f"converted into integer:{num}")

# elif '.':
#     num = float(value)
#     print(f"converted into float:{num}")

# else:
#     print("Invalid number input!!!")   

# a=2
# b=3

# print("A") if a>b else print("B")

# x=int(input("Enter a number:"))

# if x>0:
#     print("x is +ve")

#     if x<10:
#         print("x is single digit no.")

#     else:
#         print("x is not single digit no.")    

# else:
#     print("x is -Ve") 

# x=4
# y=3
# sum = 1 if x>=y else print("B")
# print(sum)


# num1 = int(input("Enter num1:"))
# num2 = int(input("Enter num2:"))

# if num1 > num2:
#     print("num1 is greater")

# else:
#     if num1 == num2:
#         print("They are equal") 

#     else:
#         print("num2 is greater")

# print("num1 is greater") if num1>num2 else print("=") if num1 == num2 else print("num2 is greater")

# a=12
# b=17

# if not a>b:
#     print("a is smaller than b")

# numbers= [1,2,3,4,5]

# for num in numbers:
#     print(num)

# numbers= [1,2,3,4,5]
# num = None

# for num in numbers:
#     if num%2==0:
#         print(f"The no. is even {num}")

#     else:
#         print(f"The no. is odd {num}")   

# numbers= [1,2,3,4,5]
# num = None

# for num in numbers:
#     if num%3==0:
#         print(f"The no. is {num}")

# count=0
# for x in "banana":
#     if x=="n":
#         count+=1
# print(count)        


# for x in "bananan":
#     count=0
#     if x=="n":
#         count+=1
# print(count)

# fruits = ["apple","banana","orange"]
# for x in fruits:
#     print(x)

#     if x == "banana":
#         break


# fruits = ["apple","banana","cherry"]
# for x in fruits:
#      if x == "banana":
#         continue
#      print(x)

# num = [1,2,3,4,5,6,7,8,9,10]

# for x in num:
#     if x == 5:
#         continue
    

#     elif x== 7:
#         break

#     print("The value in num excepts 5 till 6",x)


# a=1
# for x in range(6):
#     if x==0:
#         continue
#     a=a*x
# print("multipication ",a)

# for x in range(-2,2):
#     print(x)

# for x in range(0,31,2):
#     print(x)


# for x in range(1,30,2):
#     print(x)

# adj = ["red","yellow","blue"]

# fruits = ["apple", "banana","cherry"]

# for x in adj:
#     for y in fruits:
#         print(x,y)

# var = "hello world"

# for i in range(len(var)):
#     if var[i]=="w":
#         print(f"The index of w is {i}")

# for a in var:
#     if a.upper()=="H":
#         print("The char is h or H")

#     else:
#         print("The char is not h or H")

#swapping
# x=10
# y=20

# # tem=x
# # x=y
# # y=tem
# # print(x,y)
# x=x+y #30
# y=x-y #10
# x=x-y #30-10=20
# print(x,y)

# i=1
# while i<6:
    
# #     print(i)
# #     i+=1

# # var= "hello world"

# # print(var[::-1])

# # a= "Hello world"
# # a= "h" + a[1:]
# # print(a)

# # a= "Hello world 1 2"
# # # print(a.rstrip())
# # print(a.split(' '))

# # a = ["apple","banana","orange"]
# # a= print(' '.join(a))

# # x = "Hello,World!,123"

# # print(x.split(','))

# # name = "##############hello####world##########"
# # name = name.strip('#')
# # name = name.split('####')
# # print(name)

# name = "##################hello###world######################"
# # name = ["hello", "world"]
# lside_length = len(name)- len(name.lstrip('#'))
# rside_length = len(name) - len(name.rstrip('#'))
# name1 = name.strip("#")

# name_lst = name1.split("###") #["hello","world"]

# total = '#' * lside_length + '###'.join(name_lst) + '#' * rside_length

# print(total)


fruit = ["apple", "banana", "cherry", "grapes"]
print("The list of fruits are ",fruit)
name = input("Enter the fruit name to replae:")

for x in range(len(fruit)):
    if fruit[x] ==name:
        print("index",x)

        fruit[x] = input ("Enter the  new fruit name:")


        for y in range(len(fruit)):
            if fruit[y]==fruit[x]:
                print("The fruits name is already exits in list try new one!!")

    
print(fruit)












    









    

    




     
         













    


