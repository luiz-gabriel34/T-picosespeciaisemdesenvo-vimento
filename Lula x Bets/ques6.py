# ==========================================
# EXERCÍCIO 6
# ==========================================

# 1. Problema identificado:
# Falta de validação sobre a complexidade da senha e ausência de limite de tentativas
# (vulnerabilidade a ataques de força bruta)[cite: 1].

# 2. Algoritmo / Estratégia:
# Definir um limite máximo de 3 tentativas[cite: 1].
# Verificar se a senha inserida atende a critérios mínimos (mínimo de 6 caracteres) e bate com a cadastrada[cite: 1].

# 3. Código Python:
SENHA_CORRETA = "Senha123"

def autenticar_usuario(tentativas_entradas: list):
    max_tentativas = 3
    for i, senha in enumerate(tentativas_entradas):
        if i >= max_tentativas:
            return "Acesso bloqueado: Excesso de tentativas!"
        
        if len(senha) < 6:
            print(f"Tentativa {i+1}: Senha muito curta (mínimo 6 caracteres).")
            continue
            
        if senha == SENHA_CORRETA:
            return f"Acesso permitido na tentativa {i+1}!"
        else:
            print(f"Tentativa {i+1}: Senha incorreta.")
            
    return "Acesso negado: Tentativas esgotadas."

print(autenticar_usuario(["Senha123"]))
print(autenticar_usuario(["errada1", "errada2", "Senha123"]))
print(autenticar_usuario(["e1", "e2", "e3", "Senha123"]))

# 4. Casos de Teste:
# Caso 1: ["Senha123"]                       -> Permissão na 1ª tentativa.
# Caso 2: ["errada1", "errada2", "Senha123"] -> Permissão na 3ª tentativa.
# Caso 3: ["e1", "e2", "e3", "Senha123"]      -> Bloqueado por limite.