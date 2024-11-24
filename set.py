# set doesnot support duplicate values
#set doesnot support indexing so we use loop in set to get values 
# True and 1 & False and 0 are same

# thisset = {'apple', 'banana' , 'orange'}

# for x in thisset:
#     print(x)

# list = []  empty list
# dit = {}    empty dictionary
# set1 = set() empty set
# str = ""    empty string

# add items 
# thisset = {'apple', 'banana' , 'orange'}
# thisset.add('gauva')
# thisset.add('cherry')
# print(thisset)

# using update we can add two sets

# thisset = {'apple', 'banana' , 'orange'} 
# thisset1 = {'gauva','cherry'}
# thisset.update(thisset1)
# print(thisset)

# remove
# thisset = {'apple', 'banana' , 'orange','gauva','cherry'}

# thisset.remove('apple')
# print(thisset)

#discard
# thisset = {'apple', 'banana' , 'orange','gauva','cherry'}

# thisset.discard('apple')
# print(thisset)

# thisset = {'banana' , 'orange','gauva','cherry'}

# thisset.discard('apple')
# print(thisset)

#pop()

# thisset = {'banana' , 'orange','gauva','cherry'}

# x= thisset.pop()
# print(x)
# print(thisset)

#union() and update() are same
 
# set1 ={'a','b','c'}
# set2 = {1,2,3}
# #set3 = set1.union(set2)  
# set3 = set1 | set2
# set4 = set1.intersection(set2) # or set1 & set2
# print(set3)
# print(set4)

# if multiple set 

# set1 ={'a','b','c'}
# set2 = {1,2,3}
# set3 = {'john','Elena'}
# set4 = {'apple','banana','cherry'}
# set5 = set1.union(set2,set3,set4)  # set1 | set2 | set3 | set4
# print(set5)

#symmetric_difference

# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}

# set3 = set1.difference(set2)
# set4 = set1.symmetric_difference(set2)
# print(set3)
# print(set4)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.difference_update(set2)

# print(set1)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.intersection_update(set2)

# print(set1)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 ^ set2 # same as symmetric_difference
# print(set3)


# list1 = [1,2,1,3,4,1,5,3,5,2]
# a= set(list1)

# list1 = list(a)
# print(list1)

# lst = [1,2,1,2,4,5,6,7,8,9,10,9]
# a=set(lst)
# print(len(a))

# output = [1,2,9]
input_list = [1, 2, 1, 2, 4, 5, 6, 7, 8, 9, 10, 9]

newlist = []

for x in input_list:
    if input_list.count(x)>1:
        newlist.append(x)

print(newlist)   

set1 = set(newlist)
print(set1)

list1 = list(set1)
print(list1)









           
