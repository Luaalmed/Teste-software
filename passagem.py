def preco(idade, classe, malas, trecho):
    tarifa = 400 if trecho == "nacional" else 1500
    if classe == "executiva":
        tarifa *= 2
    if idade <= 2:
        tarifa *= 0.10
    elif idade <= 11 and classe == "economica":
        tarifa *= 0.75
    return round(tarifa + 100 * malas, 2)