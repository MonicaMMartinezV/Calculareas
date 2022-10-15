"""
-------------- C A L C U L A R E A S ---------------
El programa calcula las áreas de las siguientes formas:
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
    -Saca la media de un conjunto de valores 
    -Saca la moda de diferentes conjuntos de valores
    -Muestra tu historial
    -Casos prueba
    -Función secreta
Al final te da los resultados de las operaciones requeridas
    
"""
#Bibliotecas
import math
import os.path
from statistics import mode

if not os.path.isfile("Historial.txt"):
    f = open("Historial.txt","x")
    f.close()

file=open("Historial.txt","w+")
file.write("=================================================================\n")
file.write("----------------------- H I S T O R I A L -----------------------\n")
file.write("=================================================================\n")
file.write("\n")
file.flush()

def menu():
    """
(Conocimientos: funciones)
Esta función solo despliega el menu de opciones a las que puedes acceder
Recibe: Ningún valor
Despliega las opciones del programa
Devuelve: Ningún valor
    """
    print("=================MENÚ===================")
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
    print("13. Media de un conjunto de valores")
    print("14. Moda de diferentes conjuntos de valores")
    print("15. Casos de prueba")
    print("16. Historial")
    print("17. Función secreta")
    print("0. Salir")
  
def AreaTriangulo(h, b):
    """
(Conocimientos: funciones, operadores (aritméticos), variables, paso de parametros)
Esta función calcula el área de un triángulo por medio de una altura y base otorgadas por el usuario
Recibe: Datos de altura y base 
Calcula el área por medio de su fórmula y con los datos ingresados
Devuelve: Resultado área del triángulo
    """
    return (b * h) / 2

def AreaCirculo(r):
    """
(Conocimientos: funciones, uso de bibliotecas, operadores (aritméticos), variables, paso de parametros)
Esta función calcula el área de un círculo por medio de un radio otorgado por el usuario
Recibe: Dato del radio 
Calcula el área por medio de su fórmula y con los datos ingresados
Devuelve: Resultado área del círculo
    """
    return (math.pi * math.pow(r, 2))

def AreaRectangulo(h, b):
    """
(Conocimientos: funciones, operadores (aritméticos), variables, paso de parametros)
Esta función calcula el área de un rectángulo por medio de una altura y base otorgadas por el usuario
Recibe: Datos de altura y base 
Calcula el área por medio de su fórmula y con los datos ingresados
Devuelve: Resultado área del rectángulo
    """
    return b * h

def AreaRombo(D, d):
    """
(Conocimientos: funciones, operadores (aritméticos), variables, paso de parametros)
Esta función calcula el área de un rombo por medio de una diagonal mayor y menor otorgadas por el usuario
Recibe: Datos de la diagonal mayor y menor 
Calcula el área por medio de su fórmula y con los datos ingresados
Devuelve: Resultado área del rombo
    """
    return (D * d) / 2

def AreaCuadrado(l):
    """
(Conocimientos: funciones, operadores (aritméticos), variables, paso de parametros)
Esta función calcula el área de un cuadrado por medio de un lado otorgado por el usuario
Recibe: Dato de un lado 
Calcula el área por medio de su fórmula y con los datos ingresados
Devuelve: Resultado área del cuadrado
    """
    return l ** 2

def AreaRomboide(h, b):
    """
(Conocimientos: funciones, operadores (aritméticos), variables, paso de parametros)
Esta función calcula el área de un romboide por medio de una altura y base otorgadas por el usuario
Recibe: Datos de altura y base 
Calcula el área por medio de su fórmula y con los datos ingresados
Devuelve: Resultado área del romboide
    """
    return b * h

def AreaTrapecio(B, b, h):
    """
(Conocimientos: funciones, operadores (aritméticos), variables, paso de parametros)
Esta función calcula el área de un trapecio por medio de una base mayor, base menor y altura otorgadas por el usuario
Recibe: Datos de la base mayor, base menor y altura 
Calcula el área por medio de su fórmula y con los datos ingresados
Devuelve: Resultado área del trapecio
    """
    return ((B + b)/ 2) * h 

