# 1-Leia 2 números, representados pelas variáveis a e b.
# 2-Se a for maior que b, retorne a como maior.
# 3-Senão, retorne b

# def maximo2(a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
# # test
# print(maximo2(9, 3))
# print(maximo2(14, 99))

# 1-Leia 3 números, representados pelas variáveis a, b e c.
# 2-Se a for maior que b e a for maior que c, retorna a.
# 3-Senão, se b for maior que a e b for maior que c, retorna b.
# 4-Senão, retorna c

# def maximo3(a, b, c):
#     if a > b and a > c:
#         print(a)
#     elif b > a and b > c:
#         print(b)
#     else:
#         print(c)

# def maximo3(a, b, c):
#     if a < b:
#         return maximo3(b, c)
#     else:
#         return maximo3(a, c)
#
#
# maximo3(88, 4, 13)
# maximo3(10, 103, 77)
# maximo3(1, 43, 754)
