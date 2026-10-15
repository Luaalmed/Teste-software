from hypothesis import given, strategies as st
from romanos import para_romano, de_romano

# --- Alínea A: Propriedade de Ida e Volta ---
@given(st.integers(min_value=1, max_value=3999))
def test_ida_e_volta(n):
    # Converte para romano e de volta para inteiro
    # Esta propriedade PASSA, porque o erro no código é simétrico[cite: 15, 16]
    assert de_romano(para_romano(n)) == n

# --- Alínea B e C: Nova Propriedade e Contraexemplo ---
@given(st.integers(min_value=1, max_value=3999))
def test_formato_valido(n):
    romano = para_romano(n)
    
    # Propriedade do formato: Numerais romanos não repetem o mesmo símbolo 4 vezes seguidas
    # (Exceção seria para números maiores que 3999 com 'M', mas o limite é 3999)[cite: 13, 15]
    assert "IIII" not in romano
    assert "XXXX" not in romano
    assert "CCCC" not in romano
    
    # Ao correr o pytest, esta propriedade vai falhar.
    # O contraexemplo gerado pelo Hypothesis será o número 4 (ou números que contêm 4, como 14, 24).