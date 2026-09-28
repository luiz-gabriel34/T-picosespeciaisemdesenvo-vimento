# ==========================================
# EXERCÍCIO 8
# ==========================================

# 1. Problema identificado:
# Precedência de operadores. Escrever `n1 + n2 + n3 / 3` faz com que apenas `n3` seja
# dividido por 3 antes de somar com os outros números[cite: 1].

# 2. Algoritmo / Estratégia:
# Utilizar parênteses para forçar a prioridade de adição: `(n1 + n2 + n3) / 3`[cite: 1].

# 3. Código Python:
def calcular_media_tres_notas(n1: float, n2: float, n3: float):
    # Errado: media = n1 + n2 + n3 / 3
    media_correta = (n1 + n2 + n3) / 3.0
    return media_correta

print(calcular_media_tres_notas(6.0, 6.0, 6.0))

# 4. Casos de Teste:
# Caso 1: n1=6.0, n2=6.0, n3=6.0
#   - Sem parênteses: 6 + 6 + (6/3) = 14.0 (Incorreto)
#   - Com parênteses: (6 + 6 + 6) / 3 = 6.0 (Correto) | Passou: Sim