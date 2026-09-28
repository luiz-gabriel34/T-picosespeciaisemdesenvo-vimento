# ==========================================
# EXERCÍCIO 20 (CÓDIGO COM ERROS INTENCIONAIS & VERSÃO CORRIGIDA)
# ==========================================

# 1. Código com 5 Erros Propositais (Versão para Testador):
"""
def cadastrar_aluno_bugado():
    nome = input("Nome: ") # Erro 1: Não valida string vazia
    idade = int(input("Idade: ")) # Erro 2: ValueError se digitar texto
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    
    media = n1 + n2 + n3 / 3 # Erro 3: Erro de lógica na média (faltam parênteses)
    
    if media > 7.0: # Erro 4: Erro de fronteira (deveria ser >= 7.0 para aprovação)
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
        
    print(alunos[10]) # Erro 5: Exceção (IndexError) proposital
"""

# 2. Versão Corrigida:
def sistema_cadastro_aluno_corrigido(nome: str, idade_str: str, n1_str: str, n2_str: str, n3_str: str):
    # Validação Nome
    if not nome or not nome.strip():
        return "Erro: O nome do aluno não pode ser vazio."
    
    # Validação Idade
    try:
        idade = int(idade_str)
        if idade <= 0 or idade > 120:
            return "Erro: Idade inválida."
    except ValueError:
        return "Erro: Idade deve ser um número inteiro."
        
    # Validação e Cálculo de Notas
    try:
        n1 = float(n1_str)
        n2 = float(n2_str)
        n3 = float(n3_str)
        
        for n in [n1, n2, n3]:
            if n < 0.0 or n > 10.0:
                return "Erro: As notas devem estar entre 0 e 10."
                
        # Correção do Cálculo da Média
        media = (n1 + n2 + n3) / 3.0
        
        # Correção da Condição de Fronteira
        if media >= 7.0:
            situacao = "Aprovado"
        elif media >= 4.0:
            situacao = "Recuperação"
        else:
            situacao = "Reprovado"
            
        return {
            "Aluno": nome.strip(),
            "Idade": idade,
            "Média": round(media, 2),
            "Situação": situacao
        }
    except ValueError:
        return "Erro: As notas devem ser numéricas."

# 3. Tabela de Casos de Teste (Resumida):
# | Entrada (N, I, N1, N2, N3)  | Esperado             | Obtido               | Status |
# | ("", "18", "7", "7", "7")   | Erro Nome            | Erro Nome            | OK     |
# | ("Ana", "abc", "7", "7", "7")| Erro Idade           | Erro Idade           | OK     |
# | ("Ana", "18", "7", "7", "7") | Média 7.0 (Aprovado) | Média 7.0 (Aprovado) | OK     |