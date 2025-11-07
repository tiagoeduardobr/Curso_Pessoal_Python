# Projeto: Curso Pessoal de Python

## Visão Geral

Este projeto tem como objetivo criar um curso de Python completo e prático, seguindo uma estrutura modular incremental, com todas as aulas, exemplos de código e explicações documentadas e versionadas em um repositório Git. A progressão vai do básico ao avançado, incluindo especializações em web, dados e automação.

---

## Objetivos Principais do Curso

1. **Fundamentos Sólidos:** Ensinar os conceitos fundamentais da linguagem Python, garantindo que o aluno tenha uma base sólida para construir conhecimentos mais avançados.
2. **Aprendizagem Prática:** Focar em exemplos de código práticos e exercícios que demonstrem o uso real dos conceitos ensinados em cada aula.
3. **Estrutura Modular:** Organizar o curso em módulos e aulas sequenciais, facilitando o acompanhamento e a revisão do conteúdo. A estrutura de diretórios reflete essa modularidade (ex: `module_01/01_introduction/05_hello_world/`, `module_01/03_basic_syntax/10_variables/`, etc.).
4. **Versionamento com Git:** Utilizar o Git e o GitHub para documentar todo o progresso, permitindo que o aluno (e a IA) possa revisitar o histórico de aprendizado e gerenciar o código de forma eficiente.
5. **Automação da Tutoria:** Capacitar a IA a assistir na criação das aulas, na escrita dos códigos, na documentação e na gestão do repositório, seguindo as diretrizes estabelecidas.
6. **Integração de Tecnologias Avançadas:** Introduzir conceitos de backend (FastAPI, SQLAlchemy), frontend básico e IA generativa, simulando projetos do mundo real para construir um portfólio competitivo.

---

## Estrutura Geral do Curso

O curso é dividido em 13 módulos, do básico ao avançado, incluindo especializações em web, dados, automação e tópicos avançados. Cada aula prática tem um `main.py` com docstring, comentários, exemplos e exercício. Aulas teóricas usam `.md` bem formatados. Diretórios seguem `module_XX/XX_submodule/XX_topic/`.

---

## Estrutura Padrão de Aulas

Para manter consistência e qualidade em todas as aulas, siga este formato em cada `main.py`:

1. **Docstring no Topo:** Inclua uma docstring com título da aula, descrição breve e referência ao 'The Zen of Python'.
2. **Comentários Inline:** Explique cada conceito, variável ou operação com comentários claros e didáticos.
3. **Exemplos Práticos:** Use prints formatados para demonstrar resultados, com variáveis descritivas.
4. **Exercício Final:** Adicione um pequeno exercício para prática, incentivando o aluno a modificar e testar.
5. **PEP 8 e Simplicidade:** Mantenha o código limpo, legível e "pitônico".

Exemplo de Estrutura:
```python
"""
Aula XX: Título da Aula

Descrição breve do tópico.
Seguimos 'The Zen of Python': princípio relevante.
"""

# Exemplo 1: Conceito básico
variavel = valor  # Comentário explicativo
print(f"Resultado: {variavel}")

# Exemplo de Exercício: Calcule a área de um retângulo e o perímetro
largura = 7
altura = 3
area = largura * altura
perimetro = 2 * (largura + altura)
print(f"Área do retângulo: {area}")
print(f"Perímetro do retângulo: {perimetro}")
```

---

## Próximos Passos

Para dar continuidade ao curso de onde paramos, a IA deve seguir o seguinte fluxo para cada nova aula:

1. **Aguardar o Tópico:** Esperar que o aluno/usuário defina o tema da próxima aula (ex: "Operadores Aritméticos").
2. **Criar a Estrutura:**
    * Criar um novo diretório para a aula, seguindo o padrão de numeração sequencial (ex: `module_01/03_basic_syntax/12_arithmetic_operators/`).
    * Dentro do novo diretório, criar um arquivo `main.py`.
3. **Desenvolver o Conteúdo:**
    * No arquivo `main.py`, escrever o código Python que exemplifica o tópico da aula.
    * Utilizar comentários no código para explicar cada conceito de forma clara e didática, como se fosse o professor.
4. **Documentar e Versionar:**
    * Adicionar os novos arquivos no diretório criado (ex.: `module_01/03_basic_syntax/12_arithmetic_operators/main.py`) ao controle de versão (`git add .`).
    * Gerar uma mensagem de commit clara e descritiva, seguindo o padrão "feat: Create lesson on <TÓPICO DA AULA>" (ex: "feat: Create lesson on arithmetic operators").
    * Realizar o commit das mudanças.
