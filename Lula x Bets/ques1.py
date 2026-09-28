# ==========================================
# EXERCÍCIO 1
# ==========================================

# 1. Problema identificado:
# A função input() em Python retorna sempre uma string. Tentar usar essa entrada 
# diretamente em comparações numéricas sem converter ou tratar erros pode causar
# ValueError ou comportamentos lógicos incorretos.

# 2. Algoritmo / Estratégia:
# Receber a entrada, verificar se ela não está vazia e se pode ser convertida para número inteiro.
# Se válida, verificar se a idade está dentro de uma faixa razoável (> 0 e <= 120).
# Se inválida, exibir mensagem apropriada sem quebrar a execução do programa.

# 3. Código Python:
def validar_idade(entrada: str):
    entrada = entrada.strip()
    if not entrada:
        return "Erro: A entrada não pode estar vazia."
    try:
        idade = int(entrada)
        if idade <= 0:
            return "Erro: A idade deve ser um número inteiro positivo maior que zero."
        elif idade > 120:
            return "Erro: Idade fora do limite aceitável."
        
        if idade >= 18:
            return f"Idade {idade}: Permitido participar da atividade."
        else:
            return f"Idade {idade}: Não permitido (menor de idade)."
    except ValueError:
        return "Erro: Entrada inválida. Digite apenas um número inteiro."

# 4. Casos de Teste / Registro de Testes:
# Caso 1: Entrada = "20"   | Resp. Esperado: Permitido    | Resp. Obtido: Permitido    | Passou: Sim
# Caso 2: Entrada = "0"    | Resp. Esperado: Erro (>0)     | Resp. Obtido: Erro (>0)     | Passou: Sim
# Caso 3: Entrada = "-5"   | Resp. Esperado: Erro (>0)     | Resp. Obtido: Erro (>0)     | Passou: Sim
# Caso 4: Entrada = "abc"  | Resp. Esperado: Erro formato  | Resp. Obtido: Erro formato  | Passou: Sim
# Caso 5: Entrada = ""     | Resp. Esperado: Erro vazia    | Resp. Obtido: Erro vazia    | Passou: Sim