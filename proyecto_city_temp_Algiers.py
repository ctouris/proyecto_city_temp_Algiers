import mysql.connector

mydb = mysql.connector.connect(host='127.0.0.1', user='root', database='phpmyadmin')

mycursor = mydb.cursor()


def programa_city_temp():
    print('\n')
    print('***Bienvenido, este es un programa para saber la temperatura promedio para un día a elección del año 1995 '
          'hasta el año 2000 en la ciudad de Algiers, Algeria...***')
    print('\n')
    dia = input('Por favor ingrese un dia: ')
    mes = input('Ahora ingrese un mes: ')
    año = input('Ingrese un año, 1995 al 2000 inclusive: ')
    ciudad = 'Algiers'
    print('\n')
    sql = (
            'SELECT day, month, year, city, avgtemperature FROM schema_proyecto_guille.algiers2 WHERE day = (%s) '
            'AND month = (%s) AND year = (%s) AND city = ("%s")' % (
                dia, mes, año, ciudad))
    print(sql)
    print('\n')
    mycursor.execute(sql)

    for i in mycursor:
        print(i)
        dia2 = i[0]
        mes2 = i[1]
        año2 = i[2]
        ciudad2 = i[3]
        avgtemp = i[4]
        print('*' * 101)
        print(
            f'La temperatura promedio en la ciudad de {ciudad2} para la fecha: {dia2}/{mes2}/{año2}, es de  {avgtemp} grados Farenheit')
        print('*' * 101)


programa_city_temp()
