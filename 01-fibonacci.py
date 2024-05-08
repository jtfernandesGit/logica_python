# Na Matemática, a Sucessão de Fibonacci (também conhecida como Sequência de Fibonacci),
# é uma  sequência  de  números  inteiros,  começando  normalmente  por  0  e  1,
# na  qual,  cada  termo subsequente corresponde à soma dos dois anteriores

# algoritmo
# Fn = Fn-1 + Fn-2

# Func python para encontrar o valor em qualquer posição Fibonacci
def findFibonacci(n):
    if n < 0:
        print("Entrada incorreta")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return findFibonacci(n-1) + findFibonacci(n-2)
    # uso de recursividade

#testing code
print(findFibonacci(5))
print(findFibonacci(21))
print(findFibonacci(32))