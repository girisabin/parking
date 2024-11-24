# define class
# class myclass:
#     x = 5

# # calling the object
# o1 = myclass()
# print(o1.x)    

# class Person:
#     def __init__(self, name, age ):
#         self.name = name
#         self.age = age

#     def myfunc(self):
#         print("Hello my name is " + self.name) 

# p1 = Person("Tom",25) 
# p1.myfunc()  

# p2 = Person("abc",22)
# p2.myfunc()

# Types of Inheritance
# single inheritance

# class Animal:
#     def speak(self,a):
#         return "Animal speaks", a
    
# class Dog(Animal):
#     def bark(Self):
#         return "Dogs barks" 

# n = 5    
# my_dog = Dog()    
# print(my_dog.speak(n))
# print(my_dog.bark())

# class A:
#     def method_A(self):
#         return "Method A"
    
# class B:
#     def method_B(self):
#         return "Method B"    
    
# class C(A,B):
#     def method_C(self):
#         return "Method C" 
    
    

# x = 3    
# obj_c = C()    
# print(obj_c.method_A())
# print(obj_c.method_B())
# print(obj_c.method_C())

# class A:
#     def method_A(self):
#         return "Method A"
    
# class B(A):
#     def method_B(self):
#         return "Method B" 

#     def method_A(Self):
#         return "This is A"  
    
# class C(B):
#     def method_C(self):
#         return "Method C" 
    
    

   
# obj_c = C()    
# print(obj_c.method_A())
# print(obj_c.method_B())
# print(obj_c.method_C())

# super()

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
# square = Square(4)

# print("The area of rectangle is ",rectangle.area())
# print("The area of square is ", square.area())

# Abstraction and access specifiers
# -> hides the details of class and objects

# from abc import ABC, abstractmethod

# class Animal(ABC):

#     @abstractmethod

#     def make_sound(self):
#         pass            # no implementation here, subclass must implement this

# class Dog(Animal):

#     def make_sound(self):
#         return "Woof!!!"
    
# dog = Dog()
# print(dog.make_sound())    

# from abc import ABC, abstractmethod

# class Animal(ABC):

  

#     def make_sound(self):
#         return "Woof!!!"           # no implementation here, subclass must implement this

# class Dog(Animal):

#     pass
    
# dog = Dog()
# print(dog.make_sound())


# Polymorphism -> using same function in different way.

# class name calculator
# addition # subtraction
#division   # division

# class Calculator:

#     def __init__(self,n1,n2):
#         self.n1 = n1
#         self.n2 = n2
        

#     def add(self):
#         return self.n1 +self.n2

#     def sub(self) :
#         return self.n1 - self.n2  

#     def div(self) :
#         return self.n1 / self.n2   

#     def mul(self) :
#         return self.n1 * self.n2

# obj = Calculator(4,2)
# print(obj.add())
# print(obj.sub())
# print(obj.div())
# print(obj.mul())


# class Vehicle:
#     def __init__(self,brand,model,color):
#         self.brand = brand
#         self.model = model
#         self.color = color

# class Car(Vehicle):
#     def __init__(self, brand, model, color):
#         super().__init__(brand, model, color)

#     def open_door(self):
#         print(f"{self.brand} auto opens door")

#     def close_door(self):
#         print(f"{self.brand} auto close door") 

# class Motorbike(Vehicle):
#     def __init__(self, brand, model, color):
#         super().__init__(brand, model, color)

#     def starts(self):
#         print(f"{self.brand}  can start")  

#     def breaks(self):

#         print(f"{self.brand} have a breaks") 

# obj = Motorbike("BMW",2,"White") 
# obj1 = Car("Farari",5,"Yellow")

# print(obj.breaks())
# print(obj.starts())
# print(obj1.close_door())
# print(obj1.open_door())

# def divide(x,y):
#     try:
#         result = x/y

#     except ZeroDivisionError:
#         print("Error:Division by zero")

#     except TypeError as error:
#         print(f"Error:{error}")   

#     else:
#         print(f"Result: {result}")

#     finally:
#         print("Final block executed")

# divide(10,2) 
# divide(2,0)
# divide(2,'a')   


# try : 
#     x = -1
#     if x< 0 :
#         raise Exception("Sorry, no numbers below zero")

# except Exception as e:
#     print("e",e)   
#     print("this is exception")

# finally:
#     print("ending the program")


# class mycustomererror(Exception) :
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)

# try: 
#     x = -1

#     if x < 0:
#         raise mycustomererror("custom error")

# except mycustomererror as e:
#     print("e",e) 
#     print("this is exception") 

# finally:
#     print("Final block executed")  
#         

# import traceback

# def divide(x,y):
#     try:
#         result1 = x+y
#         result2 = x-y
#         result = x / y

#     except Exception as e:
#         print(f"General Exception{e}" )  
#         traceback.print_exc()  


# divide(1,0)  

# import traceback
 
# dict1 = {
#     "name" : "abc" ,
#     "address" : "ktm"
# }

# print("get the details")
# print("enter 1 for name \n 2 for address \n 3 for email")
# num = int(input("Enter the number: ") )
# if num == 1:
#     print(dict1["name"])

# if num == 2:
#     print(dict1["address"])  

# if num == 3:
#     try:
#         print(dict1["email"])
#     except Exception as e:
#         print(e)
#         print("This is exception!!!")
#         traceback.print_exc() 
#         dict1["email"]  = input("enter the email") 
#         print("email enterd")   
#         print(dict1["email"])     

# print(dict1)


# try:
#     result = dict1["email"]

# except Exception as e:
#     print("e",e) 
#     print("This is exception!!!") 
#     dict1 ["email"] = "john@gmail.com"
#     print("append dict1",dict1)
   
# print("email", dict1["email"])


    





            
            

       






