conjuntoA = {1, 2, "tres"}
conjuntoB = {"tres"}

#conjuntoA.add(5)
#print(conjuntoA)

#conjuntoB.clear()
#print(conjuntoB)

#conjuntoC = conjuntoA.issubset(conjuntoB)
#print(conjuntoC)

#conjuntoC = conjuntoA.union(conjuntoB)
#conjuntoC.pop() -> Elimina un elemento al azar
#print(conjuntoC)

conjuntoC = conjuntoA.union(conjuntoB)
conjuntoC.remove('tres')
print(conjuntoC)