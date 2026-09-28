# ==========================================
# EXERCÍCIO 14
# ==========================================

# 1. Problema identificado:
# Operações matemáticas com valores `None`, strings vazias ou apenas com espaços causam falhas de execução (`TypeError`/`ValueError`)[cite: 1].

# 2. Algoritmo / Estratégia:
# Criar uma função de validação que verifica se o valor é nulo ou se, após aplicar `.strip()`, a string fica vazia[cite: 1].

# 3. Código Python:
def processar_cadastro_produto(nome: str, preco_str: str):
    if nome is None or not nome.strip():
        return "Erro: O nome do produto é obrigatório."
        
    if preco_str is None or not preco_str.strip():
        return "Erro: O preço do produto está ausente."
        
    try:
        preco = float(preco_str.strip().replace(",", "."))
        return f"Produto '{nome.strip()}' cadastrado com sucesso por R$ {preco:.2f}."
    except ValueError:
        return "Erro: Valor numérico inválido para o preço."

# 4. Casos de Teste:
# Caso 1: nome="Arroz", preco="10.50" | Resp: Sucesso             | Passou: Sim
# Caso 2: nome="", preco="10.50"      | Resp: Erro nome           | Passou: Sim
# Caso 3: nome="Feijão", preco="   "  | Resp: Erro preço ausente  | Passou: Sim