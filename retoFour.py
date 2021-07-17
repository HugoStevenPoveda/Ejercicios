class Estampilla:
    # constructor
    def __init__(self, numeroEstampilla, tamañomemeoria):
        self.numeroEstampilla = numeroEstampilla
        self.tamañomemeoria = tamañomemeoria

    # almacena las estampillas que se ingresen

    def alamcenaEstapillas(self):
        estampillas = input()
        estampillas = estampillas.split(" ")
        if len(estampillas) == self.numeroEstampilla:
            estampillaStore = list(map(int, estampillas))
        return estampillaStore
    # define las estampillas repetidas

    def EstampillasRepetidas(self):
        sinRepetir = []
        repetidas = []
        for dato in self.alamcenaEstapillas():
            if dato not in sinRepetir:
                sinRepetir.append(dato)
            else:
                if dato not in repetidas:
                    repetidas.append(dato)
        print(len(repetidas))
    
    #metodo memoria
    def memoria (self):
        self.tamañomemeoria

  


numeroEstampilla = int(input())
if numeroEstampilla >= 1 and numeroEstampilla <= 10000:
    ingresoEstampillas = Estampilla(numeroEstampilla, 0)
    ingresoEstampillas.EstampillasRepetidas()
   
