calcular_pg = lambda x: x*2

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# funcao map lista de progressao geometrica
pg = list(map(calcular_pg, numeros))

#exibir
for i in pg:
    print(i)