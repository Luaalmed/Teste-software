import pytest
from itertools import product
from allpairspy import AllPairs
from cobertura import combinacoes_de

LIMITES = [
    [0, 1, 2, 11, 12, 120], # Idade
    ["economica", "executiva"], # Classe
    [0, 1, 2], # Malas
    ["nacional", "internacional"] # Trecho
]

def test_cobertura_triplas():
    # --- Alínea B: Universo de triplas e fração coberta pelo Pairwise padrão ---
    # 1. Calcula todas as triplas possíveis usando o produto completo[cite: 11]
    produto_completo = list(product(*LIMITES))
    triplas_totais = combinacoes_de(produto_completo, 3)
    total = len(triplas_totais)
    
    # 2. Calcula as triplas que o Pairwise normal (t=2) cobriu por acaso[cite: 11]
    casos_pairwise = list(AllPairs(LIMITES))
    triplas_pairwise = combinacoes_de(casos_pairwise, 3)
    
    fracao_coberta = len(triplas_pairwise) / total
    print(f"\n[Alínea B] Total de triplas possíveis: {total}")
    print(f"[Alínea B] Triplas cobertas pelo Pairwise (t=2): {len(triplas_pairwise)}")
    print(f"[Alínea B] Fração coberta (t=2): {fracao_coberta:.2%} (Esperado: 56%[cite: 16])")
    
    # --- Alínea C: Casos mínimos vs Pairwise vs Produto Completo ---
    # Produto completo: 6 * 2 * 3 * 2 = 72 casos[cite: 10]
    # O mínimo para cobrir todas as triplas é ditado pela maior tripla de parâmetros (6 * 3 * 2 = 36 casos).
    print(f"[Alínea C] Casos no Produto Completo: {len(produto_completo)}")
    print(f"[Alínea C] Casos no Pairwise (t=2): {len(casos_pairwise)}")
    print(f"[Alínea C] Mínimo teórico para t=3: Pelo menos 36 casos")
    
    # --- Alínea D: Testar o AllPairs com n=3 ---
    casos_allpairs_n3 = list(AllPairs(LIMITES, n=3))
    triplas_allpairs_n3 = combinacoes_de(casos_allpairs_n3, 3)
    fracao_n3 = len(triplas_allpairs_n3) / total
    
    print(f"[Alínea D] Casos gerados pelo AllPairs(n=3): {len(casos_allpairs_n3)}")
    print(f"[Alínea D] Fração coberta pelo AllPairs(n=3): {fracao_n3:.2%}")
    
    # A síntese diz que a ferramenta com n=3 "não entregou o que prometia"[cite: 16].
    # O assert abaixo verifica exatamente isso: o número de triplas cobertas será MENOR que o total[cite: 11, 16].
    assert len(triplas_allpairs_n3) < total, "A ferramenta deveria ter falhado em cobrir 100%"