# ==========================================
# EXERCÍCIO 11
# ==========================================

# 1. Problema identificado:
# Inicialização incorreta do contador ou inclusão/exclusão equivocada de limites (Off-by-one error)[cite: 1].

# 2. Algoritmo / Estratégia:
# Inicializar o contador em 0 e usar `range(1, N + 1)` para garantir que o limite superior `N`
# seja considerado na verificação[cite: 1].

# 3. Código Python:
def contar_pares(n: int):
    if n < 1:
        return 0
    
    contador_pares = 0
    # range(1, n + 1) garante que N está incluído no teste
    for i in range(1, n + 1):
        if i % 2 == 0:
            contador_pares += 1
            
    return contador_pares

# 4. Casos de Teste:
# Caso 1: N = 1  | Pares esperados (1..1): 0 | Resp. Obtido: 0 | Passou: Sim
# Caso 2: N = 2  | Pares esperados (1..2): 1 | Resp. Obtido: 1 | Passou: Sim
# Caso 3: N = 10 | Pares esperados (1..10): 5| Resp. Obtido: 5 | Passou: Sim