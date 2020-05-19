#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2
 
Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

def ej1():
    # Ejercicios de práctica con números

    '''
    Realice un calculadora, se ingresará por línea de comando dos números reales
    y se deberá calcular todas las operaciones entre ellos:
    - Suma
    - Resta
    - Multiplicación
    - División
    - Exponente/Potencia
    
    - Para todos los casos se debe imprimir en pantalla el resultado aclarando
      la operación realizada en cada caso y con que números se ha realizado la operación
      ej: La suma entre 4.2 y 6.5 es 10.7

    '''

    print("Ingrese el primer numero: ")
    num_1 = int(input())
    print("Ingrese el segundo numero: ")
    num_2 = int(input())

    suma = num_1 + num_2
    resta = num_1 - num_2
    multiplicacion = num_1 * num_2
    division = num_1 / num_2
    potencia = num_1 ** num_2
    
    print("La suma entre",num_1," y ",num_2," es ",suma)
    print("La resta entre",num_1," y ",num_2," es ",resta)
    print("La multiplicacion entre",num_1," y ",num_2," es ",multiplicacion)
    print("La divisionentre",num_1," y ",num_2," es ",division)
    print("La potencia entre",num_1," y ",num_2," es ",potencia)

def ej2():
    # Ejercicios de práctica numérica y cadenas
    
    '''
    Realice un programa que consulte por consola:
    - El nombre completo de la persona
    - El DNI de la persona
    - La edad de la persona
    - La altura de la persona

    Finalmente el programa debe imprimir dos líneas de texto por separado
    - En una línea imprimir el nombre completo y el DNI, aclarando de que campo se trata cada uno
            Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
    - En la segunda línea se debe imprimir el nombre completo, edad y altura de la persona
      Nuevamente debe aclarar el campo de cada uno, para el que lo lea entienda de que se
      está hablando.

    '''

    print("Ingrese sus nombres: ")
    nombres = str(input())
    print("")
    print("Ingrese su apellido: ")
    apellido = str(input())
    nombre_completo = nombres + " " + apellido
    print("")
    print("Ingrese su DNI:")
    documento = int(input())
    print("")
    print("Ingrese su edad:")
    edad = int(input())
    print("")
    print("Ingrese su altura expresada en metros, si es necesario con dos decimales")
    altura = float(input())
    print("")
    print("Nombre completo:",nombre_completo,"- DNI:",documento)
    print("")
    print("Nombre completo:",nombre_completo,"- Edad:",edad,"años","- Altura:",altura,"metros")
    print("")


def ej3():
    # Ejercicios de práctica con cadenas

    '''
    Realice un programa que determine cual sería el apellido de una persona
    si se ingresaran los dos nombres completos de sus padres.
    Dicha persona deberá tener los apellidos de ambos padres

    - Primero el programa debe consultar el nombre completo del padre_1
    - Luego el programa debe consultar el nombre completo del padre_2
    - Luego debe consultar el nombre del hijo/a
    - Debe extraer los apellidos de los padres
    - Luego formar el nombre completo del hijo/a utilizando los apellidos de sus padres
      y el nombre ingresado de dicha persona
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre completo recomendamos usar el método "split"
    Mostraremos un ejemplo:
    
    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca de este método que seguramente
    utilizarán mucho de acá en adelante. Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
        
    '''
    print("Ingrese nombres y apellido materno:")
    nombreAp_materno = str(input())
    print("")
    print("Ingrese nombres y apellido paterno:")
    nombreAp_paterno = str(input())
    print("")
    print("Ingrese nombre del hijo:")
    nombre = str(input())
    print("")

    ap_materno = nombreAp_materno.split()[-1]
    ap_paterno = nombreAp_paterno.split()[-1]
    print(nombre,ap_paterno,ap_materno)
    print("")


def ej4():
    # Ejercicios de práctica con cadenas

    '''
    Realice un programa que determine si una persona_2 es pariente de la persona_1
    Para facilitar el ejercicio solo ingresar un nombre y un apellido por persona
    Ingresar dichos datos como Nombre Apellido, es decir, primero el nombre y luego
    el apellido, separado por un espacio.
    - El programa debe consultar primero el nombre completo de la persona_1
    - Luego debe consultar el nombre completo de la persona_2
    - Debe extraer el apellido de la persona_2
    - Luego preguntar si apellido de la persona_2 está contenido en el nombre completo
      de la persona_1
    - En caso de contenerlo, son parientes
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre recomendamos usar el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca de este método que seguramente
    utilizarán mucho de acá en adelante. Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
    
        
    '''

    print("La primer persona debe ingresar su primer nombre y apellido paterno:")
    persona_1 = str(input())
    print("")
    print("La segunda persona debe ingresar su primer nombre y apellido paterno:")
    persona_2 = str(input())
    apPersona_2 = persona_2.split()[-1]
    print("")
    pariente = apPersona_2 in persona_1
    # pariente == "true"
    print("Estas personas son parientes?",pariente)
    print("")



def ej5():
    # Ejercicios de práctica con cadenas
       
    '''
    Realice un programa que reciba por consola su nombre completo
    e imprima en pantalla su nombre en los siguientes formatos:
    - Todas las letras en minúsculas
    - Todas las letras en mayúsculas
    - Solo la primera letra del nombre en mayúscula

    NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
    de strs:
    - lower
    - upper
    - capitalize

    Puede buscar en internet como usar en Python estos métodos.
    Les dejamos un el siguiente link que posee casos de uso de algunos de ellos:

    Link de referencia:
    https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

    Cualquier duda con estos métodos pueden consultarla por el campus
    

    '''

    print("Ingrese su nombre cpmpleto:")
    nombre = str(input())
    nombre_min = nombre.lower()
    nombre_may = nombre.upper()
    nombre_ini = nombre.capitalize()
    print("")
    print(nombre_min)
    print(nombre_may)
    print(nombre_ini)
    print("")


if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()