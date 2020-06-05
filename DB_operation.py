import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="pizzadb"
)

cursor = mydb.cursor()

def sent_DB(size, dough_type, toppings):
	global cursor, mydb
	#inserting data to database from GUI form
	sql_form = "INSERT INTO orders (size, type, toppings) VALUES (%s, %s, %s)"
	value = (size, dough_type, toppings)
	cursor.execute(sql_form, value)

	mydb.commit()
	
print(cursor)