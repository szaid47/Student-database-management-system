import pymysql
from tkinter import messagebox




def connect_database():
    global mycursor, conn
    try:
        conn = pymysql.connect(host='localhost', user='root', password='1234')
        mycursor = conn.cursor()
    except:
        messagebox.showerror('Error', 'Something went wrong, please open MySQL app before running')
        return
    mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
    mycursor.execute('USE employee_data')
    mycursor.execute('''CREATE TABLE IF NOT EXISTS data (
                        id VARCHAR(20),
                        name VARCHAR(20),
                        phone VARCHAR(20),
                        role VARCHAR(50),
                        gender VARCHAR(50),
                        salary DECIMAL(10,2),
                        dept_id varchar(20),
                        FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
                        )''')
    mycursor.execute('CREATE TABLE IF NOT EXISTS departments (dept_id VARCHAR(20),dept_name varchar(50)) ')



def insert(id, name, phone, role, gender, salary,dept_id):
    mycursor.execute('INSERT INTO data VALUES (%s, %s, %s, %s, %s, %s,%s)', (id, name, phone, role, gender, salary,dept_id))
    conn.commit()

def id_exists(id):
    mycursor.execute('SELECT COUNT(*) FROM data WHERE id=%s',id)
    result=mycursor.fetchone()
    return result[0]>0


def fetch_employees():
    mycursor.execute('SELECT * from data')
    result=mycursor.fetchall()
    return result

def update(id,new_name,new_phone,new_role,new_gender,new_salary,new_dept):
    mycursor.execute('UPDATE data SET name=%s,phone=%s,role=%s,gender=%s,salary=%s,dept_id=%s WHERE id=%s',(new_name,new_phone,new_role,new_gender,new_salary,new_dept,id))
    conn.commit()

def delete(id):
    mycursor.execute('DELETE FROM data WHERE id = %s ',id)
    conn.commit()

def search(option,value):
    mycursor.execute(f'SELECt * FROM data WHERE {option}=%s',value)
    result=mycursor.fetchall()
    return result

def deleteall():
    mycursor.execute('TRUNCATE TABLE data')
    conn.commit()


#department

def dept_delete(id):
    mycursor.execute('DELETE FROM departments WHERE dept_id = %s ',id)
    conn.commit()

def dept_insert(id,name):
    mycursor.execute('INSERT INTO departments VALUES (%s, %s)', (id, name))
    conn.commit()

def dept_id_exists(id):
    mycursor.execute('SELECT COUNT(*) FROM departments WHERE dept_id=%s',id)
    result=mycursor.fetchone()
    return result[0]>0


def fetch_departments():
    mycursor.execute('SELECT * from departments')
    result=mycursor.fetchall()
    return result

def update_dept(id,new_name):
    mycursor.execute('UPDATE departments SET dept_name=%s WHERE dept_id=%s',(new_name,id))
    conn.commit()

def search_dept(option,value):
    mycursor.execute(f'SELECt * FROM departments WHERE {option}=%s',value)
    result=mycursor.fetchall()
    return result

def delete_all():
    mycursor.execute('TRUNCATE TABLE departments')
    conn.commit()


connect_database()