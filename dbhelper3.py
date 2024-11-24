import datetime
print("Vehicle Parking System")



import sqlite3

conn = sqlite3.connect("test3.db")

mycursor = conn.cursor()

def create_query():
    mycursor.execute('''
                   Create table if not exists all_details(
                  id integer primary key,
                  username text not null,
                 vehicle_type text not null,
                  vehicle_no text not null,
                     starting_time date,
                     end_time date,
                     total_price float null
                  )

    
                 ''')
    conn.commit()
    


def insert_query():

    username = input("Enter your name: ")
    while True:
        print("""Enter the vehicle type
            1. Two Wheeler
            2.Four Wheeler""")
        vehicle_type_option = int(input("Enter your vehicle type:"))
        if vehicle_type_option == 1:
            vehicle_type = "Two Wheeler"
            break
        elif vehicle_type_option == 2:
            vehicle_type = "Four Wheeler"
            break
        else:
            print("Invalid option choosed")
    parking_start_time= datetime.datetime.now()
    vehicle_no = input("Enter your vehicle number:")
    details = (username,vehicle_type,vehicle_no,parking_start_time)

    mycursor.execute("insert into all_details(username,vehicle_type,vehicle_no,starting_time) values(?,?,?,?)",details)
    conn.commit()
    mycursor.execute(f"select * from all_details where vehicle_no == (?)",(vehicle_no,))
    rows = mycursor.fetchall()[0]
    print("Your slips")
   
    # for row in rows:
    #     with open(rows[3]+".txt",mode="w") as file:
    #         file.write(f"id: {rows[0]}\n")
    #         file.write(f"username: {rows[1]}\n")
    #         file.write(f"vehicle_type: {rows[2]}\n")
    #         file.write(f"starting_time: {rows[4]}\n")
    #This is for slip
    
    with open(rows[3]+".txt",mode="w") as file:
        file.write(f"id: {rows[0]}\n")
        file.write(f"username: {rows[1]}\n")
        file.write(f"vehicle_type: {rows[2]}\n")
        file.write(f"starting_time: {rows[4]}\n")

    # mycursor.execute("ALTER TABLE all_details add end_time")
    # conn.commit()
    # mycursor.execute("ALTER TABLE all_details add total_price")
    # conn.commit()
    

def show_all():
    mycursor.execute("select * from all_details")

    rows = mycursor.fetchall()
    print("All records")
    print("(id|username|vehicle_type|vehicle_no|starting_time)")
    for row in rows:
        print(row ,"\t")

def exit_parkinglot():
  
    ending_time = datetime.datetime.now()

    id  = int(input("Enter your id:"))
    mycursor.execute('update all_details set end_time = (?) where id = (?)',(ending_time,id))
    conn.commit()
    mycursor.execute("select starting_time from all_details where id = (?)",(id,))

    rows = mycursor.fetchall()
    startingtime= rows[0][0]
    format = '%Y-%m-%d %H:%M:%S.%f'
    start_time = datetime.datetime.strptime(startingtime,format)
    time_interval = ending_time - start_time
    print(time_interval)
    
    time_interval1 = str(time_interval)
    
    time_interval1 = time_interval1.split(':')
    print(time_interval1)
    hrs1=int(time_interval1[0])
    min1 = int(time_interval1[1])
    print(hrs1,min1)
    

    # time_interval = time_interval.split()



    # print(type(start_time))
    

    


    
    # difference = ending_time - 

    
    # hours_difference = difference.total_seconds() / 3600

    # print(f"The difference in hours is: {hours_difference} hours")


    










           