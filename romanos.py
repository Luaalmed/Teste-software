SIMBOLOS = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (1, "I")
]

def para_romano(n):
    r = ""
    for valor, simbolo in SIMBOLOS:
        while n >= valor:
            r += simbolo
            n -= valor
    return r

VALOR = dict(M=1000, D=500, C=100, L=50, X=10, V=5, I=1)

def de_romano(s):
    total = 0
    for atual, prox in zip(s, s[1:] + " "):
        v = VALOR[atual]
        if prox != " " and v < VALOR[prox]:
            total -= v
        else:
            total += v
    return total