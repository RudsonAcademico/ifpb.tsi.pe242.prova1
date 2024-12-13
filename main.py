def q1():
    """
    Dado um número inteiro x, retorne verdadeiro se x for um palíndromo, e falso caso contrário.

    """
    x=input("")
    if x == x[::-1]:
        print(True)
    else:
        print(False)


def q2():
    """
    Dado um numeral romano, converta-o para um número inteiro.
    """
    s={
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000,
        }
    resultado=0
    romano = input('')
    anterior = romano[0]
    for x in romano:
        if s.get(anterior) < s.get(x):
            resultado-=s[anterior]*2
            resultado+=s[x]
        else:
            resultado+=s[x]
        anterior = x
        
            
    print(resultado)

def q3():
    """Faça um programa que calcula a quantidade de divisores de um número (incluindo 1 e o próprio número) que são divisíveis por 3."""
    n = int(input(''))
    r = 0
    metade = n//2
    for i in range(metade, 0, -1):
        if n % i == 0:
            if i % 3 == 0:
                r+=1
    resultado = 'O número não possui divisores multiplos de 3' if r == 0 and n != 3 else f'Quantidade de divisores divisiveis por 3: {r+1}'
    print(resultado)

def q4():
    """Escreva um programa que receba como entrada dois números inteiros e retorne a soma dos números positivos no intervalo definido por eles, considerando inclusive os extremos."""
    n1=int(input(''))
    n2=int(input(''))
    resultado=0
    maior = n1 if n1 >= n2 else n2
    menor = n1 if maior == n2 else n2
    for i in range(menor, maior+1):
        if i > 0:
            resultado+=i
    print(resultado)