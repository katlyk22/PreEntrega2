class Cliente:
    def __init__(self,nombre,documento,fecha_nacimiento,direccion,email):
        self.nombre = nombre
        self.documento = documento
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion 
        self.email = email

    def __str__(self):
        return f"""
                    Cliente:{self.nombre},
                    Documento:{self.documento},
                    Fecha de nacimineto:{self.fehca_nacimiento},
                    Direccion:{self.direccion},
                    Email:{self.email}"""
    
    def compra(self, fecha , cantidad_articulos , monto ):
        self.fecha = fecha
        self.cantidad_articulos = cantidad_articulos
        self.monto = monto
        print (f"{self.nombre} realizo una compra el dia {self.fecha} de {self.cantidad_articulos} articulos por un monto total de $ {self.monto}")

    def descuentos(self,medio_de_pago,monto):
        self.medio_de_pago = medio_de_pago
        self.monto = monto
        
        if medio_de_pago == "efectivo":
            final = int(self.monto) - 1000
            print ("Se le ha aplicado un descuento por pago en efectivo, el monto final de la compra es de " , final )
        else:
            print( f"El valor final es de {self.monto}")

    def cancelarcompra(self,cancel):
        self.cancel = cancel
        print ("usted a solicitado la cancelacion de la compra, ingrese SI para continuar con la cancelacion o NO para salir ")
        cancel =  input(f"cancelar compra SI / NO?")
        print (cancel)
        if cancel == "SI" :
            print ("Compra cancelada exitosamente")
        else:
            print("la compra no ha sido cancelada le llegaran al mail los pasos a seguir")
        

