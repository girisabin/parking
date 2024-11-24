import sqlite3

conn = sqlite3.connect("test1.db")

mycursor = conn.cursor()
def create_query():
    mycursor.execute('''
        Create table if not exists users(
                  id integer primary key,
                  username text not null,
                 age integer,
                  email text unique
                  )

    ''')
    conn.commit()
    conn.close()

def insert_query() :
    mycursor.execute("insert into users (username, age,email) values ('alice',30,'alice@gmail.com') ")
    conn.commit()
    conn.close()

def update_query():
    mycursor.execute("update users set age = 31 where username = 'alice' ")
    conn.commit()
    conn.close()


def delete_query():
    mycursor.execute("delete from users where username = 'alice'")
    conn.commit()
    conn.close()    


    
