"""
Aula 03: Operadores Aritméticos em Python

Esta aula explora os operadores aritméticos básicos, essenciais para manipular números.
Seguimos 'The Zen of Python': simples é melhor que complexo.
"""

# Exemplo 1: Adição e Subtração
a = 10
b = 5
soma = a + b  # Adição: combina valores
subtracao = a - b  # Subtração: remove valores
print(f"Adição: {a} + {b} = {soma}")
print(f"Subtração: {a} - {b} = {subtracao}")

# Exemplo 2: Multiplicação e Divisão
multiplicacao = a * b  # Multiplicação: repete adição
divisao = a / b  # Divisão: reparte valores (sempre float)
print(f"Multiplicação: {a} * {b} = {multiplicacao}")
print(f"Divisão: {a} / {b} = {divisao}")

# Exemplo 3: Divisão Inteira e Módulo
divisao_inteira = a // b  # Parte inteira da divisão
modulo = a % b  # Resto da divisão
print(f"Divisão Inteira: {a} // {b} = {divisao_inteira}")
print(f"Módulo: {a} % {b} = {modulo}")

# Exemplo 4: Exponenciação
exponenciacao = a ** b  # Eleva a à potência b
print(f"Exponenciação: {a} ** {b} = {exponenciacao}")

# Exercício: Calcule a área de um retângulo
largura = 7
altura = 3
area = largura * altura
print(f"Área do retângulo: {area}")