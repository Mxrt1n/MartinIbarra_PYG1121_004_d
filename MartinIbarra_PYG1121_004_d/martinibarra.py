import os
import numpy as np
import ibarra as ft
matriz=np.empty([10,4],type(int))
ft.llenarmatriz(matriz)
op=0
depto=0
rut=[]
os.system("cls")

while(op!=5):
    print("********Inmobiliaria Casa Feliz*****")
    print("1) Comprar departamento ")
    print("2) Mostrar departamentos disponibles ")
    print("3) Ver listado de compradores ")
    print("4) Mostrar ganancias totales " )
    print("5) Salir ")
    op=ft.validaop(op)
    if(op==1):
        ft.validarut(rut)
        ft.mostrardisponibles(matriz)
        depto=ft.validadepto(depto)
        comprueba=ft.buscarDisponible(matriz,depto)
        if comprueba:
            print("El departamento esta disponible!! ")
            pagar=ft.comprardepto(matriz,depto)
            print("usted va a cancelar:",pagar,"UF")
        else: 
            print("El departamento no esta disponible ")
        input("Proceso realizado con exito!!!! presione una tecla para continuar ")
        os.system("pause")
    if(op==2):
        ft.mostrardisponibles(matriz)
        os.system("pause")
    if(op==3):
        totalcompradores=ft.muestrarut(rut)
        print(totalcompradores)
        input("presione una tecla para continuar")
    if(op==4):
        suma=0
        suma=ft.totalventas(matriz)
        if(suma==0):
            print(" No hay departamentos vendidos ")
        else:
            print("El total vendido es",suma)
            os.system("pause")
    if(op==5):
        print("Martin Ibarra 11/07/2023 ")
        print("ADIOOOOOOOOOOS")







    


