# ==========================================
# EXERCÍCIO 9
# ==========================================

# 1. Problema identificado:
# Sobreposição de condições ou lacunas em valores limiares (fronteiras)[cite: 1].

# 2. Algoritmo / Estratégia:
# Organizar a estrutura condicional de forma decrescente/encadeada e usar `>=` e `<=`
# adequadamente para garantir cobrir exatamente todas as faixas sem brechas[cite: 1].

# 3. Código Python:
def classificar_desempenho(pontuacao: float):
    if pontuacao < 0 or pontuacao > 100:
        return "Pontuação fora do intervalo válido (0-100)."
    
    if pontuacao >= 90:
        return "Excelente"
    elif pontuacao >= 70:
        return "Bom"
    elif pontuacao >= 50:
        return "Regular"
    else:
        return "Insuficiente"

print(classificar_desempenho(90.0))
print(classificar_desempenho(89.9))
print(classificar_desempenho(70.0))
print(classificar_desempenho(50.0))

# 4. Casos de Teste:
# Caso 1: 90.0 | Resp. Esperado: Excelente    | Resp. Obtido: Excelente    | Passou: Sim
# Caso 2: 89.9 | Resp. Esperado: Bom          | Resp. Obtido: Bom          | Passou: Sim
# Caso 3: 70.0 | Resp. Esperado: Bom          | Resp. Obtido: Bom          | Passou: Sim
# Caso 4: 50.0 | Resp. Esperado: Regular      | Resp. Obtido: Regular      | Passou: Sim