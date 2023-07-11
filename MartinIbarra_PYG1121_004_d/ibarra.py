import os
import numpy as np
def llenarmatriz(matriz):
    p=1
    for i in range(10):
        for j in range(4):
            matriz[i,j]=p
            p+=1
def validaop(op):
    while(True):
        try:
            op=int(input(" Elija una opcion "))
            if(op>=1 and op<=5):
                break
            else:
                print("Debe ingresar una opcion entre 1 y 5 ")
        except ValueError:
            print("Debe ser un numero entero ")
    return op
def validarut(rut):
    os.system("cls")
    rut=""
    while(len(rut)<=0):
        rut=input("Ingrese su rut: ")
        if(len(rut)<8):
            print("Debe tener minimo 8 digitos ")
            rut=""
 
def mostrardisponibles(matriz):
    os.system("cls")
    print("         A        B              C       D")
    for i in range(10):
        print("\n")
        for j in range(4):
            if(j==1):
                print("\t",matriz[i,j], end="        ")
            else:
                print("\t",matriz[i,j], end="    ")
    print("\n\n")
def validadepto(depto):
    depto=0
    while(True):
        try:
            depto=int(input("Ingrese un departamento 1-40 "))
            if(depto>=1 and depto<=40):
                break
            else:
                print("Debe ser un numero entre 1 y 40 ")
        except ValueError:
            print("El numero debe ser entero ")
    return depto
def buscarDisponible(matriz, depto):
    for x in range(10):
        for i in range(4):
            if (depto==matriz[x,i]):
                return True
    return False
def comprardepto(matriz,depto):
    for x in range(10):
        for i in range(4):
            if (matriz[x,i]==depto):
                matriz[x,i]=0     
                if (i==0):
                    pago=3800
                if(i==1):
                    pago=3000
                if(i==2):
                    pago=2800
                if(i==3):
                    pago=3500
    return pago

def totalventas(matriz):
    suma=0
    for x in range(10):
        for i in range(4):
            if(matriz[x,i]==0):
                if(i==0):
                    suma+=3800
                if(i==1):
                    suma+=3000
                if(i==2):
                    suma+=2800
                if(i==3):
                    suma+=3500
    return suma

def muestrarut(rut):
    print("Los rut de los compradores son",rut)
    


