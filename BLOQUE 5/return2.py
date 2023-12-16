def usd_a_eur(monto):
    resultado = monto*0.90
    return resultado

valor = int(input("Ingresa tu cantidad en dolares"))
dolares = usd_a_eur(valor)

print(f" {valor} dolares son {dolares} euros")