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

    

