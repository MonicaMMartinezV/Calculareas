"""
Mónica Monserrat Martínez Vázquez
Este programa calcula las áreas de las siguientes formas:
    Triángulo
    Círculo
    Rectángulo
    Rombo
    Cuadrado
    Romboide
    Trapecio
    Polígonos regulares
"""
import math

def menu():
    print("1. Área de un triángulo")
    print("2. Área de un círculo")
    print("3. Área de un rectángulo")
    print("4. Área de un rombo")
    print("5. Área de un cuadrado")
    print("6. Área de un romboide")
    print("7. Área de un trapecio")
    print("8. Área de un polígonos regulares")
    print("0. Salir")

def AreaTriangulo(h, b):
    return (b * h) / 2

def AreaCirculo(r):
    return (math.pi * math.pow(r, 2))

def AreaRectangulo(h, b):
    return b * h

def AreaRombo(D, d):
    return (D * d) / 2

def AreaCuadrado(l):
    return l ** 2

def AreaRomboide(h, b):
    return b * h

def AreaTrapecio(B, b, h):
    return ((B + b)/ 2) * h 

def AreaPregulares(n, l, a):
    return ((n * l) * a)/ 2

def main():
    print("Elige tu opción")
    
    menu()
    opcion = int(input(""))
    
    if opcion == 1:
        h = float(input("Introduce la altura: "))
        b = float(input("Introduce la base: "))
        
        print("Área: %.2f" %(AreaTriangulo(h, b)))
    elif opcion == 2:
        r = float(input("Introduce el radio: "))
        
        print("Área: %.2f" %(AreaCirculo(r)))
    elif opcion == 3:
        h = float(input("Introduce la altura: "))
        b = float(input("Introduce la base: "))
        
        print("Área: %.2f" %(AreaRectangulo(h, b)))
    elif opcion == 4:
        D = float(input("Introduce la diagonal mayor: "))
        d = float(input("Introduce la diagonal menor: "))
        
        print("Área: %.2f" %(AreaRombo(D, d)))
    elif opcion == 5:
        l = float(input("Introduce el lado: "))
        
        print("Área: %.2f" %(AreaCuadrado(l)))
    elif opcion == 6:
        h = float(input("Introduce la altura: "))
        b = float(input("Introduce la base: "))
        
        print("Área: %.2f" %(AreaRomboide(h, b)))
    elif opcion == 7:
        B = float(input("Introduce la base mayor: "))
        b = float(input("Introduce la base menor: "))
        h = float(input("Introduce la altura: "))
        
        print("Área: %.2f" %(AreaTrapecio(B, b, h)))
    elif opcion == 8:
        n = float(input("Introduce el numero de lados: "))
        l = float(input("Introduce la longitud de los lados: "))
        a = float(input("Introduce la apotema: "))
        
        print("Área: %.2f" %(AreaPregulares(n, l, a)))
    elif opcion == 0:
        print("¡Adios! Vuelve pronto")
    else:
        print("Opción inválida")

main()