def AreaPregulares(n, l, a):
    """
(Conocimientos: funciones, operadores (aritméticos), variables, paso de parametros)
Esta función calcula el área de un polígono regular por medio de un número de lados, logitud de los lados y apotema otorgadas por el usuario
Recibe: Datos del número de lados, logitud de los lados y apotema
Calcula el área por medio de su fórmula y con los datos ingresados
Devuelve: Resultado área del polígono regular
    """
    return ((n * l) * a)/ 2

def Divisores(N):
    """
(Conocimientos: funciones, operadores (aritméticos), variables, paso de parametros, condicionales, operadores booleanos, ciclos anidados, ciclo for, listas)
Esta función calcula y despliga en la pantalla el número de divisores sin residuo de un número otorgado por el usuario
Recibe: Número al que quieres saber sus divisores sin residuos
Por medio del for calcula los números que tengan residuo 0 al dividirlos con el número otorgado
Después, guarda en una lista todos lo números que cumplieron con la condición
Devuelve: Divisores sin residuo del número que se introdujo
    """
    d=[]
    for cont in range(1,N+1,1):
        if (N % cont) == 0:
            d.append(cont)
    print("")
    return d

def numerosPares (p):
    """
(Conocimientos: funciones, operadores (aritméticos), variables, paso de parametros, condicionales, operadores booleanos, ciclo while, listas)
Esta función calcula y despliga en la pantalla la cantidad de números pares que quiere el usuario
Recibe: Cantidad de números pares que quieres
Por medio de un contador y un while multiplicar la variable t por 2
Después, guarda en una lista todos lo números
Devuelve: Los números pares que se pidieron
    """
    NP=[]
    t=1
    cont=1
    print("Los números pares que solicitaste son los siguientes: ")
    while t <= p:
        NP.append(t*2)
        t += 1
    return NP

def sumaresta ():
    """
(Conocimientos: funciones, operadores (aritméticos), variables, paso de parametros, condicionales, operadores booleanos, ciclo while, listas)
Esta función suma y resta números ingresados por el usuario.
Puede poner la cantidad que él desee y cuando quiera el resultado debera poner 0
Recibe: Números que se sumaran o restaran y un igual(0)
Pide repetidamente, a traves de un while, los números que desea sumar y restar
Los suma y resta
Devuelve: Resultado de las sumas y restas
    """
    sumaresta=0
    n=1
    print("Cuando quiera obtener su resultado ingrese 0")
    while n != 0:
        n=int(input("Introduce los numeros que quieras sumar y restar: "))
        sumaresta+=n
    return sumaresta

def felicitaciones ():
    """
(Conocimientos: funciones, variables, condicionales, operadores booleanos, anidacion condicionales, manipulación de strings)
Esta función es especial, ya que no calcula nada en particular.
Lo que esta función hace es preguntarte tu nombre, si es o no tu cumpleaños y los años que cumples
Esto con el fin de poder felicitarte en nombre de "Calculareas"
Esta función también tiene la opcion de cuando no es tu cumpleaños, mandandote al menú otra vez
Recibe: Tu nombre, si es o no tu cumpleaños y cuantos años cumples
Pide su nombre y saluda
Pide si es o no su cumpleaños
Si es su cumpleaños, pide los años que vas a cumplir y regresa al menú
Si no es tu cumpleaños, te regresa al menú
Devuelve: Una felicitación por parte de "Calculareas"
    """
    nombre=str(input("Hola :D, ¿Cuál es tu nombre?: "))
    print("Mucho gusto", nombre, ":3")
    cumple=str(input("\n¿El día de hoy es tu cumpleaños? (Si/No)"))
    if cumple == "no" or cumple == "No" or cumple == "NO":
        print("Ohhh que lastima...")
        print("Cuando sea tu cumpleaños vuelve :D")
        print("\nMuchas gracias por usar nuestra aplicación")
        n=("No era tu compleaños")
        return n
        main()
    elif cumple == "si" or cumple == "Si" or cumple == "SI":
        print("\nQue bueno que nos dices eso")
        años=str(input("Nada más una ultima pregunta, ¿cuántos años cumples? "))
        print("************************************")
        print("¡¡Gracias por contestar nuestras preguntas!!")
        print("\nSolo queriamos desearte....")        
        print("\n\t¡¡¡FELIZ CUMPLEAÑOS", nombre, "por cumplir", años,"años!!!")
        print("\tCalculareas te desea que este día te la pases \n\t     muy bien y comas mucho pastel OwO")
        print("\t¡Muchas gracias por usar nuestra aplicación!")
        print("                          <(O//w//O)>")
        print("\nPuedes continuar con tu día :) ")
        print("************************************")
        print("")
        s=("Si era tu cumpleaños y te dimos unas felicitaciones")
        return s
 
