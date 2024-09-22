# MySQL Connector Module
import mysql.connector

# Connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="Cats"
)

# Cursor
cursor = connection.cursor()

# DDL Statements
cursor.execute("CREATE DATABASE IF NOT EXISTS Cats")
cursor.execute("USE Cats")
cursor.execute("CREATE TABLE IF NOT EXISTS Cats (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(20) NOT NULL, age INTEGER NOT NULL)")

# DML Statements
# Create
cursor.execute("INSERT INTO Cats (id, name, age) VALUES (null, 'Tadoe', 10), (null, 'Bubs', 11), (null, 'Leon', 5);")
connection.commit()

# Read
cursor.execute("SELECT * FROM Cats WHERE id = 20")
print(cursor.fetchall())

# Update
cursor.execute("UPDATE Cats SET name = 'Tonto' WHERE id = 20;")
cursor.execute("UPDATE Cats SET name = 'Tonto' WHERE id = %s;", (20,))
connection.commit()

# Delete
cursor.execute("DELETE FROM Cats WHERE id = 34;")
connection.commit()

# Closing Resources
cursor.close()
connection.close()