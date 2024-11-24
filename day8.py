# creating list of lists
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# for x in matrix:
#     print(x)
#     print(type(matrix))
#     print(x[0])
#     break

# print(matrix[0][1])

# for row in matrix:
#     for elements in row:
#         print(elements, end = ' ')
#     print()  

# calculating the sum of all elements in a matrix using nested loops:  
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]   


# Membership operators : in, not in

# In operator

# fruits = ['apple','banana','orange']

# print("banana" in fruits)

# list methods:

#.insert()


# fruits.insert(100,'orange')
# fruits.insert(-2,'gauva')
# print(fruits)

#.extend()
# fruits1 = ['apple','banana','cherry']
# fruits2 = ['gauva','orange']

# fruits1.extend(fruits2)
# print(fruits1)

# fruits1 = ['apple','banana','cherry']
# thistuple = ('gauva','orange')

# fruits1.extend(thistuple)
# print(fruits1)

# fruits1 = ['apple','banana','cherry']
# str = "fruits"
# thisset = {'gauva','orange'}

# fruits1.extend(thisset)
# fruits1.extend(str)
# print(fruits1)

#.pop()
# thislist = ['a','b','c']
# thislist.pop(1)
# print(thislist)

#del

# fruits1 = ['apple','banana','cherry']
# del fruits1[0]
# print(fruits1)
# del fruits1
# print(fruits1)

#.clear()

# fruits1 = ['apple','banana','cherry']
# fruits1.clear()
# print(fruits1)

#sort lists

# thislist = ['orange', 'apple','cake','milk']
# thislist.sort()
# print(thislist)

# list2 = [5,3,6,7,2,]

# list2.sort()
# print(list2)

# list2 = [5,3,6,7,2,]
# list2.sort(reverse = True)
# print(list2)

# thislist = ['a','Orange', 'Apple','Cake','Milk','b']
# thislist.sort()
# print(thislist)
# thislist.sort(key = str.lower)
# print(thislist)
# thislist.sort(key = str.upper)
# print(thislist)

# reverse()

# thislist = ['a','Orange', 'Apple','Cake','Milk','b']
# thislist.reverse()
# print(thislist)

# copy()

# thislist = ['apple','banana','cherry']
# mylist = thislist  #shallow copy   
# mylist = thislist.copy() # deep copy
# thislist.append("mango")
# print(mylist)

# join two list:

# list1 = ['a','b','c']
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)

# list Comprehension

# fruits = ['apple','banana','mango','cherry','kiwi']
# newlist = []
# for x in fruits:
#     if 'a' in x:
#         newlist.append(x)

# print(newlist)     


# fruits = ['apple','banana','mango','cherry','kiwi']

# newlist = [x for x in fruits if 'a' in x]
# print(newlist)

# num = [1,2,3,4,5,6,7,8,9,10]
# add the even numbers in a new list

# sorted()

# a = ['b','c','a','e', 'd']
# x = sorted(a)
# a.sort()
# print(a)
# print(x)

#Tuples

# tup = (1,2,3)
# x = list(tup)
# print(type(x))
# y = tup(x)

#unpacking a tuple

# fruits=('apple','banana','cherry')

# (green,yellow,red) = fruits

# print(green)
# print(yellow)
# print(red)

# fruits = ('apple','banana','cherry','gauva','orange')

# (green, yellow, *red)= fruits
# print(green)
# print(yellow)
# print(red)  #the values are stored as list in red

# fruits = ('apple','banana','cherry','gauva','orange')

# (green, *yellow, red)= fruits
# print(green)
# print(yellow)

# print(red)  #the values are stored as list in red