def crea_lista(tam):
    """
(Conocimientos: funciones, variables, paso de parametros, ciclo for, listas)
Esta función sirve para crear una lista de valores asignados por el usuario
Recibe: Tamaño de la lista y valores dentro de esta
Hace una lista con los datos otorgados por el usuario 
Devuelve: Una lista
    """
    m=[]
    for i in range (tam):
        valor = float(input("Introduce un valor: "))
        m.append(valor)
    return m

def media(m):
    """
(Conocimientos: funciones, variables, operadores (aritméticos), paso de parametros, ciclo for)
Esta función es para promediar un conjunto de valores 
Recibe: La lista generada anteriormente
Saca media sumando todo y dividiendolo por el número total de valores 
Devuelve: La media de una lista creada por el usuario
    """
    suma=0
    for i in range(0,len(m)):
        suma = suma + m[i]
    return suma / len(m)

def crear_matriz(r,c):
    """
(Conocimientos: funciones, variables, paso de parametros, ciclo for, matrices)
Esta función crea una matriz apartir de los datos otorgados por el usuario
Recibe: Renglones y columnas de la matriz
Hace una matriz con los datos otorgados por el usuario 
Devuelve: Una matriz
    """
    M=[]
    l=[]
    for i in range (r):
        l=[float(input("Introduce los valores: ")) for j in range (c)]
        M.append(l)
    return M

def moda(M):
    """
(Conocimientos: funciones, variables, uso de funciones de bibliotecas, paso de parametros, ciclo for, aplanado)
Esta función es para sacar la moda de una matriz creada por el usuario 
Recibe: La matriz generada anteriormente
Aplana la matriz
Y por medio de una función de statistics de mode saca la moda 
Devuelve: La moda de una matriz creada por el usuario
    """
    plana=[i for j in M for i in j]
    res=mode(plana)
    return res
    
