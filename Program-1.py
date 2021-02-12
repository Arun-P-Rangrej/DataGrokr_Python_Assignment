
import mysql.connector as mysql
db = mysql.connect(
host = "localhost",
user = "arun",
passwd = "root",
database = "employees"
)
cursor = db.cursor()

def fetch_table_names_using_generator():
    query = "SHOW TABLES"
    # Execute your MySQL query
    cursor.execute(query)
    # Iterate through fetchall(), but yield the row
    for row in cursor.fetchall():
        yield row 

def fetch_employees_table_values_using_generator():
    query = "SELECT * FROM employees"
    # Execute your MySQL query
    cursor.execute(query)
    # Iterate through fetchall(), but yield the row
    for row in cursor.fetchall():
        yield row 

def main():
    #iterate through all with a for loop to get list of all tables inside employees database
    for row in fetch_table_names_using_generator():
        print(row)
    #iterate through all with a for loop to get list of all values of employee table  
    for row in fetch_employees_table_values_using_generator():
        print(row)


if '__main__' == __name__:
    main()
