# calculating the sum of all elements in a matrix using nested loops:  
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ] 
# sum = 0

# for row in matrix:
#     for elements in row:
#         sum += elements

# print("The total sum of matrix elements is",sum) 

# add the even numbers in a new list
# num = [1,2,3,4,5,6,7,8,9,10]
# sum=0
# newlist=[]
# for i in range(len(num)):
#     if num[i]%2 == 0:
#         print(num[i])
#         newlist.append(num[i])
         
# print(newlist)  

# fruit = ["apple", "banana", "cherry", "grapes"]
# print("The list of fruits are ",fruit)
# name = input("Enter the fruit name to replae:")
# name2 = ""

# for x in range(len(fruit)):
#     if fruit[x] ==name:
#         print("index",x)

#         name2 = input ("Enter the  new fruit name:")

#         if name2 in fruit:
#             print("already in the list try new one!!!")

#         else:
#             fruit[x] = name2
               
      
# print(fruit)      


a= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

b= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

sum=0

for i in a:
    for j in b:
        sum[i][j] = a[i][j]+ b[i][j]

print(sum[i][j])    







