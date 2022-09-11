"""
Este programa calcula las áreas de las siguientes formas:
    -Triángulo
    -Círculo
    -Rectángulo
    -Rombo
    -Cuadrado
    -Romboide
    -Trapecio
    -Polígonos regulares
Además, realiza acciones como:
    -Divisores sin residuos
    -Numeros pares
    -Suma y resta de números
    -Te fecilita por ser tu cumpleaños 
    -Casos prueba
    
"""
import math


#Esta función solo despliega el menu de opciones a las que puedes acceder
def menu():
    print("1. Área de un triángulo")
    print("2. Área de un círculo")
    print("3. Área de un rectángulo")
    print("4. Área de un rombo")
    print("5. Área de un cuadrado")
    print("6. Área de un romboide")
    print("7. Área de un trapecio")
    print("8. Área de un polígonos regulares")
    print("9. Divisores sin residuos de un número")
    print("10. Números pares")
    print("11. Sumar y restar")
    print("12. Felicitaciones")
    print("13. Casos de prueba")
    print("0. Salir")
    
    
#Esta función calcula el área de un triángulo por medio de una altura y base otorgadas por el usuario
def AreaTriangulo(h, b):
    return (b * h) / 2


#Esta función calcula el área de un círculo por medio de un radio otorgado por el usuario
def AreaCirculo(r):
    return (math.pi * math.pow(r, 2))


#Esta función calcula el área de un rectángulo por medio de una altura y base otorgadas por el usuario
def AreaRectangulo(h, b):
    return b * h


#Esta función calcula el área de un rombo por medio de una diagonal mayor y menor otorgadas por el usuario
def AreaRombo(D, d):
    return (D * d) / 2


#Esta función calcula el área de un cuadrado por medio de un lado otorgado por el usuario
def AreaCuadrado(l):
    return l ** 2


#Esta función calcula el área de un romboide por medio de una altura y base otorgadas por el usuario
def AreaRomboide(h, b):
    return b * h


#Esta función calcula el área de un trapecio por medio de una base mayor, base menor y altura otorgadas por el usuario
def AreaTrapecio(B, b, h):
    return ((B + b)/ 2) * h 


#Esta función calcula el área de un polígono regular por medio de un número de lados, logitud de los lados y apotema otorgadas por el usuario
def AreaPregulares(n, l, a):
    return ((n * l) * a)/ 2


#Esta función calcula y despliga en la pantalla el número de divisores sin residuo de un número otorgado por el usuario
def Divisores(N):
    print("Los divisores sin residuos del número", N, "son: ", end="")
    for cont in range(1,N+1,1):
        if (N % cont) == 0:
            if cont == 1:
                print((cont), end="")
            else:
                print(",", (cont), end="")


#Esta función calcula y despliga en la pantalla la cantidad de números pares que quiere el usuario
def numerosPares (p):
    t=1
    cont=1
    while t <= p:
        if (cont%2) == 0:
            print(cont)
            cont+=1
            t+=1
        else:
            cont+=1


"""Esta función suma y resta números ingresados por el usuario.
   Puede poner la cantidad que él desee y cuando quiera el resultado debera poner 0
"""
def sumaresta ():
    sumaresta=0
    n=1
    print("Cuando quiera obtener su resultado ingrese 0")
    while n != 0:
        n=int(input("Introduce los numeros que quieras sumar y restar: "))
        sumaresta+=n
    print(sumaresta)


"""Esta función es especial, ya que no calcula nada en particular.
   Lo que esta función hace es preguntarte tu nombre, si es o no tu cumpleaños y los años que cumples
   Esto con el fin de poder felicitarte en nombre de "Calculareas"
   Esta función también tiene la opcion de cuando no es tu cumpleaños, mandandote al menú otra vez
"""
def felicitaciones ():
    nombre=str(input("Hola :D, ¿Cuál es tu nombre?: "))
    print("Mucho gusto", nombre, ":3")
    cumple=str(input("\n¿El día de hoy es tu cumpleaños? (Si/No)"))
    if cumple == "no" or cumple == "No" or cumple == "NO":
        print("Ohhh que lastima...")
        print("Cuando sea tu cumpleaños vuelve :D")
        print("\nMuchas gracias por usar nuestra aplicación")
        main()
    elif cumple == "si" or cumple == "Si" or cumple == "SI":
        print("\nQue bueno que nos dices eso")
        años=str(input("Nada más una ultima pregunta, ¿cuántos años cumples? "))
        print("¡¡Gracias por contestar nuestras preguntas!!")
        print("\nSolo queriamos desearte....")        
        print("\n\t¡¡¡FELIZ CUMPLEAÑOS", nombre, "por cumplir", años,"años!!!")
        print("\tCalculareas te desea que este día te la pases muy bien y comas mucho pastel OwO")
        print("\t¡Muchas gracias por usar nuestra aplicación! <(O//w//O)>")
        print("\nPuedes contiinuar con tu día :) ")
        main()

