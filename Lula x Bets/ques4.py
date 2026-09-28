# ==========================================
# EXERCÍCIO 4
# ==========================================

# 1. Problema identificado:
# Se o usuário digitar caracteres não numéricos ou formatar com vírgula (ex: "10,50"),
# a conversão `float()` lança `ValueError`.

# 2. Algoritmo / Estratégia:
# Tratar a entrada substituindo vírgulas por pontos, remover espaços das pontas
# e utilizar `try-except` para capturar exceções durante a conversão.

# 3. Código Python:
def processar_preco(entrada: str):
    texto_limpo = entrada.strip().replace(",", ".")
    try:
        preco = float(texto_limpo)
        if preco < 0:
            return "Erro: O preço não pode ser negativo."
        return f"Preço válido: R$ {preco:.2f}"
    except ValueError:
        return "Erro: Entrada inválida! Digite apenas valores numéricos."

print(processar_preco("100"))
print(processar_preco("25.50"))
print(processar_preco("12,30"))
print(processar_preco("abc"))

# 4. Casos de Teste:
# Caso 1: entrada="100"      | Resp. Esperado: R$ 100.00 | Resp. Obtido: R$ 100.00 | Passou: Sim
# Caso 2: entrada="25.50"    | Resp. Esperado: R$ 25.50  | Resp. Obtido: R$ 25.50  | Passou: Sim
# Caso 3: entrada="  12,30 " | Resp. Esperado: R$ 12.30  | Resp. Obtido: R$ 12.30  | Passou: Sim
# Caso 4: entrada="abc"      | Resp. Esperado: Erro form.| Resp. Obtido: Erro form.| Passou: Sim