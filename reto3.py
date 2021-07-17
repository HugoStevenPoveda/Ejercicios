#reto 1 camilo
class ModeloTv:
    # metodoconstructor
    def __init__(self,puertosHdmi=0,pulgadas=0,resolucion=0,frecuencia=0,valor=0):
        #atributos de tv
        self.puertosHdmi=puertosHdmi
        self.pulgadas=pulgadas
        self.resolucion=resolucion
        self.frecuencia=frecuencia
        self.valor=valor

    #metodos 
    def tvElegidos(self):
        if self.puertosHdmi>=3 and self.pulgadas>=55 and  self.resolucion>=1080 and self.frecuencia>=60:
            indicador=True
        else:
            indicador=False
        return indicador
         

#dato sobre numero de datos y donde guardar si cuplen las condiciones 
cantidadDeDatos=int(input())
listaTv=[]
#evaluando datos
for dato in range(1,cantidadDeDatos+1):
    a , b , c , d , valor = input().split(" ")#permite tomar los datos de forma lineal 
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    valor = float(valor)
    datos=ModeloTv(a,b,c,d,valor)
    if datos.tvElegidos():
        listaTv.append(int(datos.valor))
#mostrat datos
if len(listaTv)>0:
    for dato in listaTv:
        print(dato)
else:
    print("NO DISPONIBLE")



