# --*-- coding: utf-8 -*-

# Algoritmo: Multiplo de un numero y suma de esos multiplos

def main():
    # Bucle repeat-untill
    while True: # True indica que el bucle es infinito hasta que se cumpla la condicion "if" de abajo
        try:
            #Entradas
            numero = int(input('Escribe un numero entero: '))
            rango = int(input('¿hasta donde quieres hallar los multiplos? escribe un entero: '))

            if(numero < 0) or (rango < 0):
                print('!Atencion¡: uno o ambos valores que ingresaste es negativo, vuelve a ingresar los numeros')
        except:
            print('!Atencion¡: ingresa solo números enteros positivos')
            break
        
        if (numero  == int(numero) > 0) and (rango == int(rango) > 0):
            
            #Proceso
            multiplo = []
            for i in range(numero, rango):
                if i % numero == 0:
                    multiplo.append(i)
            #Salida
            print(f'Los multiplos de {numero} son:\n{multiplo}')
            print(f'La suma de los multiplos de {numero} es:\n{sum(multiplo)}')
            break
if __name__ == '__main__':
    main()