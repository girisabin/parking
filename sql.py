# import sqlite3

# conn = sqlite3.connect("test.db")

# mycursor = conn.cursor()
# mycursor.execute('''
#                 Create table if not exists users(
#                  id integer primary key,
#                  username text not null,
#                  age integer,
#                  email text unique
#                  )
# '''
    
# )

# mycursor.execute("insert into users (username, age,email) values ('alice',30,'alice@gmail.com') ")
# conn.commit()

# users= [
#     ('Bob',25,'bob@gmail.com'),
#     ('Charlie',20,'charlie@gmail.com')
# ]

# mycursor.executemany("insert into users (username,age,email) values (?,?,?)",users)
# conn.commit()

# mycursor.execute("select * from users")

# rows = mycursor.fetchall()
# print("All records")

# for row in rows:
#     print(row)
# print(type(row))

# mycursor.execute("update users set age = 31 where username = 'alice' ")
# conn.commit()

# mycursor.execute("delete from users where username = 'Bob'")
# conn.commit()

import sqlite3

conn = sqlite3.connect("test.db")

mycursor = conn.cursor()

import csv

data = []

file_path = "data1.csv"

with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
   
    header = next(csv_reader)
    
    data = [tuple(row) for row in csv_reader]
    # for row in csv_reader:
    #     data.extend(tuple(row))

    
    

users = data
print(users)

mycursor.executemany("insert into users (username,age,email) values (?,?,?)",users) 
conn.commit()    

# import csv        
# csv_data = """username,age,email
# Tom,23,tom@gmail.com
# Jack,25,jack@gmail.com
# Johnny,24,johnny@gmail.com
# Jake,30,jake@gmail.com
# lilly,29,lilly@gmail.com
# Rae,28,rae@gmail.com
# Cris,27,cris@gmail.com"""

# # Using csv.reader to read the data and convert it into a list of tuples
# csv_reader = csv.reader(csv_data.splitlines())
# header = next(csv_reader)  # Skip the header row

# # Convert each row to a tuple
# data = [tuple(row) for row in csv_reader]

# # Print the result
# print(data)