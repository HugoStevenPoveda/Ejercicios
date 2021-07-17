#diccionario como base de datos  key nombre precio inventario 
#reto 1 camilo
productos ={
    '1':['Manzanas',6000.0,25],
    '2':['Limones',2500.0,15],
    '3':['Peras',2700.0,33],
    '4':['Arandanos',9300.0,34],
    '5':['Tomates',2100.0,42],
    '6':['Fresas',4100.0,10],
    '7':['Helado',4500.0,41],
    '8':['Galletas',500.0,8],
    '9':['Chocolates',4500.0,80],
    '10':['Jamon',15000.0,10],

} 


def listaIdProducto():
    idElementos =sorted(list(map(int,list(productos))))
    return idElementos

#metodoprecio mayor
def numeroMayor(listDatos,lista):
    numeroMayor=0
    keyPrecioMayor=0
    for  indice in lista:
        if numeroMayor<listDatos[str(indice)][1]:
            keyPrecioMayor=indice
            numeroMayor=listDatos[str(indice)][1]
    return(keyPrecioMayor,numeroMayor)
#metodo preciomenor
def numeroMenor(listDatos,lista):
    numeroMenor=numeroMayor(listDatos,lista)[1]
    keyPrecioMenor=numeroMayor(listDatos,lista)[0] 
    for  indice in lista:
        if numeroMenor>listDatos[str(indice)][1]:
            keyPrecioMenor=indice
            numeroMenor=listDatos[str(indice)][1]
    return(keyPrecioMenor)

#metodo promedio de precio
def promedioPrecios():
    sumaProducto=0
    for indice in listaIdProducto():
        sumaProducto+=productos[str(indice)][1]
    return("{0:.1f}".format(sumaProducto/len(listaIdProducto())))



#metodo valor inventario
def valorInventario():
    valorInventario=0
    valorProducto=0
    for indice in listaIdProducto():
        valorProducto=productos[str(indice)][1] * productos[str(indice)][2]
        valorInventario +=valorProducto
    return(valorInventario)


#metodo imprime los resultados
def resultado():
    articuloPrecioMayor=str(numeroMayor( productos,listaIdProducto())[0])
    articuloPrecioMenor=str(numeroMenor( productos,listaIdProducto()))
    print(productos[articuloPrecioMayor][0],productos[articuloPrecioMenor][0],promedioPrecios(),valorInventario())

#metodo create
def agregar(IdProducto,nombre,precio,inventario):
    if int(IdProducto) not in listaIdProducto():
        productos[IdProducto]=[nombre,precio,inventario]
        resultado()
    else:
        print("ERROR")


#metodo Update
def actualizar(IdProducto,nombre,precio,inventario):
    if int(IdProducto) in listaIdProducto() :
        productos.update({IdProducto:[nombre,precio,inventario]})
        resultado()
    else:
        print("ERROR")

#metodo delete
def borrar(IdProducto):
    if int(IdProducto) in listaIdProducto() :
        productos.pop(IdProducto)
        resultado()
    else:
        print("ERROR")
    

operacion=input()

idProdu , nombre , precio , inventario = input().split()
idProdu=str(idProdu)
nombre=str(nombre)
precio=float(precio)
inventario=int(inventario)

if operacion=='ACTUALIZAR':
    actualizar(idProdu,nombre,precio,inventario)
elif operacion=='BORRAR':
    borrar(idProdu)
elif operacion =='AGREGAR':
    agregar(idProdu,nombre,precio,inventario)
    












    


