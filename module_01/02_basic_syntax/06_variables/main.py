"""
Aula 06: Variáveis em Python

Explora a criação, nomenclatura e atribuição de variáveis, fundamentais para armazenar e manipular dados.
Seguimos 'The Zen of Python': explícito é melhor que implícito.
"""

# Exemplo 1: Atribuição simples de valores a variáveis
nome_usuario = "Maria"  # Atribui uma string (texto) à variável
idade_usuario = 28      # Atribui um número inteiro à variável
print(f"Usuário: {nome_usuario}, Idade: {idade_usuario}")  # Exibe os valores atribuídos

# Exemplo 2: Nomenclatura correta (seguindo PEP 8)
# Use letras minúsculas, underscores (_) para separar palavras, e nomes descritivos
email_principal = "maria@email.com"  # Correto: claro e legível
salario_mensal = 3500.50            # Correto: indica o que representa
print(f"Email: {email_principal}, Salário: R$ {salario_mensal}")

# Exemplo 3: Reatribuição de valores (variáveis podem mudar)
pontuacao = 0      # Valor inicial
pontuacao = pontuacao + 10  # Adiciona 10 ao valor existente
print(f"Pontuação atual: {pontuacao}")  # Mostra o novo valor

# Exemplo 4: Tipos dinâmicos em Python (não precisa declarar tipo)
dado = 42          # Começa como inteiro
print(f"Tipo inicial: {type(dado).__name__}")
dado = "Agora sou texto"  # Muda para string
print(f"Tipo após mudança: {type(dado).__name__}")

# Exercício: Crie variáveis para seu nome, cidade e hobby, e imprima uma frase completa
meu_nome = "Seu Nome"
minha_cidade = "Sua Cidade"
meu_hobby = "Seu Hobby"
print(f"Olá, sou {meu_nome} de {minha_cidade} e gosto de {meu_hobby}.")
