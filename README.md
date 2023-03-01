# proyecto_city_temp_Algiers
This is a Python program that connects to a MySQL Workbench database using XAMPP and retrieves the average temperature for a specific day, month, year, and city. 
This dataset was downloaded from Kaggle.

The program prompts the user to input the day, month, year, and city, and then uses these values to construct a SQL query to retrieve the data. The retrieved data is then printed to the console in a formatted manner.

Here is a brief explanation of what each line of the code does:

import mysql.connector #imports the mysql.connector module to allow Python to interact with a MySQL database.

mydb = mysql.connector.connect(host='127.0.0.1',user='root', database='phpmyadmin') #connects to a MySQL database with the specified host, 
user, and database name, and returns a connection object.

mycursor = mydb.cursor()# creates a cursor object from the connection object to execute SQL queries.

def programa_city_temp()# defines a function called programa_city_temp().

print('\n')# prints a new line character to the console.

print('***Bienvenido, este es un programa para saber la temperatura promedio para un día a elección del año 1995 hasta el año 2000 en 
la ciudad de Algiers, Algeria...***')#  prints a welcome message to the console.

dia = input('Por favor ingrese un dia: ')#  prompts the user to input a day value and assigns it to the variable dia.

mes = input('Ahora ingrese un mes: ')# prompts the user to input a month value and assigns it to the variable mes.

año = input('Ingrese un año, 1995 al 2000 inclusive: ')# prompts the user to input a year value between 1995 and 2000 inclusive, and 
ssigns it to the variable año.

ciudad = 'Algiers'#  assigns the string value 'Algiers' to the variable ciudad.

sql = ('SELECT day, month, year, city, avgtemperature FROM schema_proyecto_guille.algiers2 WHERE day = (%s) AND month = (%s) AND year = (%s)
AND city = ("%s")'%(dia, mes, año, ciudad))#  constructs a SQL query to retrieve the average temperature for the specified day, month, year, 
and city, and assigns it to the variable sql.

print(sql)#  prints the SQL query to the console.

mycursor.execute(sql)#  executes the SQL query using the cursor object.
for i in mycursor: ...#  loops through the rows returned by the SQL query and assigns the values to the variables dia2, mes2, año2, ciudad2, and avgtemp, which are then printed to the console in a formatted manner.

Overall, this program allows the user to retrieve the average temperature for a specific day, month, year, and city from a MySQL database.
