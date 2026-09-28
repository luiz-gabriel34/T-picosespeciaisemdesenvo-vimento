# ==========================================
# EXERCÍCIO 3
# ==========================================

# 1. Problema identificado:
# Tentar acessar um elemento de uma lista em uma posição fora dos seus limites
# lança a exceção 'IndexError'.

# 2. Algoritmo / Estratégia:
# Verificar se o índice informado está dentro do intervalo válido de 0 até (len(lista) - 1).
# (Caso queira proibir índices negativos do Python, verificar índice >= 0).

# 3. Código Python:
alunos = ["Ana", "Bruno", "Carla", "Daniel"]

def buscar_aluno(indice: int):
    if 0 <= indice < len(alunos):
        return f"Aluno encontrado na posição {indice}: {alunos[indice]}"
    else:
        return f"Erro: Posição {indice} é inválida. O intervalo válido é de 0 a {len(alunos) - 1}."

print(buscar_aluno(0))
print(buscar_aluno(3))
print(buscar_aluno(-1))
print(buscar_aluno(10))

# 4. Casos de Teste:
# Caso 1: indice=0   | Resp. Esperado: Ana         | Resp. Obtido: Ana         | Passou: Sim
# Caso 2: indice=3   | Resp. Esperado: Daniel      | Resp. Obtido: Daniel      | Passou: Sim
# Caso 3: indice=-1  | Resp. Esperado: Erro Índice | Resp. Obtido: Erro Índice | Passou: Sim
# Caso 4: indice=10  | Resp. Esperado: Erro Índice | Resp. Obtido: Erro Índice | Passou: Sim