5. **Confirmar e Avançar:** Informar ao usuário que a aula foi criada e comitada, e aguardar a instrução para a próxima aula ou qualquer outra solicitação.
6. **Refinar e Conectar ao Mercado:** Após o commit, sugerir atualizações no [README.md](http://_vscodecontentref_/3) principal com um resumo da aula. Explicar como essa habilidade agrega valor ao portfólio (ex: "Essa aula demonstra fundamentos essenciais para entrevistas em Python"). Aguarde feedback do usuário para ajustes ou a próxima aula.

---

## Estado Atual

O projeto já foi iniciado com algumas aulas básicas, que serão reposicionadas para a nova estrutura modular (ex: `00-import-this` vai para `module_01/01_introduction/01_import_this/`). As aulas existentes incluem introdução ao Python e conceitos iniciais. A nova estrutura TODO lista todas as lições a serem desenvolvidas ou movidas, priorizando Módulos 1 e 2 para respeitar a ordem sequencial.

---

TODO: Estrutura Completa do Curso

Esta lista TODO descreve todas as aulas a serem criadas ou reposicionadas, seguindo a estrutura modular. Aulas existentes serão movidas para novos diretórios. Use [x] para concluídas, [ ] para pendentes. Diretórios: `module_XX/XX_submodule/XX_topic/`. Aulas práticas: `main.py`; Teóricas: `topic.md`.

### Módulo 1: Fundamentos e Configuração do Ambiente

#### 1.1. Introdução e Configuração

* [x] O que é Python? (Filosofia, usos) - `module_01/01_introduction/01_import_this/main.py`
* [ ] Instalar Python (e a diferença entre Python 2 vs 3) - `module_01/01_introduction/02_python_installation/python_installation.md`
* [ ] Configurando o Ambiente de Desenvolvimento (IDEs como VS Code, PyCharm) - `module_01/01_introduction/03_development_environment/development_environment.md`
* [ ] Usando o Interpretador (REPL) - `module_01/01_introduction/04_interpreter_repl/interpreter_repl.md` e `main.py`
* [x] Seu primeiro programa: `print("Olá, Mundo!")` - `module_01/01_introduction/05_hello_world/main.py`

#### 1.2. Ferramentas Essenciais do Desenvolvedor

* [ ] O que é Controle de Versão? (Git) - `module_01/02_essential_tools/06_git_concepts/git_concepts.md`
* [ ] Ambientes Virtuais (`venv`) - Um conceito crucial para projetos - `module_01/02_essential_tools/07_virtual_environments/virtual_environments.md` (reposicionar de 31)
* [ ] Introdução ao Pip (instalando pacotes externos) - `module_01/02_essential_tools/08_pip_introduction/pip_introduction.md` (reposicionar de 29)
* [ ] O arquivo `requirements.txt` - `module_01/02_essential_tools/09_requirements_txt/requirements_txt.md` (reposicionar de 30)

#### 1.3. Sintaxe Básica

* [x] Variáveis (Nomenclatura e atribuição) - `module_01/03_basic_syntax/10_variables/main.py` (reposicionar de 06)
* [x] Tipos de Dados Primitivos: (`int`, `float`, `str`, f-strings, `bool`) - `module_01/03_basic_syntax/11_data_types/main.py` (reposicionar de 07)
* [x] Operadores (Aritméticos, de Comparação, Lógicos) - `module_01/03_basic_syntax/12_arithmetic_operators/main.py` (reposicionar de 08)
* [ ] Entrada e Saída (`input()` e `print()`) - `module_01/03_basic_syntax/13_input_output/main.py` (reposicionar de 09)
* [ ] Comentários e Indentação (a regra mais importante do Python) - `module_01/03_basic_syntax/14_comments_indentation/comments_indentation.md` e `main.py` (reposicionar de 10)

### Módulo 2: Estruturas de Controle e Lógica

#### 2.1. Lógica Condicional

* [ ] `if`, `elif`, `else` - `module_02/01_conditional_logic/15_if_elif_else/main.py` (reposicionar de 11)

#### 2.2. Estruturas de Repetição (Loops)

* [ ] `for` (iterando sobre sequências) - `module_02/02_loops/16_for_loops/main.py` (reposicionar de 12)
* [ ] `while` (loops baseados em condição) - `module_02/02_loops/17_while_loops/main.py` (reposicionar de 13)
* [ ] Controle de loops: `break` e `continue` - `module_02/02_loops/18_loop_control/main.py` (reposicionar de 14)
* [ ] A função `range()` - `module_02/02_loops/19_range_function/main.py` (reposicionar de 15)

### Módulo 3: Estruturas de Dados

#### 3.1. Sequências e Coleções

* [ ] Listas (Lists): Mutáveis, ordenadas (criação, indexação, fatiamento, métodos) - `module_03/01_sequences_collections/20_lists/main.py` (reposicionar de 16)
* [ ] Tuplas (Tuples): Imutáveis, ordenadas - `module_03/01_sequences_collections/21_tuples/main.py` (reposicionar de 17)
* [ ] Dicionários (Dictionaries): Pares chave-valor, métodos `.keys()`, `.values()`, `.items()` - `module_03/01_sequences_collections/22_dictionaries/main.py` (reposicionar de 18)
* [ ] Conjuntos (Sets): Itens únicos, operações de conjunto (união, interseção) - `module_03/01_sequences_collections/23_sets/main.py` (reposicionar de 19)

#### 3.2. Iteração

* [ ] Métodos de iteração (loops em Dicionários, etc) - `module_03/02_iteration/24_iteration_methods/main.py` (reposicionar de 20)
* [ ] Iteração Avançada (`enumerate` e `zip`) - `module_03/02_iteration/25_enumerate_zip/main.py`

### Módulo 4: Funções e Modularidade

#### 4.1. Funções

* [ ] Definindo funções (`def`) - `module_04/01_functions/26_defining_functions/main.py` (reposicionar de 21)
* [ ] Argumentos e Parâmetros (posicionais, nomeados, padrão, `*args`, `**kwargs`) - `module_04/01_functions/27_arguments_parameters/main.py` (reposicionar de 22)
* [ ] Retornando valores (`return`) - `module_04/01_functions/28_return_values/main.py` (reposicionar de 23)

#### 4.2. Tópicos Funcionais

* [ ] Escopo de Variáveis (Local vs. Global, `global`) - `module_04/02_functional_topics/29_variable_scope/main.py` (reposicionar de 24)
* [ ] Funções Anônimas (`lambda`) - `module_04/02_functional_topics/30_lambda_functions/main.py` (reposicionar de 25)
* [ ] Funções de Ordem Superior (`map`, `filter`) - `module_04/02_functional_topics/31_map_filter/main.py`

#### 4.3. Modularidade

* [ ] Importando módulos (`import`, `from ... import`) - `module_04/03_modularity/32_importing_modules/main.py` (reposicionar de 26)
* [ ] Módulos da Biblioteca Padrão (ex: `math`, `random`, `datetime`) - `module_04/03_modularity/33_standard_library/main.py` (reposicionar de 27)
* [ ] Criando seus próprios módulos (arquivos `.py`) - `module_04/03_modularity/34_custom_modules/main.py` (reposicionar de 28)

### Módulo 5: Programação Orientada a Objetos (POO)

#### 5.1. Conceitos de POO

* [ ] Classes e Objetos (Instâncias) - `module_05/01_oop_concepts/35_classes_objects/main.py` (reposicionar de 32)
* [ ] Atributos (dados da classe/objeto) - `module_05/01_oop_concepts/36_attributes/main.py` (reposicionar de 33)
* [ ] Métodos (funções da classe) - `module_05/01_oop_concepts/37_methods/main.py` (reposicionar de 34)
* [ ] Construtores (`__init__`) e o parâmetro `self` - `module_05/01_oop_concepts/38_constructors_self/main.py` (reposicionar de 35)

#### 5.2. Pilares da POO

* [ ] Herança: Criando subclasses - `module_05/02_oop_pillars/39_inheritance/main.py` (reposicionar de 36)
* [ ] Encapsulamento: Atributos públicos e privados - `module_05/02_oop_pillars/40_encapsulation/main.py` (reposicionar de 37)
* [ ] Polimorfismo: Sobrescrita de métodos - `module_05/02_oop_pillars/41_polymorphism/main.py` (reposicionar de 38)
* [ ] Métodos Mágicos (Métodos Dunder), como `__str__` e `__repr__` - `module_05/02_oop_pillars/42_magic_methods/main.py` (reposicionar de 39)

#### 5.3. Tópicos Avançados de POO

* [ ] `@staticmethod` e `@classmethod` - `module_05/03_advanced_oop/43_static_class_methods/main.py`

### Módulo 6: Python Moderno - Type Hints

#### 6.1. Anotações de Tipo

* [ ] Sintaxe básica de anotação (`var: str`, `-> bool`) - `module_06/01_type_hints/44_basic_syntax/main.py`
* [ ] O Módulo `typing` (`List`, `Dict`, `Optional`, `Union`) - `module_06/01_type_hints/45_typing_module/main.py`
* [ ] Ferramentas de Verificação (Introdução ao `Mypy`) - `module_06/01_type_hints/46_mypy/mypy.md`

### Módulo 7: Fundamentos de Banco de Dados (SQL)

#### 7.1. Conceitos e SQL Básico

* [ ] Conceitos de Bancos Relacionais (Tabelas, Chaves) - `module_07/01_sql_basics/47_db_concepts/db_concepts.md`
* [ ] Comandos SQL (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) - `module_07/01_sql_basics/48_sql_crud/sql_crud.md`
* [ ] Junções (`JOINs`) - `module_07/01_sql_basics/49_sql_joins/sql_joins.md`

#### 7.2. Python e SQL

* [ ] Usando a biblioteca `sqlite3` - `module_07/02_python_sql/50_sqlite3/main.py`

### Módulo 8: Tópicos Intermediários

#### 8.1. Manipulação de Erros

* [ ] Tratamento de Exceções: `try`, `except`, `else`, `finally` - `module_08/01_error_handling/51_exception_handling/main.py` (reposicionar de 40)
* [ ] Lançando exceções (`raise`) - `module_08/01_error_handling/52_raising_exceptions/main.py` (reposicionar de 41)

#### 8.2. Manipulação de Arquivos

* [ ] Lendo e escrevendo arquivos (`open()`, `with open(...)`) - `module_08/02_file_handling/53_file_handling/main.py` (reposicionar de 42)
* [ ] Trabalhando com formatos comuns (CSV, JSON) - `module_08/02_file_handling/54_csv_json/main.py` (reposicionar de 43)

#### 8.3. Processamento de Texto (Regex)

* [ ] Expressões Regulares (Módulo `re`) - `module_08/03_regex/55_regex/main.py`

#### 8.4. Tópicos "Pythônicos"

* [ ] Compreensões de Lista (List Comprehensions) - `module_08/04_pythonic_topics/56_list_comprehensions/main.py` (reposicionar de 44)
* [ ] Geradores (`yield`) e Expressões Geradoras - `module_08/04_pythonic_topics/57_generators/main.py` (reposicionar de 45)
* [ ] Decoradores (`@decorator`) - `module_08/04_pythonic_topics/58_decorators/main.py` (reposicionar de 46)

### Módulo 9: Especialização - Desenvolvimento Web (Backend)

#### 9.1. Conceitos Web Fundamentais

* [ ] Conceitos: HTTP, APIs REST, WSGI vs ASGI - `module_09/01_web_concepts/59_web_concepts/web_concepts.md` (reposicionar de 47)

#### 9.2. Frameworks Principais

* [ ] Framework: Flask - `module_09/02_frameworks/60_flask/main.py` (reposicionar de 48)
* [ ] Framework: Django - `module_09/02_frameworks/61_django/main.py` (reposicionar de 49)
* [ ] Framework: FastAPI - `module_09/02_frameworks/62_fastapi/main.py` (reposicionar de 50)

#### 9.3. Banco de Dados e ORMs

* [ ] ORM: SQLAlchemy (para Flask/FastAPI) - `module_09/03_orms/63_sqlalchemy/main.py` (reposicionar de 51)
* [ ] Django ORM (integrado) - `module_09/03_orms/64_django_orm/main.py`

#### 9.4. Validação e Serialização

* [ ] Pydantic (Validação com Type Hints) - `module_09/04_serialization/65_pydantic/main.py`
* [ ] Django REST Framework (DRF) - `module_09/04_serialization/66_drf/main.py`

#### 9.5. Ferramentas de Ecossistema

* [ ] Biblioteca: Requests (Consumindo APIs) - `module_09/05_ecosystem/67_requests/main.py` (reposicionar de 52)
* [ ] Autenticação (JWT, Sessões) - `module_09/05_ecosystem/68_authentication/authentication.md`
* [ ] Servidores (Gunicorn, Uvicorn) - `module_09/05_ecosystem/69_servers/servers.md`

### Módulo 10: Especialização - Ciência de Dados e Machine Learning

#### 10.1. Análise e Manipulação de Dados

* [ ] NumPy (computação numérica, arrays) - `module_10/01_data_analysis/70_numpy/main.py` (reposicionar de 53)
* [ ] Pandas (manipulação e análise de dados, DataFrames) - `module_10/01_data_analysis/71_pandas/main.py` (reposicionar de 54)

#### 10.2. Visualização de Dados

* [ ] Matplotlib (biblioteca-base para gráficos) - `module_10/02_visualization/72_matplotlib/main.py` (reposicionar de 55)
* [ ] Seaborn (visualizações estatísticas) - `module_10/02_visualization/73_seaborn/main.py` (reposicionar de 56)

#### 10.3. Machine Learning (ML)

* [ ] Scikit-learn (sklearn) (algoritmos clássicos de ML) - `module_10/03_machine_learning/74_scikit_learn/main.py` (reposicionar de 57)

#### 10.4. Deep Learning (DL)

* [ ] TensorFlow - `module_10/04_deep_learning/75_tensorflow/main.py` (reposicionar de 58)
* [ ] Keras - `module_10/04_deep_learning/76_keras/main.py` (reposicionar de 59)
* [ ] PyTorch - `module_10/04_deep_learning/77_pytorch/main.py` (reposicionar de 60)

### Módulo 11: Especialização - Automação e Scripting

#### 11.1. Automação Web (Scraping/Testing)

* [ ] Selenium (controla um navegador web) - `module_11/01_web_automation/78_selenium/main.py` (reposicionar de 61)
* [ ] Beautiful Soup 4 (BS4) (extrair dados de HTML/XML) - `module_11/01_web_automation/79_beautiful_soup/main.py` (reposicionar de 62)
* [ ] Scrapy (framework completo de web scraping) - `module_11/01_web_automation/80_scrapy/main.py` (reposicionar de 63)

#### 11.2. Automação de Tarefas

* [ ] Bibliotecas Padrão (`os`, `shutil`, `subprocess`) - `module_11/02_task_automation/81_task_automation/main.py` (reposicionar de 64)
* [ ] PyAutoGUI (controlar mouse e teclado) - `module_11/02_task_automation/82_pyautogui/main.py` (reposicionar de 65)

### Módulo 12: Especialização - Interfaces Gráficas (Desktop)

#### 12.1. Bibliotecas de GUI

* [ ] Tkinter (biblioteca padrão de GUI) - `module_12/01_gui_libraries/83_tkinter/main.py` (reposicionar de 66)
* [ ] PyQt ou PySide (framework Qt) - `module_12/01_gui_libraries/84_pyqt_pyside/main.py` (reposicionar de 67)
* [ ] Kivy (framework multiplataforma) - `module_12/01_gui_libraries/85_kivy/main.py` (reposicionar de 68)

### Módulo 13: Tópicos Avançados e Boas Práticas

#### 13.1. Testes Automatizados

* [ ] Conceitos de Teste (Unitário, Integração) - `module_13/01_automated_testing/86_testing_concepts/testing_concepts.md` (reposicionar de 69)
* [ ] Bibliotecas: `unittest` e `pytest` - `module_13/01_automated_testing/87_unittest_pytest/main.py` (reposicionar de 70)

#### 13.2. Código Limpo e Padrões

* [ ] PEP 8 (guia oficial de estilo) - `module_13/02_clean_code/88_pep8/pep8.md` (reposicionar de 71)
* [ ] Linters e Formatadores (Flake8, Black) - `module_13/02_clean_code/89_linters_formatters/linters_formatters.md` (reposicionar de 72)

#### 13.3. Tópicos Avançados da Linguagem

* [ ] Programação Assíncrona (`asyncio`, `async`/`await`) - `module_13/03_advanced_topics/90_asyncio/main.py` (reposicionar de 73)
* [ ] Concorrência (Threads vs. Processos) - `module_13/03_advanced_topics/91_concurrency/main.py` (reposicionar de 74)

#### 13.4. Produção e Deploy

* [ ] Docker (empacotando aplicações em contêineres) - `module_13/04_production_deploy/92_docker/docker.md` (reposicionar de 75)
* [ ] Conceitos de CI/CD (Integração Contínua / Entrega Contínua) - `module_13/04_production_deploy/93_ci_cd/ci_cd.md` (reposicionar de 76)
