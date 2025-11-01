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

# Exemplo 5: Precedência de Operadores
# Ordem: **, *, /, //, %, +, - (use parênteses para clareza)
expressao = 2 + 3 * 4  # Multiplicação antes da adição
expressao_com_parenteses = (2 + 3) * 4  # Parênteses alteram a ordem
print(f"2 + 3 * 4 = {expressao} (multiplicação primeiro)")
print(f"(2 + 3) * 4 = {expressao_com_parenteses} (adição primeiro)")

# Exemplo 6: Caso Edge - Números Negativos
negativo = -10
modulo_negativo = negativo % 3  # Módulo com negativo
print(f"Módulo com negativo: {-10} % 3 = {modulo_negativo}")

# Exercício: Calcule a área de um retângulo e o perímetro
largura = 7
altura = 3
area = largura * altura
perimetro = 2 * (largura + altura)
print(f"Área do retângulo: {area}")
print(f"Perímetro do retângulo: {perimetro}")