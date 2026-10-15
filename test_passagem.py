import pytest
from allpairspy import AllPairs
from passagem import preco

# Oráculo construído a partir da especificação correta
def esperado(idade, classe, malas, trecho):
    tarifa = 400.0 if trecho == "nacional" else 1500.0
    
    if classe == "executiva":
        tarifa *= 2.0
    
    if 0 <= idade <= 1:
        tarifa *= 0.10
    elif 2 <= idade <= 11:
        tarifa *= 0.75
        
    return round(tarifa + (100.0 * malas), 2)

# Modelos com os valores solicitados no exercício
REPRESENTANTES = [
    [1, 6, 40],
    ["economica", "executiva"],
    [0, 1, 2],
    ["nacional", "internacional"]
]

LIMITES = [
    [0, 1, 2, 11, 12, 120],
    ["economica", "executiva"],
    [0, 1, 2],
    ["nacional", "internacional"]
]

# Teste com o modelo REPRESENTANTES
@pytest.mark.parametrize("idade, classe, malas, trecho", AllPairs(REPRESENTANTES))
def test_representantes(idade, classe, malas, trecho):
    assert preco(idade, classe, malas, trecho) == esperado(idade, classe, malas, trecho)

# Teste com o modelo LIMITES
@pytest.mark.parametrize("idade, classe, malas, trecho", AllPairs(LIMITES))
def test_limites(idade, classe, malas, trecho):
    assert preco(idade, classe, malas, trecho) == esperado(idade, classe, malas, trecho)