# import module
# module.greeting("abc")

# import package.module2 as mod

# mod.sum(1,2)

# import calculator
# from calculator import sum as add , diff as sub

# value = add(4,6)
# value = sub(5,4)


# from calculator import person
# value = person["name"]
# print(value)

# def decorator1(fun):
#     def wrapper():
#         print("something before function runs")
#         fun()
#         print("something after the function runs")

#     return wrapper

# @decorator1
# def say_hello():
#     print("hello") 

# say_hello()  

# @decorator1
# def say_hi():
#     print("hi")
# say_hi()    

# def decorator1(fun):
#     def wrapper(*args,**kwargs):
#         print("something before function run") 
#         fun(*args,**kwargs)
#         print("something after the function runs") 
#     return wrapper    

# @decorator1
# def say_hello(a,b):
#     print("hello",a,b)

# say_hello(1,2)

# def greet_decorator(greetings):
#     def decorator1(fun):
#         def wrapper(*args,**kwargs):
#             print(f"{greetings} before function run") 
#             fun(*args,**kwargs)
#             print("something after the function runs") 
#         return wrapper 
#     return decorator1   

# @greet_decorator("hello")
# def say_hello(a,b):
#     print("a and b",a,b)

# say_hello(1,2)

def greet_decorator(greetings,bye):
    def decorator1(fun):
        def wrapper(*args,**kwargs):
            print(f"{greetings} before function run") 
            fun(*args,**kwargs)
            print(f"{bye} after the function runs") 
        return wrapper 
    return decorator1   

@greet_decorator("hello","bye")
def say_hello(a,b):
    print("a and b",a,b)

say_hello(1,2)

