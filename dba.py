import pymysql 

conn = pymysql.connect(host="localhost",user="root",passwd="",db="my_python")
myCursor = conn.cursor() #RECORDAR QUE ESTE ASIGNACION DEBE ESTAR ALINEADO AL myCursor.execute  

#PARA CREAR LA TABLA
#myCursor.execute("""CREATE TABLE names
#(
#id int primary key,
#name varchar(20)
#)
#""")
#print ("tabla creada")

PARA INSERTAR UN REGISTRO
myCursor.execute("INSERT INTO names (id,name) VALUES (1,'Juan');" )
print ("Dato insertado")

#PARA ELIMINAR UN REGISTRO
myCursor.execute("DELETE FROM names WHERE id=1;" )
print ("Dato eliminado")

#PARA ACTUALIZAR UN REGISTRO
#myCursor.execute("UPDATE names SET name='Miguel' WHERE id=2 ;" )
#print ("Dato actualizado")

#PROCEDIMIENTOS PARA EJECUTAR TOD0
conn.commit()
conn.close()


#PARA CORREGIR
'''
if a == 1:
    #print("id")
    #id=int(input())
    print("name")
    name=str(input())

    myCursor = conn.cursor()
    myCursor.execute("INSERT INTO names (id,name) VALUES  (5,"+name+");" )
    print ("Dato insertado")
'''