#Esta función es para comprobar si funcionan correctamente todas las funciones en este programa, poniendole números predeterminados
def casosdeprueba ():
    print("\nArea de un triángulo con altura 2 y base 4:", AreaTriangulo(2, 4))
    print("\nArea de un circulo con radio 2: ", AreaCirculo(2))
    print("\nArea de un rectángulo con altura 5 y base 6:", AreaRectangulo(5, 6))
    print("\nArea de un rombo con diagonal mayor 7 y diagonal menor 8:", AreaRombo(7, 8))
    print("\nArea de un cuadrado con lado 4:", AreaCuadrado(4))
    print("\nArea de un romboide con altura 2 y base 4:", AreaRomboide(2, 4))
    print("\nArea de un trapecio con base mayor 4, base menor 2 y altura 6:", AreaTrapecio(4, 2, 6))
    print("\nArea de un polígono regular con número de lados 5, una longitud de lados 4 y apotema 4:", AreaPregulares(5, 4, 4))
    print("\nDivisores:")
    Divisores(4)
    print("\n4 números pares:")
    numerosPares(4)
    print("\nIntroduce 2 y 4, el resultado debe darte 6")
    sumaresta ()
    print("\nIntroduce el nombre Juan, que Si es tu compleaños y que tienes 12, los resultados \nque debe de darte es una felicitación personalizada")
    felicitaciones ()


"""Esta función main realiza las acciones "tronco" de todas las funciones
   Las llama y pide los datos basicos que necesita la función para trabajar
   Ademas de las excepciones y posibles errores
"""
def main():
    print("Elige tu opción: ")
    
    menu()
    opcion = int(input("--> "))
    
    if opcion == 1:
        h = float(input("Introduce la altura: "))
        b = float(input("Introduce la base: "))
        if (h<0 or b<0):
            print("No valido")
        else:
            print("Área: %.2f" %(AreaTriangulo(h, b)))
    
    elif opcion == 2:
        r = float(input("Introduce el radio: "))
        if r<=0:
            print("No valido")
        else:
            print("Área: %.2f" %(AreaCirculo(r)))
    
    elif opcion == 3:
        h = float(input("Introduce la altura: "))
        b = float(input("Introduce la base: "))
        if (h<=0 or b<=0):
            print("No valido")
        else:    
            print("Área: %.2f" %(AreaRectangulo(h, b)))
    
    elif opcion == 4:
        D = float(input("Introduce la diagonal mayor: "))
        d = float(input("Introduce la diagonal menor: "))
        if (D<=0 or d<=0):
            print("No valido")
        else:
            print("Área: %.2f" %(AreaRombo(D, d)))
    
    elif opcion == 5:
        l = float(input("Introduce el lado: "))
        if l<=0:
            print("No valido")
        else:
            print("Área: %.2f" %(AreaCuadrado(l)))
    
    elif opcion == 6:
        h = float(input("Introduce la altura: "))
        b = float(input("Introduce la base: "))
        if (h<=0 or b<=0):
            print("No valido")
        else:
            print("Área: %.2f" %(AreaRomboide(h, b)))
    
    elif opcion == 7:
        B = float(input("Introduce la base mayor: "))
        b = float(input("Introduce la base menor: "))
        h = float(input("Introduce la altura: "))
        if (B<=0 or b<=0 or h<=0):
            print("No valido")
        else:
            print("Área: %.2f" %(AreaTrapecio(B, b, h)))
    
    elif opcion == 8:
        n = float(input("Introduce el numero de lados: "))
        l = float(input("Introduce la longitud de los lados: "))
        a = float(input("Introduce la apotema: "))
        if (n<=0 or l<=0 or a<=0):
            print("No valido")
        else:
            print("Área: %.2f" %(AreaPregulares(n, l, a)))
            
    elif opcion == 9:
        N=int(input("Introduce un número entero: "))
        if N<=0:
            print("No valido")
        else:
            Divisores(N)
            
    elif opcion == 10:
        p=int(input("¿Cuántos numeros pares quieres?: "))
        if p<=0:
            print("No valido")
        else:
            numerosPares(p)
    
    elif opcion == 11:
        sumaresta()
    
    elif opcion == 12:
        felicitaciones()
    
    elif opcion == 13:
        casosdeprueba()
            
    elif opcion == 0:
        print("¡Adios! Vuelve pronto")
    
    else:
        print("Opción inválida")

main()
