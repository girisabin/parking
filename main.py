import dbhelper

print("Enter 1 for create table \n enter 2 for insert \n enter 3 for delete  \n enter 4 for update" )

option = int(input("Enter the option:"))

if option==1:
    dbhelper.create_query()

if option==2:
    dbhelper.insert_query()

if option==3:
    dbhelper.delete_query()  

if option==4:
    dbhelper.update_query()      




