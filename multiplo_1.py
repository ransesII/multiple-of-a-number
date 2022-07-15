# --*-- coding: utf-8 -*-

# Algoritmo: Multiplo de un numero y suma de esos multiplos

def main():
    #Entradas
    numero = int(input('Escribe un numero entero: '))
    rango = int(input('¿hasta donde quieres hallar los multiplos? escribe un entero: '))
    #Proceso
    multiplo = []
    for i in range(numero, rango):
        if i % numero == 0:
            multiplo.append(i)
    #Salida
    print(f'Los multiplos de {numero} son:\n{multiplo}')
    print(f'La suma de los multiplos de {numero} es:\n{sum(multiplo)}')

if __name__ == '__main__':
    main()