# --*-- coding: utf-8 -*-

#Algoritmo: Multiplo de un numero y suma de los mismos

def main():
    #visualizar todos los multiplos de 3 y lugo sumarlos

    Intro = """Bienvenido, este programa visualiza los multiplos de un número y su suma."""
    print(Intro)

    N = int(input('Ingresa un numero entero: '))
    rango = int(input('Ingresa el rango de los multiplos: '))

    multiplo = [i for i in range(N, rango) if i % N == 0] #list comprenhension
    a = f'Los multiplos de {N} son: '
    b = f'La suma de los multiplos de {N} es: '

    print(a, multiplo)
    print(b, sum(multiplo))


if __name__ == '__main__':
    main()