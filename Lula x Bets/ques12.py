# ==========================================
# EXERCÍCIO 12
# ==========================================

# 1. Problema identificado:
# Registros duplicados inseridos por erro humano ou inconsistência na coleta de dados[cite: 1].

# 2. Algoritmo / Estratégia:
# Iterar sobre a lista contando a frequência dos elementos ou utilizar conjuntos (`set`)
# para identificar quais nomes aparecem mais de uma vez[cite: 1].

# 3. Código Python:
def identificar_duplicados(lista_nomes: list):
    vistos = set()
    duplicados = set()
    
    for nome in lista_nomes:
        nome_normalizado = nome.strip().title()
        if nome_normalizado in vistos:
            duplicados.add(nome_normalizado)
        else:
            vistos.add(nome_normalizado)
            
    if duplicados:
        return f"Atenção, nomes duplicados encontrados: {list(duplicados)}"
    return "Nenhum nome duplicado na lista."

# 4. Casos de Teste:
# Caso 1: ["Ana", "Bruno", "Carla"]         | Resp. Esperado: Nenhum duplicado | Passou: Sim
# Caso 2: ["Ana", "Bruno", "Ana"]           | Resp. Esperado: ['Ana']          | Passou: Sim
# Caso 3: ["Ana", "Ana", "Bruno", "Bruno"]  | Resp. Esperado: ['Ana', 'Bruno'] | Passou: Sim