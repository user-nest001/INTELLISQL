import sqlite3

# Connect to sqlite
connection = sqlite3.connect("data.db")

# Create a cursor object
cursor = connection.cursor()

# Create the table
table_info = """
CREATE TABLE STUDENTS(
    NAME VARCHAR(25), 
    CLASS VARCHAR(25), 
    SECTION VARCHAR(25), 
    MARKS INT
);
"""
# Note: The prompt description mentioned 'Company' but the SQL snippet usually implies standard columns. 
# Based on your record insertion description, the columns are Name, Class, Marks, Company.
# Let's correct the CREATE statement to match your specific data insertion logic.

cursor.execute("DROP TABLE IF EXISTS STUDENTS") # Clean slate

table_schema = """
CREATE TABLE STUDENTS(
    NAME VARCHAR(25), 
    CLASS VARCHAR(25), 
    MARKS INT,
    COMPANY VARCHAR(25)
);
"""
cursor.execute(table_schema)

# Insert records
cursor.execute('''INSERT INTO STUDENTS VALUES('Sijo', 'BTech', 75, 'JSW')''')
cursor.execute('''INSERT INTO STUDENTS VALUES('Lijo', 'MTech', 69, 'TCS')''')
cursor.execute('''INSERT INTO STUDENTS VALUES('Rijo', 'BSc', 79, 'WIPRO')''')
cursor.execute('''INSERT INTO STUDENTS VALUES('Sibin', 'MSc', 89, 'INFOSYS')''')
cursor.execute('''INSERT INTO STUDENTS VALUES('Dilsha', 'MCom', 99, 'Cyient')''')

# Display data to verify
print("The inserted records are:")
data = cursor.execute('''SELECT * FROM STUDENTS''')
for row in data:
    print(row)

# Commit and close
connection.commit()
connection.close()
