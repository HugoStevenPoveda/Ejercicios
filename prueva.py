datos={
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,

}

nuevo = list(map(int,list(datos)))

def suma1():
    suma=0
    for x in nuevo:
        suma+=x
    print(suma)
suma1()

""" def suma(a):
    suma=0
    for x in range(1,a+1):
        suma+=x
    print(suma)

a=int(input("digite su numero"))
suma(a) """
