# ==========================================
# EXERCÍCIO 15
# ==========================================

# 1. Problema identificado:
# Usar `print()` dentro da função em vez de `return`. A função exibe o resultado no console,
# mas retorna `None`, impedindo reaproveitar o valor em outros cálculos[cite: 1].

# 2. Algoritmo / Estratégia:
# Modificar o escopo da função para utilizar a palavra-chave `return` devolvendo o valor da média[cite: 1].

# 3. Código Python:
def calcular_media_retorno(nota1: float, nota2: float) -> float:
    media = (nota1 + nota2) / 2.0
    return media  # Permite encadear resultados

# Testando reuso em outro cálculo (Ex: Bônus de 1 ponto):
media_aluno = calcular_media_retorno(7.0, 8.0)
media_final_com_bonus = media_aluno + 1.0  # Funciona perfeitamente porque media_aluno != None

print(calcular_media_retorno(7.0, 8.0))

# 4. Casos de Teste:
# Caso 1: nota1=7.0, nota2=8.0 -> Retorno: 7.5 | Usado no bônus: 8.5 | Passou: Sim