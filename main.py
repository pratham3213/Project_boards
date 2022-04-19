from time import time
from mysql.connector import *


def dbms(password):
    con=connect(host="localhost",user="root",passwd=password)
    cur=con.cursor()

def main():
    choice=int(input("""Welcome to the Medical Database Management System
    
    Choose between 1-6
    1.To Manage Medicinal Database"""))
    password=input("Please enter the password of Mysql Server:- ")
    if choice==1:
        print("Connecting to Database...")
        time.sleep(3)
        dbms(password)
