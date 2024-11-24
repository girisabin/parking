# f = open("demofile1.txt","r")
# a = f.read()
# # print(a)
# # print(type(a))
# # print(a[0:5])
# # print(a[-10:-1])
# # print(a[-4:])
# val = f.readline()
# print(val)
# f.close()

# # read() 
# # readline()
# # readlines()

# f = open("csvfile.txt","r")



# lst = []
# for x in f:


#     val = x.strip("\n").split(',')
#     lst.extend(val)
# print(lst)    

# import csv

# file_path = 'data.csv'
# with open(file_path, mode='r') as file:
#     csv_reader = csv.reader(file)
#     header = next(csv_reader)
#     header = next(csv_reader)
#     for row in csv_reader:
#         print(row[1])
        # print(type(row))

# print(type(csv_reader)) 

# import csv
# data = [
#     ["Alice",23,'london'],
#     ['bob',24,'Paris'],
#     ['charlie',26,'Berlin']
# ]
# file_path = 'output.csv'
# with open(file_path, mode = 'w', newline='') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(['Name', 'Age', 'City']) # write header

#     for row in data:
#         csv_writer.writerow(row)    

# import os

# # get current working directory

# current_dir = os.getcwd()

# # list files in a directory

# files = os.listdir(current_dir)

# import random

# random_number = random.randint(1, 10)
# print(random_number)

# my_list = [1,2,3,4,5]
# random.shuffle(my_list)

# import math

# sqrt_value = math.sqrt(25)
# print(sqrt_value)

# factorial_value = math.factorial(4)
# print(factorial_value)

