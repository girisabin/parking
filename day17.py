# numbers = [1,2,3,4,5]
# squared = list(map(lambda x: x**2, numbers))
# print(squared)

# lst = [1,2,3,4,5]
# def squared(x):
#     return x**2
# squared_num = list(map(squared,lst))
# print(squared_num)

# numbers = [1,2,3,4,5,6,7,8,9,10]
# even_nums = list(filter(lambda x:x % 2 == 0, numbers))
# print(even_nums)

# list_nums = [1,2,3,4,5,6,7,8,9,10]
# def even(x):
#     return x % 2 == 0
#     # print(x % 2 == 0)

# even_nums = list(filter(even,list_nums))
# print(even_nums)

from functools import reduce

#suming upto a list numbers
# list1 = [1,2,3,4,5]
# sum = reduce(lambda x,y : x + y , list1)
# print(sum)

# finding max_number in list
# list2 = [3,8,1,6,2]
# max_num = reduce(lambda x,y : x if x > y else y, list2 )
# print(max_num)

#Concatenating strings in a list
# list3 = ["Hello"," ", "World","!"]
# sentence = reduce(lambda x,y : x + y, list3)
# print(sentence)

# finding multipication of all members in list using an initializer
# numbers = [1,2,3,4,5]
# product = reduce(lambda x,y:x*y,numbers,1)
# print(product)

# convert strings to uppercase
# words = ["abc","def","ghi"]

# upper_words = list(map(lambda x:x.upper(),words))
# print(upper_words)

# Get words with more than 4 letter
# words = ["cat","elephant","dog","giraffe","bird"]

# words_4 = list(filter(lambda x :  len(x)> 4,words))
# print(words_4)

# remove all the odd number and square the even numbers

# numbers= [1,2,3,4,5,6,7,8,9,10]

# even_num = list(filter(lambda x : x % 2 ==0 ,numbers))
# square_even = list(map(lambda x: x**2,even_num))
# print(square_even)

# convert temp from celsisus to fahrenheit
# fahrenheit = celsius * 9/5 +32
# celsisus = [37,38,39]
# fahrenheit = list(map(lambda x: (x * 9/5 )+32 , celsisus))
# print(fahrenheit)

# remove all the even numbers less tahn 10 from list
#square the remaining numbers
# sum the squared numbers

# list23 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# rem_even_less10_list = list(filter(lambda x: not (x % 2 == 0 and x < 10), list23))
# square_list = list(map(lambda x : x**2, rem_even_less10_list))
# sum_list = reduce(lambda x,y : x+y,square_list)
# print(sum_list)

# list23 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# for i in range(len(list23)):
#     if not(list23[i] % 2==0 and list23[i] < 10):
#         print(list23[i])
    
    

    







            
   
        

    


    
    

       











