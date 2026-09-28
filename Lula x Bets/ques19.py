# ==========================================
# EXERCÍCIO 19
# ==========================================

# 1. Problema identificado:
# Garantir que 100% das ramificações (branches) do código sintático sejam testadas pelo menos uma vez[cite: 1].

# 2. Algoritmo / Estratégia:
# Estruturar múltiplos caminhos condicionais e construir casos de teste que forcem a execução de cada branch[cite: 1].

# 3. Código Python:
def avaliar_emprestimo_estudantil(idade: int, renda: float, cadastrado: bool):
    if not cadastrado:
        return "Caminho 1: Cadastro inativo." # Branch 1
    
    if idade < 18:
        return "Caminho 2: Requer autorização dos responsáveis." # Branch 2
        
    if renda < 1500.0:
        return "Caminho 3: Elegível para auxílio integral." # Branch 3
    else:
        return "Caminho 4: Elegível para auxílio parcial." # Branch 4

# 4. Casos de Teste Caixa-Branca (Cobertura de Código):
# Teste C1: (20, 1000.0, False) -> Testa Branch 1 | Passou: Sim
# Teste C2: (16, 1000.0, True)  -> Testa Branch 2 | Passou: Sim
# Teste C3: (20, 1000.0, True)  -> Testa Branch 3 | Passou: Sim
# Teste C4: (20, 2000.0, True)  -> Testa Branch 4 | Passou: Sim