from os import system
import sqlite3 as lit 

def read(db):
    with db:
        cur = db.cursor()
        cur.execute('SELECT * FROM student')
        row = cur.fetchall()
        for data in row:
            print(data)

def add(db):
    cur = db.cursor()
    print('add details:')
    name = input('name:')
    class_ = int(input('class:'))
    phone = input('phone:')
    email = input('email:')
    tp = (name,class_,phone,email)
    cur.execute("INSERT INTO student(name,class,phone,email) VALUES(?,?,?,?)",tp)
    print('Record inserted')
    read(db)
    

def update(db):
    read(db)
    cur = db.cursor()
    user_id = int(input('Enter the id of the record you want to update: '))
    name = input('name:')
    class_ = int(input('class:'))
    phone = input('phone:')
    email = input('email:')
    tp = (name,class_,phone,email,user_id)
    cur.execute("UPDATE student SET name=?, class = ?, phone= ?, email=? WHERE id = ?",tp)
    print('Record updated')
    read(db)



def delete(db):
    with db:
        cur = db.cursor()
        read(db)
        user_id = int(input('Enter the id of the record you want to delete: '))

        cur.execute("DELETE FROM student WHERE id= ? ",(user_id,))
        print('Record deleted')
        read(db)

if __name__ == '__main__':
    db = lit.connect('students.db')
    gate = True
    while(gate):
        print('''Student CRUD operation:
                1 - Read
                2 - Add
                3 - Update
                4 - Delete
                5 - exit
                ''')
        option = int(input('Select option:'))
        system('cls')
        if option == 5 or (option>5 or option<1):
            gate = False
        else:
            if option==1:
                read(db)
            elif option ==2:
                add(db)
            elif option == 3:
                update(db)
            elif option == 4:
                delete(db)
    print('Task Ended')


