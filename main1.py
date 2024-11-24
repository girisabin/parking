import dbhelper1
print("enter 1 for insert data for two_wheeler and 2 for four_wheeler")
option = int(input("Enter your option:"))
if option == 1:
    dbhelper1.insert_2wheeler()

elif option == 2:
    dbhelper1.insert_4wheeler()

else:
    print("Invalid input!!! Try right input...")