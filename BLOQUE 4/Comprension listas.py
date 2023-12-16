valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_cuadrados=[n**2 for n in valores]
valores_pares = [n for n in valores if n%2==0 ]

print(valores_cuadrados)
print(valores_pares)