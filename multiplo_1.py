# --*-- coding: utf-8 -*-

# Algoritmo: Multiplo de un numero y suma de esos multiplos

def main():
    # Bucle repeat-untill
    while True: # True indica que el bucle es infinito hasta que se cumpla la condicion "if" de abajo
        try:
            #Entradas
            numero = int(input('\n* Escribe el numero entero positivo al que le vas hallar los multiplos: '))
            rango = int(input('* ¿hasta donde quieres hallar los multiplos? escribe un numero entero positivo: '))

            if(numero < 0) or (rango < 0):
                print('\n!Atencion¡: <<Uno o ambos valores que ingresaste es negativo, vuelve a ingresar los numeros>> 😔')
        except:
            print('\n!Atencion¡: <<Ingresa solo números enteros positivos>> 😞')
            main() #al aplicar recursividad, me permite no romper el codigo subitamente, y ejecutar las instrucciones varias veces mas
            break 
        
        
        if (numero  == int(numero) > 0) and (rango == int(rango) > 0):
            
            #Proceso
            multiplo = []
            for i in range(numero, rango):
                if i % numero == 0:
                    multiplo.append(i)
            #Salida
            print(f'\n* Los multiplos de {numero} son:\n{multiplo} 🥳')
            print(f'\n* La suma de los multiplos de {numero} es: {sum(multiplo)} 🥳')
            break
    
def evaluar_intro(intro):
    while intro == 'si':
        main()
        intro = input('¿Deseas seguir en el programa? si/no: ')
        evaluar_intro(intro)
        break
    else:
        if intro == 'no':
            print('\n!Adios¡ 😎\n')
        elif (intro != 'si') or (intro != 'no'):
            print('\n* Ingresa "si" o "no" por favor')
            intro = input('¿Deseas seguir en el programa? si/no: ')
            evaluar_intro(intro)
            
def run():
    introduccion = """
    *********************** MULTIPLO *************************
                Hola y Bienvenido a MULTIPLO 😊\n
        Este es un programa que halla los multiplos de 
        cualquier numero y tambien suma los multiplos hallados\n
    **********************************************************
    """
    print(introduccion)
    main()
    intro = input('¿Deseas seguir en el programa? si/no: ')
    evaluar_intro(intro)

if __name__ == '__main__':
    run()