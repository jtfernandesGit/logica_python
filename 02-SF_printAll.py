# Programa para exibir a Sequência de Fibonacci até o enésimo termo,
# onde n é fornecido pelo usuário

# definir variavel da posição desejada na SF
n = int(input("Qual número da sequencia Fibonnaci deseja verificar: "))

# primeira posição
n1 = 0

# segunda posição
n2 = 1

# contador
count = 0

if n < 0:
    print("A posição não pode ser negativa")
elif n  == 1:
    print(f"Sequência de Fibonacci até {n}:{n1}")
else:
    print("Sequência de Fibonacci até {n}")
    while count < n:
        print(n1, end=',')
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
