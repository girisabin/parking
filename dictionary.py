# key must be unique.
# empty dictionary = {}

#dict with initial values

# my_dict = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }
# print(my_dict)

# # print(my_dict["address"])
# print(my_dict.get("address"),1)
# x= my_dict.keys()
# print(x)


#Dict with mixed_values

# my_dict1 = {
#     1: "one",
#     2: "two",
#     (1,2): "tuple"
# }
# print(my_dict1[1,2])
# print(my_dict1.get((1,2)))

# add a new item to the original dictionary

# car = {
#     "brand": "Ford",
#     "model" : "Mustang",
#     "year" : 1964
# }

# x= car.keys()

# car["color"] = "White"
# car["year"]  = 1965
# print(x)
# print(car)
# y = car.values() 
# print(y)

#Using items()
# z = car.items()
# print(z)

# for k,v in car.items():
#     print("keys",k)
#     print("values",v)

# update()
# car.update({"year" : 2020})
# print(car)

#in pop() we use key of the values. 

# car.pop("year")
# print(car)

# using popitem -> remove the last key and value.

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)

# copy()
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)

# nested dictionary

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# print(myfamily["child1"]["name"])
# # myfamily.update({"child1" : {"name" : "John"}})
# # print(myfamily)
# myfamily["child1"]["name"]= "kala"
# print(myfamily)

# print(myfamily.get("child1").get("name"))

college = {
    "student1":{
        "name":"abc",
        "score" : [1,2,3,4]
    },
    "student2":{
        "name": "cde",
        "score" : [5,6,7,8,9]
    }
}
#output
#student1 score : 10
#student2 score : 35
sum_score = 0
for k,v in college.items():
    sum_score = sum(v.get("score"))
    print(f"{k} score : {sum_score}")
    
    
    # for i in v["score"]:
    #     sum_score =sum_score + i
    # print(sum_score)    









    
    

    
       



            
        
    
        
   


    



    
    



