# -*- coding: utf-8 -*-

"""
Este módulo demonstra a declaração e utilização de variáveis e tipos de dados em Python.
"""

# Variáveis Numéricas
idade = 30  # Inteiro (int)
altura = 1.75  # Ponto flutuante (float)
numero_complexo = 1 + 2j  # Complexo (complex)

print("--- Tipos Numéricos ---")
print(f"Idade: {idade} (Tipo: {type(idade).__name__})")
print(f"Altura: {altura} (Tipo: {type(altura).__name__})")
print(f"Número Complexo: {numero_complexo} (Tipo: {type(numero_complexo).__name__})")
print("-" * 20)

# Variável de Texto (String)
nome = "Ada Lovelace"  # String (str)
primeira_letra = 'A'

print("--- Tipo de Texto (String) ---")
print(f"Nome: {nome} (Tipo: {type(nome).__name__})")
print(f"A primeira letra do nome é: {primeira_letra}")
print("-" * 20)

# Variável Booleana
eh_programador = True  # Booleano (bool)
tem_experiencia = False

print("--- Tipo Booleano ---")
print(f"É programador? {eh_programador} (Tipo: {type(eh_programador).__name__})")
print(f"Tem experiência? {tem_experiencia}")
print("-" * 20)

# Tipos de Sequência
# Lista (list) - mutável
frutas = ["maçã", "banana", "cereja"]
print("--- Tipo Lista (mutável) ---")
print(f"Lista de frutas: {frutas}")
frutas.append("laranja")
print(f"Lista após adicionar 'laranja': {frutas}")
print(f"Tipo: {type(frutas).__name__}")
print("-" * 20)

# Tupla (tuple) - imutável
coordenadas = (10.0, 20.0)
print("--- Tipo Tupla (imutável) ---")
print(f"Coordenadas: {coordenadas}")
# coordenadas[0] = 15.0  # Isto geraria um erro (TypeError)
print(f"Tipo: {type(coordenadas).__name__}")
print("-" * 20)

# Tipo de Mapeamento
# Dicionário (dict)
pessoa = {
    "nome": "Alan Turing",
    "idade": 41,
    "profissao": "Cientista da Computação"
}
print("--- Tipo Dicionário ---")
print(f"Informações da pessoa: {pessoa}")
print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']}")
print(f"Tipo: {type(pessoa).__name__}")
print("-" * 20)

# Tipo Set (conjunto)
numeros_unicos = {1, 2, 3, 2, 1, 4}
print("--- Tipo Set (Conjunto) ---")
print(f"Conjunto de números únicos: {numeros_unicos}")
print(f"Tipo: {type(numeros_unicos).__name__}")
print("-" * 20)

# Tipo None
valor_nulo = None
print("--- Tipo None ---")
print(f"Valor nulo: {valor_nulo} (Tipo: {type(valor_nulo).__name__})")
print("-" * 20)