def casosdeprueba ():
    """
(Conocimientos: funciones, variables, paso de parametros)
Esta función es para comprobar si funcionan correctamente todas las funciones en este programa, poniendole números predeterminados
Recibe: Ningún valor
Ejecuta la funciones de este programa, aplicandoles casos de prueba
Devuelve: Informa que se ejecuto esta función
    """
    print("Area de un triángulo con altura 2 y base 4:", AreaTriangulo(2, 4))
    print("---------")
    print("Area de un circulo con radio 2: ", AreaCirculo(2))
    print("---------")
    print("Area de un rectángulo con altura 5 y base 6:", AreaRectangulo(5, 6))
    print("---------")
    print("Area de un rombo con diagonal mayor 7 y diagonal menor 8:", AreaRombo(7, 8))
    print("---------")
    print("Area de un cuadrado con lado 4:", AreaCuadrado(4))
    print("---------")
    print("Area de un romboide con altura 2 y base 4:", AreaRomboide(2, 4))
    print("---------")
    print("Area de un trapecio con base mayor 4, base menor 2 y altura 6:", AreaTrapecio(4, 2, 6))
    print("---------")
    print("Area de un polígono regular con número de lados 5, una longitud de lados 4 y apotema 4:", AreaPregulares(5, 4, 4))
    print("---------")
    print("Divisores:")
    Divisores(4)
    print("---------")
    print("Cuatro números pares:")
    numerosPares(4)
    print("---------")
    print("Introduce 2 y 4, el resultado debe darte 6")
    print("El resultado de la suma y resta es: ",sumaresta ())
    print("---------")
    print("Introduce el nombre Juan, que Si es tu compleaños y que tienes 12, los resultados \nque debe de darte es una felicitación personalizada")
    felicitaciones ()
    print("---------")
    print("Esta función realiza una lista apartir de los datos asignados por el usuario")
    print("En este caso sera de tamaño 4")
    print("Introduce los valores 3, 8, 10, 3")
    print("La lista sera [3,8,10,3]")
    m=crea_lista(4)
    print("Esta es la lista: ", m)
    print("---------")
    print("La media de la lista anterior sera 6")
    print("La media es: ", media(m))
    print("---------")
    print("Esta función hara una matriz de 2 renglones y 2 columnas")
    print("Inserta los valores 2,5,5,7")
    print("La matriz quedara así: [[2,5],[5,7]]")
    M=crear_matriz(2,2)
    print("Esta es la matriz: ", M)
    print("---------")
    print("Con la matriz anterior realizaremos la moda")
    print("La moda de la matriz anterior sera 5")
    Moda=moda(M)
    print("La moda es: ", Moda)
    res=("Se ejecutó la función casos prueba")
    return res

def historial():
    """
(Conocimientos: funciones, variables, archivos, paso de parametros)
Esta función es para poder visualizar el historial de esta ejecución 
Recibe: Ningún valor
Regresa a la posición inicial del archivo y lo lee. Después lo imprime
Devuelve: Ningún valor
    """
    file.seek(0)
    contenido=file.read()
    print(contenido)

def funcionsecreta(cadena, caracter):
    """
(Conocimientos: funciones, operadores (aritméticos), variables, paso de parametros, Manipulación de cadenas, ciclo for, operadores booleanos, condicionales)
Esta función te permite saber cuantas veces se repite un caracter en tu nombre y te agradece
Recibe: La cadena y el caracter
Por medio de un for y un contador, se cuentas las veces que se repite un caracter dentro de una cadena
Devuelve: El número de veces que se repite el caracter
    """
    cont=0
    for i in range(len(cadena)):
        if cadena[i]==caracter:
            cont+=1
    return cont

