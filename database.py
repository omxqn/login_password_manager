# pip install mysql-connector-python ,install mysql-connector-python==8.0.29
import mysql.connector
import datetime
import logging
global times
global date
import ast
from encryption import *
dateing = str(datetime.datetime.now().date())
timesss = str(datetime.datetime.now().time().strftime(f'%H:%M:%S'))
timesss = f'{timesss.split(":")[0] + "-" + timesss.split(":")[1] + "-" + timesss.split(":")[2]}'

def start():
    """
    start connection function with mysql database
    """

    global timesss
    global date
    global db
    global my_curser
    date = datetime.datetime.now().date()

    db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='test')
    my_curser = db.cursor()
    print("Database connected successfully")


def new_table(table_name, instractions):
    # Create new table
    """
    # view table descriptions
    my_curser.execute('DESCRIBE id_list')
    for i in my_curser:
        print(i)
    """
    try:
        # UNSIGNED there is no - or +
        # Example: instractions =  mention_ID int PRIMARY KEY AUTO_INCREMENT,name VARCHAR(50),id int(20) UNSIGNED,date VARCHAR(50),message VARCHAR(50)
        my_curser.execute(f'CREATE TABLE {table_name} ({instractions})')
        return "Table has been created successfully"
    except Exception:
        return 'This table is already existed'


def delete_all(table_name):
    """
    Delete all table information
    """
    my_curser.execute(f'DELETE FROM {table_name}')
    print("All data has been deleted")


def add_user(table, user_name,password,):
    global timesss
    try:
        password = create_hash(password)
        my_curser.execute(
            f'INSERT INTO {table} (user_name, password, created_date) VALUES {(user_name, password, str(date)+" "+str(timesss))}')
        print("committing")
        db.commit()
        print("Data saved successfully in database")
        print("succ")
    except:
        print("Error")


def create_hash(passwd):
    """
    convert password into hash string
    """
    while True:
        if check_key():
            print("Your key has been successfully imported \n\n")
            passwd = encrypting(passwd)
            break
        else:
            print("Master key missing")
            master_pass = input("Enter master password for hashing")
            new_master_key(master_pass)
    return passwd


def validate_password(username, passwd):
    while True:
        if check_key():
            print("Your key has been successfully imported \n\n")
            passwd = encrypting(passwd)

            data = get_user_info(username)
            username = data[0]
            hashed_password = data[1]
            if passwd == hashed_password:
                print(f"This password for {username} is valid")
                return True
            else:
                print("This password for {username} is not match")
                return False

        else:
            print("Master key missing")
            master_pass = input("Enter master password for hashing")
            new_master_key(master_pass)

def get_user_info(username):
    """
    getting username info from database
    """
    try:
        my_curser.execute(
            f'SELECT username,password,created_date FROM users WHERE (username =%s)' % username)
        x = []
        for i in my_curser:
            for g in i:
                x.append(g)
        s = x[2]
        return ast.literal_eval(s)

    except:
        print("Error while searching and getting users")
        return False


start()
if __name__ == "__main__":
    new_table("users",
              'user_ID int PRIMARY KEY AUTO_INCREMENT,username VARCHAR(300),password VARCHAR(600),created_date VARCHAR(300)')
    #print(add_new_booking(table='entertain_booking',user_id="11111",booking_type='d',booking_details="gfdgdfg",booking_time="10:22",finish_date="10/10/1001",name="ss",phone_number="33"))





    '''    f = open('database_cache.txt', 'w')
    f.write(str(my_curser))
    f.close()

    #print(get_table_info('sale_log', False))



    # table_columns('vid') '''
