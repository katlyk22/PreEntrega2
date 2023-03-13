from Paquete.ClassCliente import Cliente
from Paquete.RegistroCliente import Regis


Regis.registro ()
Regis.datos()

Cliente1 = Cliente ( "Harry Styles", "25698541", "10/11/1996", "Av.Styles 45 London UK"," comebackonedirection@gmail.com" )
Cliente1.compra("13/03/2023" , "10" , "$10000")
Cliente1.descuentos("efectivo", "10000")
Cliente1.cancelarcompra("si/no")

Cliente2 = Cliente ("taylor Swift", "98765432","13/12/1989","Av.Folklore 34 los angeles USA", "loveyoujoealwin@gmail.com")
Cliente2.compra("13/03/2023","700","$45000")
Cliente2.descuentos("Debito", "45000")

print (Cliente1.compra)
print (Cliente1.descuentos)
print (Cliente1.cancelarcompra)
