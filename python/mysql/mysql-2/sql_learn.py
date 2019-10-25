import pymysql

mydb = pymysql.connect(
	host = 'localhost',
	user = 'root',
	password = 'Password',
	database = 'test_database')

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE test_database")

# mydb.commit()

# mycursor.execute("SHOW DATABASES;")

# for i in mycursor:
# 	print(i)

# mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")


#### Insert

# sqlFormula = "INSERT INTO students (name, age) VALUES ('Mike', 17)"
# mycursor.execute(sqlFormula)

# sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
# student1 = ("Rachel", 21)
# mycursor.execute(sqlFormula, student1)
# mydb.commit()


# sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
# students = [("Bob", 22),
# 			("Jacob",18)]

# mycursor.executemany(sqlFormula, students)
# mydb.commit()

#### select 

# mycursor.execute("SELECT age FROM students")

# myresult = mycursor.fetchall()
# for r in myresult:
# 	print(r)

# myresult = mycursor.fetchone()
# for r in myresult:
# 	print(r)


#### where 

# sql = "SELECT * FROM students WHERE age = 18"
# sql = "SELECT * FROM students WHERE name LIKE 'Mi%'"
# sql = "SELECT * FROM students WHERE name =%s and age = %s"
# mycursor.execute(sql,('Mike',18))


# # mycursor.execute(sql)
# myresult = mycursor.fetchall()

# for r in myresult:
# 	print(r)


#### order

# sql = "SELECT * FROM students ORDER BY age DESC"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for r in myresult:
# 	print(r)

# sql = "UPDATE students SET age = 13 WHERE name = 'Mike'"
# mycursor.execute(sql)
# mydb.commit()


# sql = "SELECT * FROM students LIMIT 2"




#### Destroy

# sql = "DELETE FROM students WHERE name  = 'Mike' and age = 17"

# sql = "DROP TABLE IF EXISTS students"

# sql = "DROP DATABASE testdb"

# mycursor.execute(sql)
# mydb.commit()















