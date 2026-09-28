# ==========================================
# EXERCÍCIO 13
# ==========================================

# 1. Problema identificado:
# Inicializar `maior` com 0 pode falhar se todas as temperaturas forem negativas[cite: 1].

# 2. Algoritmo / Estratégia:
# Inicializar `maior` e `menor` com o primeiro elemento da lista e percorrer o restante dos itens[cite: 1].

# 3. Código Python:
def encontrar_extremos_temperatura(temperaturas: list):
    if not temperaturas:
        return "Erro: A lista de temperaturas está vazia."
    
    maior = temperaturas[0]
    menor = temperaturas[0]
    
    for temp in temperaturas[1:]:
        if temp > maior:
            maior = temp
        if temp < menor:
            menor = temp
            
    return f"Maior temperatura: {maior}°C, Menor temperatura: {menor}°C"

# 4. Casos de Teste:
# Caso 1: [25.0, 30.0, 15.0]     | Maior: 30.0, Menor: 15.0  | Passou: Sim
# Caso 2: [-5.0, -12.0, -2.0]    | Maior: -2.0, Menor: -12.0 | Passou: Sim
# Caso 3: [20.0, 20.0, 20.0]     | Maior: 20.0, Menor: 20.0  | Passou: Sim