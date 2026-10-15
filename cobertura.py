from itertools import combinations

def combinacoes_de(casos, t):
    """
    Recebe uma lista de casos gerados e o tamanho t (ex: 3 para triplas).
    Devolve um conjunto (set) com todas as t-uplas únicas cobertas, 
    guardando os índices dos parâmetros para garantir a distinção.
    """
    cobertas = set()
    for caso in casos:
        n = len(caso)
        # O combinations gera as combinações dos índices dos parâmetros[cite: 6]
        # Ex: (0, 1, 2) -> idade, classe, malas
        for indices in combinations(range(n), t):
            # Extrai os valores correspondentes a esses índices
            valores = tuple(caso[i] for i in indices)
            # Guarda a tupla de (índices, valores) para ser única
            cobertas.add((indices, valores))
            
    return cobertas