# ==========================================
# EXERCÍCIO 7
# ==========================================

# 1. Problema identificado:
# O sistema aceita cadeias de texto com tamanho diferente de 11 dígitos ou que contenham letras[cite: 1].

# 2. Algoritmo / Estratégia:
# Remover caracteres de formatação (pontos, traços)[cite: 1].
# Verificar se a string resultante possui apenas dígitos (`isdigit()`) e se o tamanho exato é 11[cite: 1].

# 3. Código Python:
def validar_formato_cpf(cpf_str: str):
    limpo = cpf_str.replace(".", "").replace("-", "").strip()
    
    if not limpo.isdigit():
        return "Erro: O identificador deve conter apenas números."
    if len(limpo) != 11:
        return f"Erro: Tamanho incorreto ({len(limpo)} dígitos). Deve conter exatamente 11 dígitos."
        
    return f"Identificador {limpo} está no formato correto."

# 4. Casos de Teste:
# Caso 1: "12345"       | Resp. Esperado: Erro tamanho | Resp. Obtido: Erro tamanho | Passou: Sim
# Caso 2: "123456789012"| Resp. Esperado: Erro tamanho | Resp. Obtido: Erro tamanho | Passou: Sim
# Caso 3: "1234567890a" | Resp. Esperado: Erro letras  | Resp. Obtido: Erro letras  | Passou: Sim
# Caso 4: "12345678901" | Resp. Esperado: Formato ok   | Resp. Obtido: Formato ok   | Passou: Sim