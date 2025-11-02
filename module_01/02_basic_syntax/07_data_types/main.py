"""
Aula 07: Tipos de Dados Primitivos em Python

Explora tipos primitivos (int, float, str, bool) e estruturas de dados básicas.
Seguimos 'The Zen of Python': simples é melhor que complexo.
"""

# Variáveis Numéricas
idade = 30  # Inteiro (int): armazena números inteiros, sem casas decimais
altura = 1.75  # Ponto flutuante (float): armazena números decimais
numero_complexo = 1 + 2j  # Complexo (complex): armazena números com parte real e imaginária

print("--- Tipos Numéricos ---")
print(f"Idade: {idade} (Tipo: {type(idade).__name__})")
print(f"Altura: {altura} (Tipo: {type(altura).__name__})")
print(f"Número Complexo: {numero_complexo} (Tipo: {type(numero_complexo).__name__})")
print("-" * 20)

#Variável de Texto (String)
nome = "Ada Lovelace"  # String (str): armazena sequências de caracteres (texto)
primeira_letra = 'A'  # Exemplo de string com um único caractere

print("--- Tipo de Texto (String) ---")
print(f"Nome: {nome} (Tipo: {type(nome).__name__})")
print(f"A primeira letra do nome é: {primeira_letra}")
print("-" * 20)

# Variável Booleana
eh_programador = True  # Booleano (bool): armazena valores verdadeiro (True) ou falso (False)
tem_experiencia = False  # Útil para condições e decisões no código

print("--- Tipo Booleano ---")
print(f"É programador? {eh_programador} (Tipo: {type(eh_programador).__name__})")
print(f"Tem experiência? {tem_experiencia}")
print("-" * 20)

# Tipos de Sequência
# Lista (list) - mutável: pode ser alterada após criação
frutas = ["maçã", "banana", "cereja"]  # Lista: coleção ordenada e mutável de itens
print("--- Tipo Lista (mutável) ---")
print(f"Lista de frutas: {frutas}")
frutas.append("laranja")  # Adiciona um item à lista
print(f"Lista após adicionar 'laranja': {frutas}")
print(f"Tipo: {type(frutas).__name__}")
print("-" * 20)

# Tupla (tuple) - imutável: não pode ser alterada após criação
coordenadas = (10.0, 20.0)  # Tupla: coleção ordenada e imutável
print("--- Tipo Tupla (imutável) ---")
print(f"Coordenadas: {coordenadas}")
# coordenadas[0] = 15.0  # Isto geraria um erro (TypeError) - tuplas são imutáveis
print(f"Tipo: {type(coordenadas).__name__}")
print("-" * 20)

# Tipo de Mapeamento
# Dicionário (dict): armazena pares chave-valor para acesso rápido
pessoa = {
    "nome": "Alan Turing",
    "idade": 41,
    "profissao": "Cientista da Computação"
}
print("--- Tipo Dicionário ---")
print(f"Informações da pessoa: {pessoa}")
print(f"Nome: {pessoa['nome']}")  # Acessa valor pela chave
print(f"Idade: {pessoa['idade']}")
print(f"Tipo: {type(pessoa).__name__}")
print("-" * 20)

# Tipo Set (conjunto): coleção não ordenada de itens únicos
numeros_unicos = {1, 2, 3, 2, 1, 4}  # Set: remove duplicatas automaticamente
print("--- Tipo Set (Conjunto) ---")
print(f"Conjunto de números únicos: {numeros_unicos}")
print(f"Tipo: {type(numeros_unicos).__name__}")
print("-" * 20)

# Tipo None: representa ausência de valor
valor_nulo = None  # None: usado para indicar "nada" ou valor indefinido
print("--- Tipo None ---")
print(f"Valor nulo: {valor_nulo} (Tipo: {type(valor_nulo).__name__})")
print("-" * 20)

# Exercício: Crie um dicionário com suas informações pessoais e imprima uma delas
# Exemplo: meu_perfil = {"nome": "Seu Nome", "idade": 25}
# print(f"Meu nome é {meu_perfil['nome']}")