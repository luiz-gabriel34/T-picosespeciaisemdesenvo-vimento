# ==========================================
# EXERCÍCIO 18
# ==========================================

# 1. Problema identificado:
# Verificar o correto cálculo do desconto sem acessar a implementação interna, focando nas especificações/fronteiras[cite: 1].

# 2. Algoritmo / Estratégia:
# Se valor <= 100, desconto = 0%.
# Se valor > 100, desconto = 10%.

# 3. Código Python:
def calcular_valor_compra(valor: float):
    if valor < 0:
        return "Valor inválido"
    if valor > 100.0:
        return valor * 0.90  # 10% de desconto
    return valor

# 4. Casos de Teste Caixa-Preta (Entrada | Esperado):
# - Fronteira Inferior:  100.00 -> R$ 100.00 (sem desconto)
# - Fronteira Superior: 100.01 -> R$ 90.009 (com desconto)
# - Caso Normal:        200.00 -> R$ 180.00 (com desconto)
# - Entrada Inesperada:  -50.00 -> "Valor inválido"