import sqlite3

conn = sqlite3.connect("test2.db")

mycursor = conn.cursor()

mycursor.execute('''
        Create table if not exists two_wheeler(
                  id integer primary key,
                  name text not null,
                 vehicle_type text not null,
                  vehicle_no text not null
                  )

    ''')

conn.commit()


mycursor.execute('''
        Create table if not exists four_wheeler(
                  id integer primary key,
                  name text not null,
                 vehicle_type text not null,
                  vehicle_no text not null
                  )

    ''')

conn.commit()


import csv

def insert_2wheeler():
    
    file_path = "data2.csv"
    with open(file_path,mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        # for row in csv_reader:
        #     if row[1]=="two_wheeler":
        #         print(tuple(row))
        
        data = [tuple(row) for row in csv_reader if row[1]=="two_wheeler"]
        # print(data)
     
    
    mycursor.executemany("insert into two_wheeler (name,vehicle_type,vehicle_no) values (?,?,?)",data) 
    conn.commit()
    
def insert_4wheeler():
    
    file_path = "data2.csv"
    with open(file_path,mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        # for row in csv_reader:
        #     if row[1]=="two_wheeler":
        #         print(tuple(row))
        
        data1 = [tuple(row) for row in csv_reader if row[1]=="four_wheeler"]
        # print(data1)
     
    
    mycursor.executemany("insert into four_wheeler (name,vehicle_type,vehicle_no) values (?,?,?)",data1) 
    conn.commit()
    conn.close()