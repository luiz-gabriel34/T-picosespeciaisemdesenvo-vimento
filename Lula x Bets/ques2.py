# ==========================================
# EXERCÍCIO 2
# ==========================================

# 1. Problema identificado:
# Tentar dividir qualquer valor numérico por zero lança a exceção 'ZeroDivisionError',
# interrompendo a execução do programa.

# 2. Algoritmo / Estratégia:
# Verificar o divisor (quantidade de notas) antes da operação matemática.
# Caso a quantidade seja zero, interromper a operação e avisar o usuário com mensagem amigável.

# 3. Código Python:
def calcular_media(soma_notas: float, quantidade_notas: int):
    if quantidade_notas <= 0:
        return "Erro: A quantidade de notas deve ser maior que zero (evita divisão por zero)."
    
    media = soma_notas / quantidade_notas
    return f"Média calculada: {media:.2f}"

print(calcular_media(15.0, 2))
print(calcular_media(20.0, 0))

# 4. Casos de Teste:
# Caso 1: soma=15.0, qtd=2 | Resp. Esperado: Média 7.50 | Resp. Obtido: Média 7.50 | Passou: Sim
# Caso 2: soma=20.0, qtd=0 | Resp. Esperado: Erro Qtd   | Resp. Obtido: Erro Qtd   | Passou: Sim