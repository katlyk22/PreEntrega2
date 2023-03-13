import csv 

class Regis :

    def registro ():

        f = open ("mi_db.csv" , "a" )
        usuario = input("Cree su nombre de usuario:")
        password = input("Cree su contraseña:")
        f.close()
        f = open ("mi_db.csv" , "r" )
        base_datos = csv.reader(f, delimiter=",")

        for usu in base_datos:
                if usuario == usu[0]:
                    return ("Nombre de usuario no disponible. Intente nuevamente" )
                    break
                else:
                    continue
        else:
            print ("Usuario y contraseña registrados exitosamente")
        f.close()
        f = open ("mi_db.csv" , "a" )
        f.write (f"{usuario},{password},")
        print (f"usuario: {usuario}\n contraseña: {password}")
        f.close()

    def datos ():
         f = open ("mi_db.csv" , "a" )
         nombre = input("ingrese su nombre completo ")
         documento = input("Ingrese su numero de documento ")
         fecha_nacimiento = input("Ingrese su fecha de nacimiento ")
         direccion = input("ingrese su direccion ")
         email = input("ingrese su email ")
         f.close()
         f = open ("mi_db.csv" , "a" )
         f.write (f"{nombre},{documento},{fecha_nacimiento},{direccion},{email}\n")
         print("datos guardados exitosamente")
         print(f" nombre = {nombre}, documento: {documento}, fecha_nacimiento: {fecha_nacimiento}, direcion: {direccion}, email: {email}")
         f.close
