import pytest
from hypothesis import given, strategies as st
from collections import Counter
from topk import top_k, versao_a, versao_b, versao_c, versao_d

# Lista com todas as versões para a parametrização
FUNCOES = [top_k, versao_a, versao_b, versao_c, versao_d]

# Estratégia de geração: tuplos com uma lista de inteiros e um inteiro k de 0 a 10
estrategia_dados = st.tuples(st.lists(st.integers()), st.integers(min_value=0, max_value=10))

def preparar_dados(dados):
    lista, k = dados
    # Ajusta o k para ficar entre 0 e len(lista)
    k = min(k, len(lista))
    return lista, k

# 1. Propriedade: O tamanho do resultado deve ser exatamente k
@pytest.mark.parametrize("funcao", FUNCOES)
@given(dados=estrategia_dados)
def test_prop_tamanho(funcao, dados):
    lista, k = preparar_dados(dados)
    resultado = funcao(lista, k)
    assert len(resultado) == k

# 2. Propriedade: O resultado deve estar em ordem decrescente
@pytest.mark.parametrize("funcao", FUNCOES)
@given(dados=estrategia_dados)
def test_prop_ordem_decrescente(funcao, dados):
    lista, k = preparar_dados(dados)
    resultado = funcao(lista, k)
    assert resultado == sorted(resultado, reverse=True)

# 3. Propriedade: Todo o elemento vem da lista (respeitando as repetições)[cite: 20]
@pytest.mark.parametrize("funcao", FUNCOES)
@given(dados=estrategia_dados)
def test_prop_elementos(funcao, dados):
    lista, k = preparar_dados(dados)
    resultado = funcao(lista, k)
    contagem_lista = Counter(lista)
    contagem_resultado = Counter(resultado)
    # Garante que nenhum elemento aparece mais vezes no resultado do que na lista original
    for elemento, quantidade in contagem_resultado.items():
        assert quantidade <= contagem_lista[elemento]

# 4. Oráculo: O resultado deve ser idêntico à implementação correta com sorted[cite: 20]
@pytest.mark.parametrize("funcao", FUNCOES)
@given(dados=estrategia_dados)
def test_oraculo(funcao, dados):
    lista, k = preparar_dados(dados)
    resultado = funcao(lista, k)
    esperado = sorted(lista, reverse=True)[:k]
    assert resultado == esperado