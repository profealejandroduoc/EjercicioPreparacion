from os import system
system("cls")



rut=""
nombre=""
direccion=""
correo=""
edad=0
sexo=""
registros=""
plansalud=""

while True:
    system("cls")
    print("""
    Centro Médico DUOC 

    1.	Registrar Paciente
    2.	Atención Paciente
    3.	Consultar Datos Paciente
    4.	Salir

    """)
    op=input("Ingrese opción: ")
    match op:
        case "1":
            #Rut debe ser un número entero que se encuentre dentro del rango de 5000000 y 99999999
            while True:
                rut=input("Ingrese rut: ")
                rut=rut.replace(".","").replace("-","")
                
                if int(rut)>=5000000 and int(rut)<=99999999:
                    break
                else:
                    print("Rut incorrecto, reingrese ")



        case "2":
            pass
        case "3":
            pass
        case "4":
            print("Fin del programa....")
            break
    
    input("Presione una tecla para continuar......")
    
