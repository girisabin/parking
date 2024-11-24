# class mycustomerror(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)

# try:
#     x = -1 
#     if x < 0:
#         raise mycustomerror("custom error") 

# except mycustomerror as e:
#     print("e",e) 
#     print("This is exception")   

# finally:
#     print("The final block executed")  
# 

# def greeting(greetings,bye):
#     def decorator1(fun):
#         def wrapper(*args,**kwargs):
#             print(f"{greetings} before the function runs")
#             fun(*args,**kwargs)
#             print(f"{bye} after the function run")

#         return wrapper
#     return decorator1

# @greeting("hello","bye")
# def say_hello(a,b) :
#     print("a and b",a,b)

# say_hello(1,2)    

# f = open("demofile1.txt",'r')
# # a= f.read()
# # print(a)
# # print(type(a))
# val = f.readline()
# print(val)
# f.close()

# f = open("csvfile.txt",'r')

# lis = []

# for x in f:
#     val = x.strip('\n').split(',')
#     lis.extend(val)

# print(lis)    
import csv

# file_path = 'data.csv'
# with open(file_path,'r') as file:
#     csv_reader = csv.reader(file)
#     header = next(csv_reader)
#     for row in csv_reader:
#         print(row[0])
#         print(type(row))

# print(type(csv_reader))
# data1 = [
#     ['John',22,'london'],
#     ['Tom',23,'Paris'],
#     ['Mike',24,'Berlin']
# ]

# file_path = "output1.csv"
# with open(file_path,mode='w',newline = "") as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow((["Name","Age","City"]))

#     for row in data1:
#         csv_writer.writerow(row)

# 1
# 1 2
# 1 2 3 
# 1 2 3 4
# 1 2 3 4 5


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="   ")
#     print("\n")

########################
# note:
#1.create table for parking system(10)
#1.driver name
#2. vehicle type
# 3.parking time start 
#4. end time
#5. total price
#6 vehicle number
#7.print slip

#fare table
#vehicle type: two wheelerprice/four wheeler price
# 2wheeler :till 1hr : 10rs
#  

# from datetime import datetime

# # Define two date-time strings
# date_str1 = "2024-11-21 10:30:00"
# date_str2 = "2024-11-22 14:45:00"

# # Convert the strings to datetime objects
# date1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
# date2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")

# # Calculate the difference
# difference = date2 - date1            

# # Get the difference in hours
# hours_difference = difference.total_seconds() / 3600

# print(f"The difference in hours is: {hours_difference} hours")  


import datetime

# Get the current date and time for both date1 and date2
date1 = datetime.datetime.now()

date2 = datetime.datetime.now()


# Calculate the difference
difference = date2 - date1

# Get the difference in hours
hours_difference = difference.total_seconds() / 3600

print(f"The difference in hours is: {hours_difference} hours")
    
      


