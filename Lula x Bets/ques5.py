# ==========================================
# EXERCÍCIO 5
# ==========================================

# 1. Problema identificado:
# Aceitar valores fora do intervalo [0.0, 10.0] ou entradas não numéricas contamina a média do aluno.

# 2. Algoritmo / Estratégia:
# Converter a entrada para `float` tratando erros com `try-except`.
# Verificar se o número está entre 0.0 e 10.0. Depois, aplicar as faixas de aprovação.

# 3. Código Python:
def classificar_nota(entrada: str):
    try:
        nota = float(entrada.replace(",", "."))
        if nota < 0.0 or nota > 10.0:
            return "Erro: A nota deve estar estritamente entre 0.0 e 10.0."
        
        if nota >= 7.0:
            return f"Nota {nota:.1f}: Aprovado"
        elif nota >= 4.0:
            return f"Nota {nota:.1f}: Recuperação"
        else:
            return f"Nota {nota:.1f}: Reprovado"
    except ValueError:
        return "Erro: Digite um número decimal válido para a nota."

print(classificar_nota("-3"))
print(classificar_nota("-15"))
print(classificar_nota("0"))
print(classificar_nota("10"))
print(classificar_nota("5.5"))

# 4. Casos de Teste:
# Caso 1: entrada="-3"  | Resp. Esperado: Erro faixa | Resp. Obtido: Erro faixa | Passou: Sim
# Caso 2: entrada="15"  | Resp. Esperado: Erro faixa | Resp. Obtido: Erro faixa | Passou: Sim
# Caso 3: entrada="0"   | Resp. Esperado: Reprovado  | Resp. Obtido: Reprovado  | Passou: Sim
# Caso 4: entrada="10"  | Resp. Esperado: Aprovado   | Resp. Obtido: Aprovado   | Passou: Sim
# Caso 5: entrada="5.5" | Resp. Esperado: Recuperação| Resp. Obtido: Recuperação| Passou: Sim