def top_k(lista, k):
    return sorted(lista, reverse=True)[:k]

def versao_a(lista, k):
    return sorted(set(lista), reverse=True)[:k]

def versao_b(lista, k):
    if k == 0:
        return []
    return sorted(lista)[-k:]

def versao_c(lista, k):
    return sorted(lista)[-k:][::-1]

def versao_d(lista, k):
    if not lista:
        return []
    limiar = sorted(lista, reverse=True)[k - 1]
    maiores = [x for x in lista if x >= limiar]
    return sorted(maiores, reverse=True)