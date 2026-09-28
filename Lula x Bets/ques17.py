# ==========================================
# EXERCÍCIO 17
# ==========================================

# 1. Problema identificado:
# Inserção de dados inconsistentes como idades negativas, cursos sem nome ou ano fora da faixa escolar[cite: 1].

# 2. Algoritmo / Estratégia:
# Validar sequencialmente cada campo com regras de negócios explícitas[cite: 1].

# 3. Código Python:
def validar_cadastro_aluno(idade: int, curso: str, ano: int):
    erros = []
    
    if idade <= 0 or idade > 100:
        erros.append("Idade inválida.")
    if not curso or not curso.strip():
        erros.append("Curso não pode ser vazio.")
    if ano < 1 or ano > 4:
        erros.append("Ano escolar deve estar entre 1 e 4.")
        
    if erros:
        return f"Cadastro Rejeitado: {', '.join(erros)}"
    return "Cadastro de Aluno Válido!"

# 4. Casos de Teste:
# Válidos:
#   (17, "Informática", 3) -> Válido
#   (15, "Eletrotécnica", 1) -> Válido
#   (18, "Mineração", 4) -> Válido
# Inválidos:
#   (-2, "Informática", 3) -> Rejeitado (Idade)
#   (16, "", 2)           -> Rejeitado (Curso)
#   (17, "Química", 5)    -> Rejeitado (Ano)