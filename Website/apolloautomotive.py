import mysql.connector

try:
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Demigod808!',
        port='3306',
        database='apolloautomotive',
    )
except:
    print("Error didnt connect properly")
mycursor = mydb.cursor()

mycursor.execute('Select * From Vehicle ')

vehicles = mycursor.fetchall()

for vehicles in vehicles:
    print(vehicles)

mycursor = mydb.cursor()

mycursor.execute('Select * From Customer ')

Customer = mycursor.fetchall()

for Customer in Customer:
    print(Customer)
