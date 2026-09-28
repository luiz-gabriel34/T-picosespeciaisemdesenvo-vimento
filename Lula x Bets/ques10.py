# ==========================================
# EXERCÍCIO 10
# ==========================================

# 1. Problema identificado:
# A variável de controle dentro do laço `while` não é atualizada a cada iteração,
# resultando em um laço infinito[cite: 1].

# 2. Algoritmo / Estratégia:
# Garantir que a leitura do novo número ocorra rigorosamente DENTRO do laço de repetição[cite: 1].

# 3. Código Python:
def executar_loop_solicitacao(entradas_simuladas: list):
    resultados = []
    i = 0
    while i < len(entradas_simuladas):
        num = entradas_simuladas[i]
        i += 1  # Atualização da variável de controle do loop
        
        if num == 0:
            resultados.append("Programa encerrado com 0.")
            break
        resultados.append(f"Número processado: {num}")
        
    return resultados

# 4. Casos de Teste:
# Caso 1: entradas=[0]        | Parou na 1ª iteração.  | Passou: Sim
# Caso 2: entradas=[5, 2, 0]  | Processou 5, 2 e parou | Passou: Sim