# ==========================================
# EXERCÍCIO 16
# ==========================================

# 1. Problema identificado:
# Tentar abrir um arquivo inexistente com `open()` lança a exceção `FileNotFoundError`[cite: 1].

# 2. Algoritmo / Estratégia:
# Envolver a leitura do arquivo em um bloco `try-except FileNotFoundError` para tratar
# graciosa e seguramente a ausência do arquivo[cite: 1].

# 3. Código Python:
def ler_arquivo_alunos(caminho_arquivo: str):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.readlines()
            return f"Sucesso! {len(conteudo)} linhas lidas do arquivo."
    except FileNotFoundError:
        return f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado. Verifique o caminho digitado."

# 4. Casos de Teste:
# Caso 1: caminho="arquivo_existente.txt" -> Sucesso ao ler.
# Caso 2: caminho="nao_existe.txt"       -> Captura FileNotFoundError e exibe erro amigável.