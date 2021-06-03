import sqlite3

conn = sqlite3.connect ("productos.sqlite")

cursor = conn.cursor()

# ~ cursor.execute ("CREATE TABLE productos (id NUMERIC, nombre TEXT, precio NUMERIC)")

# ~ cursor.execute ("CREATE TABLE productos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, precio NUMERIC)")

#UNICAMENTE SELECCIONAR 1

productos_var = (( 1, "teclado", 500),
                 ( 2, "mouse", 200),
                 (3, "monitor", 1000),
                 (4, "parlantes", 400))
                 
while True:
    try:
        id_ingreso = int( input ("ingrese el id: "))                 
        nombre_ingreso = input("ingrese el nombre del producto nombre: ")
        Precio_ingreso = int( input ("ingrese el precio: "))
        
        cursor.execute ("SELECT * FROM productos")
        productos_var = cursor.fetchall()
        print(productos_var)
                   
    except Exception:
        print ("Recuerde que tanto ID como Precio deben ser nunmeros")        
    
        
for id, nombre, precio in productos_var:
    cursor.execute ("INSERT INTO productos VALUES ( ?, ?, ?)", (id, nombre, precio))

conn.commit ()



conn.close()
