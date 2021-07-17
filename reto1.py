#datos de entrada
#reto 1 camilo
salario_Base , hora_Extras , bonificaciones  = input().split(" ")#permite tomar los datos de forma lineal 
salario_Base = float(salario_Base)
horaExtras = int(horaExtras)#cantidad de horas extras en un type int
bonificaciones = int(bonificaciones) #uno si existe y 0 si no existe
#metodos para horas extras
valorHoraNormal = salario_Base/185
recargo = 0.45 * valorHoraNormal #evalua el recargo por hora extra tomadolo como el 45%
valorHorasExtras = valorHoraNormal + recargo
salarioHorasExtras = hora_Extras*valorHorasExtras 
#metodos para bonificaciones
valorbonificaciones = 0.035*salario_Base #define la cantida del recargo tomando el 3.5%
salariobonificaciones = valorbonificaciones*bonificaciones
#salalrio total
salarioTotalSinDescuento = salario_Base + salarioHorasExtras  + salariobonificaciones
#metodos de descuentos
descuentoplanSalud = 0.045*salarioTotalSinDescuento #descuento del 4.5%
descuentoPension = 0.03*salarioTotalSinDescuento #descuento del 3%
descuentoCompesaccion = 0.03*salarioTotalSinDescuento #descuento del 3%
totalDescuentos = descuentoCompesaccion + descuentoPension + descuentoplanSalud
salarioTotalConDescuento = salarioTotalSinDescuento - totalDescuentos
print("{0:.1f}".format(salarioTotalSinDescuento) , "{0:.1f}".format(salarioTotalConDescuento))