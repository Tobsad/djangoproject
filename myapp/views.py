from django.shortcuts import render
from django.http import HttpResponse

#imports
import random

# Vistas.
#Ejercicios For
def ejercicio1(request):
    lista=[]
    n = random.randint(1, 10)
    for i in range(1, n):
        lista.append(i)
    return HttpResponse(lista)

def ejercicio2(request):
    suma = 0
    n = random.randint(1, 20)
    for i in range(1, n):
        suma += i
    return HttpResponse(f"La suma de los {n-1} numeros es {suma} ")   

def ejercicio3(request):
    nombres = ["Ana", "Pedro", "María", "Juan","Christian","Mark","Sebastian","David"]
    for nombre in nombres:
        i = random.randint(0, 7)
    return HttpResponse(nombres[i]) 

def ejercicio4(request):
    numero = ["Primero", "Segundo", "Tercero", "Cuarto", "Quinto"]
    for i in range(len(numero)):
        i = random.randint(0, 4)
    return HttpResponse(f"El número en la posición {i+1} es {numero[i]}")

def ejercicio5(request):
    n = random.randint(0, 10)
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return HttpResponse(f"El factorial de {n} es {factorial}")
#Ejercicios While
def ejercicio6(request):
    numeros = [23, 45, 67, 1, 34, 56, 78, 9]
    maximo = numeros[0]
    i = 1
    while i < len(numeros):
        if numeros[i] > maximo:
            maximo = numeros[i]
        i += 1
    return HttpResponse(f"El número más grande es:{maximo}")

def ejercicio7(request):
    n = random.randint(1, 50)
    es_primo = True
    i = 2
    while i <= n // 2:
        if n % i == 0:
            es_primo = False
            break
        i += 1
    if es_primo:
        s="El número ", n,"  es primo"
        respuesta7=s
    else:
        n="El número ",n ," no es primo"
        respuesta7=n
    return HttpResponse(respuesta7)

def ejercicio8(request):
    cadena = "Hola mundo"
    while True:
        inverso= ''.join(reversed(cadena))
        print(inverso) # salida: odnum aloH
        return HttpResponse(f"La palabra es {cadena} y su inverso es {inverso}")

def ejercicio9(request):
    n = random.randint(0, 10)
    a, b = 0, 1
    ultimo=[]
    while a <= n:
        ultimo.append(a)
        a, b = b, a+b
    
    return HttpResponse(ultimo)

def ejercicio10(request):
    numero = random.randint(9, 50)
    inicial=numero
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    return HttpResponse(f"El usuario dio el numero {inicial} y la suma de los dígitos es: {suma} ")

def ejercicio11(request):
    cadena = "anitalavalatina"
    i, j = 0, len(cadena) - 1
    es_palindromo = True
    while i < j:
        if cadena[i] != cadena[j]:
            es_palindromo = False
            break
        i += 1
        j -= 1
    if es_palindromo:
        palindromo="La cadena es un palíndromo"
    else:
        palindromo="La cadena no es un palíndromo"
    return HttpResponse(palindromo)

def ejercicio12(request):
    cadena = "esternocleidomastoideo"
    letra = "o"
    contador = 0
    indice = 0
    while indice < len(cadena):
        if cadena[indice] == letra:
            contador += 1
        indice += 1
    return HttpResponse(f"La letra {letra} aparece {contador} veces en la cadena")

def ejercicio13(request):
    password = "123456789"
    if int(len(password))>=8 :
        valido="Enhorabuena!, su contraseña es segura ya que posee mas de 8 digitos"
    else:
        valido="no contiene 8 caracteres"
    return HttpResponse(f"Se analizo su contraseña y es {valido}")

def ejercicio14(request):
    numero_aleatorio = random.randint(1, 11)
    adivinado = False

    while not adivinado:
        numero_adivinado = 5
        if numero_adivinado > numero_aleatorio:
            respuesta= "Demasiado alto"
        elif numero_adivinado < numero_aleatorio:
            respuesta= "Demasiado bajo"
        else:
            respuesta= "¡Felicidades, lo has adivinado!"
        adivinado = True
    return HttpResponse(f"El numero aleatorio era: {numero_aleatorio}, su numero fue: {numero_adivinado} asi que su respuesta es: {respuesta}")

def ejercicio15(request):
    #superusuario:
    username = "Tobsad"
    #usuario ingresado
    usuario_ingresado="Tobsad"    
    adivinado = False
    while not adivinado:
        if usuario_ingresado != username:
            ingresado=f"Acceso denegado, El usuario: {usuario_ingresado} no tiene permisos de superusuario."
        else:
            ingresado=f"Acceso concedido, Bienvenido {username}"
        adivinado = True
    return HttpResponse(f"El  nombre del usuario es {username} y usted ingreso {usuario_ingresado}. Asi que:{ingresado}")

#todas las vistas
def vista_compuesta(request):
    resultado1 = ejercicio1(request).content.decode('utf-8')
    resultado2 = ejercicio2(request).content.decode('utf-8')
    resultado3 = ejercicio3(request).content.decode('utf-8')
    resultado4 = ejercicio4(request).content.decode('utf-8')
    resultado5 = ejercicio5(request).content.decode('utf-8')
    resultado6 = ejercicio6(request).content.decode('utf-8')
    resultado7 = ejercicio7(request).content.decode('utf-8')
    resultado8 = ejercicio8(request).content.decode('utf-8')
    resultado9 = ejercicio9(request).content.decode('utf-8')
    resultado10 = ejercicio10(request).content.decode('utf-8')
    resultado11 = ejercicio11(request).content.decode('utf-8')
    resultado12 = ejercicio12(request).content.decode('utf-8')
    resultado13 = ejercicio13(request).content.decode('utf-8')
    resultado14 = ejercicio14(request).content.decode('utf-8')
    resultado15 = ejercicio15(request).content.decode('utf-8')
    # resultado3 =
    edad=30
    context={
        'resultado1': resultado1, 
        'resultado2': resultado2, 
        'resultado3': resultado3, 
        'resultado4': resultado4,
        'resultado5': resultado5, 
        'resultado6': resultado6,
        'resultado7': resultado7, 
        'resultado8': resultado8, 
        'resultado9': resultado9, 
        'resultado10': resultado10, 
        'resultado11': resultado11, 
        'resultado12': resultado12,
        'resultado13': resultado13, 
        'resultado14': resultado14, 
        'resultado15': resultado15, 
        'edad':edad
        }
    return render(request, 'mi_template.html', context)

def autor(request):
    autor="Tobsad"
    context={'autor':autor}
    return render(request, 'home.html',context)