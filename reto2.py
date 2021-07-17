#reto 1 camilo
class FotoMulta:
    #metodo constructor
    def __init__(self , distanciaMetros,velocidadMaxima,tiempoSegundo):
        self.distanciaMetros = distanciaMetros
        self.velocidadMaxima = velocidadMaxima # en km/h
        self.tiempoSegundo = tiempoSegundo
    #pasa de segundo a hora 
    def tiempoHora(self):
        tiempoHora =  self.tiempoSegundo/3600
        return tiempoHora
    # metros a kilometros
    def distanciaKilometros(self):
        distanciaKilometros =   self.distanciaMetros/1000
        return distanciaKilometros 
    #evalua velociada alcansada
    def velocidadPromedio(self):
        velocidadPromedio= self.distanciaKilometros()/self.tiempoHora()
        return velocidadPromedio
    #evalua el porcentaje de la velocida maxima
    def porcentajeMaximoVelocidad(self):
        porcentajeMaximoVelocidad = 0.2 * self.velocidadMaxima #dado por el 20% que evalua el tipo de infraccion
        return porcentajeMaximoVelocidad 
    # elvalua el resultado final
    def resultadoMulta(self):
        velocidaPermitidaPocentaje = self.velocidadMaxima + self.porcentajeMaximoVelocidad()
        if self.velocidadPromedio()< self.velocidadMaxima:
            print("OK")
        elif self.velocidadPromedio()>self.velocidadMaxima and self.velocidadPromedio()<velocidaPermitidaPocentaje:
            print("MULTA")
        elif self.velocidadPromedio()>=velocidaPermitidaPocentaje:
            print("CURSO SENSIBILIZACION")
    

        
a , b , c = input().split(" ")#permite tomar los datos de forma lineal 

a = float(a)
b = float(b)
c = float(c)

if a<0 or b<0 or c<0:
    print("ERROR")
else :
    autos = FotoMulta(a ,b ,c )
    autos.resultadoMulta()

