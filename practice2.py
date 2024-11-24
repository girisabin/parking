# name = "###################hello#####world#########################"

# lstrip_name = len(name) - len(name.lstrip('#'))
# rstrip_name = len(name) - len(name.rstrip('#'))
# name1 = name.strip('#')
# print(name1)

# list_name1 = name1.split('#####')
# print(list_name1)

# total = '#' * lstrip_name + '#####'.join(list_name1) + '#' * rstrip_name
# print(total)

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

# list comprehension

# fruit = ["apple", "cherry", "grapes", "banana"]
# newlist = []
# for x in fruit:
#     if 'a' in x:
#         newlist.append(x)

# print(newlist)  
# newlist =[x for x in fruit if 'a' in x]   
# print(newlist)   
# fruit.sort()
# print(fruit)
# x = sorted(fruit)
# print(x)


# college = {
#     "student1":{
#         "name":"abc",
#         "score" : [1,2,3,4]
#     },
#     "student2":{
#         "name": "cde",
#         "score" : [5,6,7,8,9]
#     }
# }
# total_score = 0

#output
#student1 score : 10
#student2 score : 35

# x = college["student1"]["score"]  
# for j in x:
#     sum1 += j
# print("student1 score:",sum1)    
    
# y = college["student2"]["score"]  
# for i in y:
#     sum2 += i

# print("student2 score:",sum2) 


# Calculate total scores
# for k, v in college.items():
#     total_score = sum(v["score"])
#     print(f"{k} score : {total_score}")

# for k,v in college.items():
    
#     x = v.get("score")
#     print(x)
#     for i in x:
#         total_score += i
        
#     print(total_score)    

# n1,n2 = 0,1
# count = 0
# n = int(input("Enter the how many terms : "))
# if n <= 0:
#     print("Input +ve number!!!")
# elif n == 1 :
#     print("Fabonacci series upto nth terms: ")
#     print(n1)
    

# else:
#     print("Fabonacci series upto nth terms:")
#     for i in range(0,n):
#         print(n1)
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth

# class A:
#     def method_A(self):
#         return "A"

# class B:
#     def method_B(self):
#         return "B" 

# class C(A,B):
#     def method_C(self):
#         return "C" 

# obj = C()
# print(obj.method_A())              
# print(obj.method_B())
# print(obj.method_C())

# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width
    
# class Square(Rectangle):
#     def __init__(self,side_length):
#         super().__init__(side_length,side_length)

        
    
# rectangle = Rectangle(5,4) 
# square =  Square(5)
# print(rectangle.area()) 
# print(square.area()) 

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def speak(self) :
        print(f"{self.name} make sound ") 

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age) 
        self.breed = breed

    def speak(self):
        a =  super().speak()  
        print(f"{self.name} says bark")  
        

dog = Dog("buddy",23,"bull dog")  

print(dog.speak())
    

         

  
   





    
            
      
    