def main():
    """
(Conocimientos: funciones, variables, archivos, condicionales, operadores booleanos, anidación de condicionales, ciclos while, ciclos anidados)
Esta función main realiza las acciones "tronco" de todas las funciones
Las llama y pide los datos basicos que necesita la función para trabajar
Ademas de las excepciones y posibles errores 
Recibe: Ningún valor
Llama todas las funciones que tiene este programa, pide los valores que necesita cada funcion para trabajar y los mete en variables; las funciónes
le regresan os resultados y los imprime y guarda en el historial
Devuelve: Ningún valor
    """
    continua = True
    while continua:
        print("Elige tu opción: ")
        
        menu()
        opcion = int(input("--> "))
        print("============================================")
        print("")
    
        if opcion == 1:
            file.write("Seleccionaste área de un triángulo \n")
            h = float(input("Introduce la altura: "))
            b = float(input("Introduce la base: "))
            if (h<0 or b<0):
                file.write("Input no valido\n")
                file.write("\n")
                file.flush()
                print("No valido")
                print("")
            else:
                n1=AreaTriangulo(h, b)
                file.write("Área triángulo: %.2f\n" %(n1))
                file.write("\n")
                file.flush()
                print("Área triángulo: %.2f" %(n1))
                print("")
    
        elif opcion == 2:
            file.write("Seleccionaste área de un círculo \n")
            r = float(input("Introduce el radio: "))
            if r<=0:
                file.write("Input no valido\n")
                file.write("\n")
                file.flush()
                print("No valido")
                print("")
            else:
                n2=AreaCirculo(r)
                file.write("Área círculo: %.2f\n" %(n2))
                file.write("\n")
                file.flush()
                print("Área círculo: %.2f" %(n2))
                print("")
    
        elif opcion == 3:
            file.write("Seleccionaste área de un rectángulo \n")
            h = float(input("Introduce la altura: "))
            b = float(input("Introduce la base: "))
            if (h<=0 or b<=0):
                file.write("Input no valido\n")
                file.write("\n")
                file.flush()
                print("No valido")
                print("")
            else:    
                n3=AreaRectangulo(h, b)
                file.write("Área rectángulo: %.2f\n" %(n3))
                file.write("\n")
                file.flush()
                print("Área rectángulo: %.2f" %(n3))
                print("")
    
        elif opcion == 4:
            file.write("Seleccionaste área de un rombo \n")
            D = float(input("Introduce la diagonal mayor: "))
            d = float(input("Introduce la diagonal menor: "))
            if (D<=0 or d<=0):
                file.write("Input no valido\n")
                file.write("\n")
                file.flush()
                print("No valido")
                print("")
            else:
                n4=AreaRombo(D, d)
                file.write("Área rombo: %.2f\n" %(n4))
                file.write("\n")
                file.flush()
                print("Área rombo: %.2f" %(n4))
                print("")
    
        elif opcion == 5:
            file.write("Seleccionaste área de un cuadrado \n")
            l = float(input("Introduce el lado: "))
            if l<=0:
                file.write("Input no valido\n")
                file.write("\n")
                file.flush()
                print("No valido")
                print("")
            else:
                n5=AreaCuadrado(l)
                file.write("Área cuadrado: %.2f\n" %(n5))
                file.write("\n")
                file.flush()
                print("Área cuadrado: %.2f" %(n5))
                print("")
    
        elif opcion == 6:
            file.write("Seleccionaste área de un romboide \n")
            h = float(input("Introduce la altura: "))
            b = float(input("Introduce la base: "))
            if (h<=0 or b<=0):
                file.write("Input no valido\n")
                file.write("\n")
                file.flush()
                print("No valido")
                print("")
            else:
                n6=AreaRomboide(h, b)
                file.write("Área romboide: %.2f\n" %(n6))
                file.write("\n")
                file.flush()
                print("Área romboide: %.2f" %(n6))
                print("")
    
        elif opcion == 7:
            file.write("Seleccionaste área de un trapecio \n")
            B = float(input("Introduce la base mayor: "))
            b = float(input("Introduce la base menor: "))
            h = float(input("Introduce la altura: "))
            if (B<=0 or b<=0 or h<=0):
                file.write("Input no valido\n")
                file.write("\n")
                file.flush()
                print("No valido")
                print("")
            else:
                n7=AreaTrapecio(B, b, h)
                file.write("Área trapecio: %.2f\n" %(n7))
                file.write("\n")
                file.flush()
                print("Área trapecio: %.2f" %(n7))
                print("")
    
        elif opcion == 8:
            file.write("Seleccionaste área de un polígono regular \n")
            n = float(input("Introduce el numero de lados: "))
            l = float(input("Introduce la longitud de los lados: "))
            a = float(input("Introduce la apotema: "))
            if (n<=0 or l<=0 or a<=0):
                file.write("Input no valido\n")
                file.write("\n")
                file.flush()
                print("No valido")
                print("")
            else:
                n8=AreaPregulares(n, l, a)
                file.write("Área polígono regular: %.2f\n" %(n8))
                file.write("\n")
                file.flush()
                print("Área polígono regular: %.2f" %(n8))
                print("")
            
        elif opcion == 9:
            file.write("Seleccionaste ver los divisores de un número asignado por tí \n")
            N=int(input("Introduce un número entero: "))
            if N<=0:
                file.write("Input no valido\n")
                file.write("\n")
                file.flush()
                print("No valido")
                print("")
            else:
                d=Divisores(N)
                d1=[str(n) for n in d]
                file.write("Estos son los divisores del número %d"%N)
                file.write(": ")
                file.write(", ".join(d1))
                file.write("\n")
                file.write("\n")
                file.flush()
                print("Estos son los divisores del número", N, ": " , end="")
                print(", ".join(d1))
                print("")
            
        elif opcion == 10:
            file.write("Seleccionaste ver los números pares que desees \n")
            p=int(input("¿Cuántos numeros pares quieres?: "))
            if p<=0:
                file.write("Input no valido\n")
                file.write("\n")
                file.flush()
                print("No valido")
                print("")
            else:
                NP=numerosPares(p)
                NP1=[str(N) for N in NP]
                file.write("Estos son sus números pares: ")
                file.write(', '.join(NP1))
                file.write('\n')
                file.write("\n")
                file.flush()
                print("Estos son sus números pares: ", end="")
                print(", ".join(NP1))
                print("")
    
        elif opcion == 11:
            file.write("Seleccionaste hacer una suma y resta \n")
            res=sumaresta()
            file.write("El resultado es: %.2f\n" %(res))
            file.write("\n")
            file.flush()
            print("El resultado es: ", res)
            print("")
            
        elif opcion == 12:
            file.write("Seleccionaste la función especial \n")
            feli=felicitaciones()
            file.write(feli)
            file.write("\n")
            file.flush()
    
        elif opcion == 13:
            file.write("Seleccionaste ver la media de un conjunto de valores \n")
            tam = int(input("¿Cuantos valores quieres sacarle la media? "))
            m = crea_lista(tam)
            med = media(m)
            file.write("La media es: %.2f\n" %(med))
            file.write("\n")
            file.flush()
            print("La media es %.2f" % med)
            print("")
        
        elif opcion == 14:
            file.write("Seleccionaste ver la moda de diferentes conjuntos \n")
            r=int(input("¿Cuántos valores tendra cada conjunto? "))
            c=int(input("¿Cuántos conjuntos van a ser? "))
            M=crear_matriz(r,c)
            mod=moda(M)
            file.write("La moda es: %.2f\n" %(mod))
            file.write("\n")
            file.flush()
            print("La moda es", mod)
            print("")
    
        elif opcion == 15:
            file.write("Seleccionaste ejecutar los casos de prueba \n")
            CdP=casosdeprueba()
            file.write(CdP)
            file.write("\n")
            file.flush()
            print("")
        
        elif opcion == 16:
            historial()
            print("")
        
        elif opcion == 17:
            file.write("Seleccionaste ejecutar la función secreta \n")
            cadena=str(input("Introduce tu nombre: "))
            caracter=str(input("\nIntroduce un caracter: "))
            n17=funcionsecreta(cadena, caracter)
            file.write("Las veces que se repite en tu nombre son: %d\n" %(n17))
            file.write("\n")
            file.flush()
            print("Las veces que", caracter, "se repite en tu nombre son", n17)
            print("Por cierto quería que supieras que a Calculareas le gusta tu nombre,", cadena, "<3")
            print("Te agradecemos mucho por usar nuestra aplicación ", cadena, ", nos ayudas mucho a crecer")
            print("                      \ U//u//U /                      ")
            print("")
            
        elif opcion == 0:
            file.close()
            print("¡Adios! Vuelve pronto")
            continua = False
        
        else:
            file.write("Seleccionaste una opción invalida \n")
            print("Opción inválida")

main()
