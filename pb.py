from mysql.connector import *

def med_db(passwd_mysql,user_mysql="root"):
	con=connect(host="localhost",user=user_mysql,passwd=passwd_mysql)
	cur_object=con.cursor()
	cur_object.execute("CREATE DATABASE IF NOT EXISTS Medical_Store;")
	cur_object.execute("USE Medical_Store;")
	ch="y"
	while ch=="y" or ch=="yes":
		choice=int(input("""Choose Between 1-5
		1.To Create a Table
		2.To Add Data in table
		3.To Delete Data from table
		4.To Modify Data in the table
		5.Exit"""))
		if choice==1:
			cur_object.execute("CREATE TABLE Medicines(ID varchar(100), Name varchar(200), Place varchar(),Quantity int(50),PRIMARY KEY(ID));")
			print("Medicine table have been created with Fields ID, Name, Place, Quantity.")
		elif choice==2:
			ID=input("Enter the ID her:- ")
			Name=input("Enter the name of Medicine:- ")
			Place=input(f"Enter the Place where {ID} has been placed:- ")
			Quantity=input(f"Enter the Quantity of {ID}:- ")
			cur_object.execute(f"INSERT INTO Medicines VALUES({ID},{Name},{Place},{Quantity});")
			print("Your Credentials have been inserted in the table Medicines")
		elif choice==3:
			ID=input("Enter the ID you wanna Delete:- ")
			cur_object.execute(f"DELETE FROM Medicines WHERE ID={ID};")
			print(f"Data of {ID} has been deleted")
		elif choice==4:
			modify=input("Enter the Data you need to update:- ")
			modify1=input("Enter the Field of Data According to Table:- ")
			Id=input("Enter the ID with which Data is associated:- ")
			cur_object.execute(f"UPDATE Medicines SET {modify1}={modify} WHERE ID={Id};")
			print("Your Data has been modified")
		elif choice==5:
			break
		ch=ianput("Do you wanna continue?\n:-")
	con.close()

def sp_med_db(passwd_mysql,user_mysql="root"):
	con=connect(host="localhost",user=user_mysql,passwd=passwd_mysql)
	cur_object=con.cursor()
	s_db=cur.
	if s_db!="Medical_Store":
		cur_object.execute("USE Medical_Store;")
	ch="y"
	while ch=="y" or ch=="yes":
		medicine=input("Enter the ID of Medicine:- ")

		ch=input("Do you wanna continue?\n:-")
	con.close()

def main():
	user_mysql=input("Welcome to the Medical Store Managent System\n\nEnter your Mysql User name (Leave blanck if you don't know): ")
	passwd_mysql=input("Enter your Mysql Password (Leave blanck if you don't know): ")
	choice=int(input("""Please Choose Between 1-7
	1.To manage database of all the medicines available in the store
	2.To manage any specific medicine's available quantity
	3.To manage any specific medicine's location in store
	4.To manage the suppliers of a specific medicine
	5.To Generate a bill for the customer
	6.To Manage Database of Employees and Customers
	7.Exit
	
	Your Choice:-"""))

	if choice==1:
		med_db(passwd_mysql,user_mysql)
	elif choice==2:

main()
