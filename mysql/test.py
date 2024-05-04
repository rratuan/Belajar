import mysql.connector

# konek ke server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Hilapdeui13",
    database="testdb"
)

# function
def show(param):
    mycursor.execute(param)
    for sh in mycursor:
        print(sh)

def display(var):
    for row in var:
        print(row)
    print("")


mycursor = mydb.cursor()
# show("SHOW DATABASES")


# CREAT DATABASE
# mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")
# show("SHOW TABLES")


# CREATE TABLE AND INSERT DATA TO TABLE
sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
# student = ("Ratu", 19)
# mycursor.execute(sqlFormula, student)
# mydb.commit()

# students = [
#             ("Ayu", 19),
#             ("Nur", 19),
#             ("Fajar", 19)
#         ]
# mycursor.executemany(sqlFormula, students)
# mydb.commit()


# SELECTING AND GETTING DATA
# mycursor.execute("SELECT * FROM students")
# # ngambil semua data
# result = mycursor.fetchall()
# # menampilkan hasil dari pengambilan data
# display(result)

# mycursor.execute("SELECT name FROM students")
# # mengambil data nama
# name = mycursor.fetchall()
# # menampilkan nama
# display(name)

# mycursor.execute("SELECT age FROM students")
# # mengambil data pertama dari age
# age = mycursor.fetchone()
# # menampilkan data age
# # display(age)


# # Jika ada hasil, baca hasilnya
# if mycursor.rowcount > 0:
#     mycursor.fetchall()


# CONDITIONS WITH WHERE AND WILDCARD
# # mengambil dan menampilkan data nama 'fajar'
# mycursor.execute("SELECT * FROM students WHERE name='Fajar'")
# result = mycursor.fetchall()
# display(result)

# mengambil dan menampilkan data nama dengan awalan 'Ra' (WILDCARD)
# mycursor.execute("SELECT * FROM students WHERE name LIKE 'Ra%'")
# result = mycursor.fetchall()
# display(result)

# mengambil dan menampilakn data nama dengan sisipan 'aja' (WILDCARD)
# mycursor.execute("SELECT * FROM students WHERE name LIKE '%aja%'")
# result = mycursor.fetchall()
# display(result)

# mengambil dan menampilkan data nama dengan akhiran 'u' (WILDCARD)
# mycursor.execute("SELECT * FROM students WHERE name LIKE '%u'")
# result = mycursor.fetchall()
# display(result)


# UPDATING ENTRIES AND LIMITING QUERIES
# update data
# mycursor.execute("UPDATE students SET age=20 WHERE name='Ayu'")
# mydb.commit()

# menampilkan n data pertama
# mycursor.execute("SELECT * FROM students LIMIT 4")
# result = mycursor.fetchall()
# display(result)

# menampilkan n data pertama setelah m data 
# mycursor.execute("SELECT * FROM students LIMIT 4 OFFSET 2")
# result = mycursor.fetchall()
# display(result)


# ORDERING QUERIES AND RESULT
# mengurutkan dari nilai terbesar ke nilai terkecil berdasarkan umur
# mycursor.execute("SELECT * FROM students ORDER BY age DESC")
# result = mycursor.fetchall()
# display(result)


# DELETE ENTRIES
mycursor.execute("SELECT * FROM students DELETE nama='Ayu'")
result = mycursor.fetchall()
display(result)
