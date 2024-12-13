n1=int(input(''))
n2=int(input(''))
resultado=0
maior = n1 if n1 >= n2 else n2
menor = n1 if maior == n2 else n2
for i in range(menor, maior+1):
    if i > 0:
        resultado+=i
print(resultado)