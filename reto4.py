#reto4#reto 1 camilo
class MaquinaEstampillas:
    #constructor 
    def __init__(self,N):
        self.N = N
    #genenar  ls datos de las estampillas
    def storeEstampillas(self):
        estampillas = input().split()
        if self.N == len(estampillas):
            estampillaStore=list()
            for dato in range(0,len(estampillas)):
                estampillaStore.append(int(estampillas[int(dato)]))
        return(estampillaStore)

        
N,K = input().split()
N = int(N)
K = int(K)

maquina=MaquinaEstampillas(N)
estampillasLista=maquina.storeEstampillas()




#contar estampillas repetidas
def estamillasRepetidas():
    sinRepetir=list()
    repetidas=list()
    for dato in estampillasLista:
        if dato not in sinRepetir:
            sinRepetir.append(dato)
        else:
            repetidas.append(dato)
    return(len(repetidas))

#memoria de maquina
def memoriaMaquina(K):
    memoriaLimitada=list()
    for indice in range(K,len(estampillasLista)):
        for i in range(indice -K, indice):
            if estampillasLista[ indice ] == estampillasLista[ i ] and i not in memoriaLimitada:
                    memoriaLimitada.append(i)
    return(len(memoriaLimitada))

#llama a los metodos
print(estamillasRepetidas(),memoriaMaquina(K))
            



