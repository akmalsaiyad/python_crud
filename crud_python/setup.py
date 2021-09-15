import sqlite3 as lit

def create_tbl(db):
    try:
        cur = db.cursor()
        tablequery = "CREATE TABLE student (id INT AUTOINCREMENT, name TEXT, class INT, phone TEXT, email TEXT)"
        cur.execute(tablequery) 
        print('table created')
    except lit.Error as e:
        print('Unable to create table :',e)

def main():
    try:
        db = lit.connect('students.db')
        print('database created :',db)
        create_tbl(db)

    except:
        print('failed to create database')

if __name__ == '__main__':
    main()