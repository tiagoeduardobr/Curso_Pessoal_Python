# Projeto: Curso Pessoal de Python

## Visão Geral

Este projeto tem como objetivo criar um curso de Python completo e prático, seguindo uma estrutura modular incremental, com todas as aulas, exemplos de código e explicações documentadas e versionadas em um repositório Git. A progressão vai do básico ao avançado, incluindo especializações em web, dados e automação.

---

## Objetivos Principais do Curso

1. **Fundamentos Sólidos:** Ensinar os conceitos fundamentais da linguagem Python, garantindo que o aluno tenha uma base sólida para construir conhecimentos mais avançados.
2. **Aprendizagem Prática:** Focar em exemplos de código práticos e exercícios que demonstrem o uso real dos conceitos ensinados em cada aula.
3. **Estrutura Modular:** Organizar o curso em módulos e aulas sequenciais, facilitando o acompanhamento e a revisão do conteúdo. A estrutura de diretórios reflete essa modularidade (ex: `module_01/01_introduction/05_hello_world/`, `module_01/02_basic_syntax/06_variables/`, etc.).
4. **Versionamento com Git:** Utilizar o Git e o GitHub para documentar todo o progresso, permitindo que o aluno (e a IA) possa revisitar o histórico de aprendizado e gerenciar o código de forma eficiente.
5. **Automação da Tutoria:** Capacitar a IA a assistir na criação das aulas, na escrita dos códigos, na documentação e na gestão do repositório, seguindo as diretrizes estabelecidas.
6. **Integração de Tecnologias Avançadas:** Introduzir conceitos de backend (FastAPI, SQLAlchemy), frontend básico e IA generativa, simulando projetos do mundo real para construir um portfólio competitivo.

---

## Estrutura Geral do Curso

O curso é dividido em 8 módulos, do básico ao avançado. Cada aula prática tem um `main.py` com docstring, comentários, exemplos e exercício. Aulas teóricas usam `.md` bem formatados. Diretórios seguem `module_XX/XX_submodule/XX_topic/`.

---

## Estado Atual

O projeto já foi iniciado com algumas aulas básicas, que serão reposicionadas para a nova estrutura modular (ex: `00-import-this` vai para `module_01/01_introduction/01_import_this/`). As aulas existentes incluem introdução ao Python e conceitos iniciais. A nova estrutura TODO lista todas as lições a serem desenvolvidas ou movidas, priorizando Módulos 1 e 2 para respeitar a ordem sequencial.

---

## Próximos Passos para a IA

Para dar continuidade ao curso de onde paramos, a IA deve seguir o seguinte fluxo para cada nova aula:

1. **Aguardar o Tópico:** Esperar que o aluno/usuário defina o tema da próxima aula (ex: "Operadores Aritméticos").
2. **Criar a Estrutura:**
    * Criar um novo diretório para a aula, seguindo o padrão de numeração sequencial (ex: `module_01/02_basic_syntax/08_arithmetic_operators/`).
    * Dentro do novo diretório, criar um arquivo `main.py`.
3. **Desenvolver o Conteúdo:**
    * No arquivo `main.py`, escrever o código Python que exemplifica o tópico da aula.
    * Utilizar comentários no código para explicar cada conceito de forma clara e didática, como se fosse o professor.
4. **Documentar e Versionar:**
    * Adicionar os novos arquivos no diretório criado (ex.: `module_01/02_basic_syntax/08_arithmetic_operators/main.py`) ao controle de versão (`git add .`).
    * Gerar uma mensagem de commit clara e descritiva, seguindo o padrão "feat: Create lesson on <TÓPICO DA AULA>" (ex: "feat: Create lesson on arithmetic operators").
    * Realizar o commit das mudanças.
5. **Confirmar e Avançar:** Informar ao usuário que a aula foi criada e comitada, e aguardar a instrução para a próxima aula ou qualquer outra solicitação.
6. **Refinar e Conectar ao Mercado:** Após o commit, sugerir atualizações no [README.md](README.md) principal com um resumo da aula. Explicar como essa habilidade agrega valor ao portfólio (ex: "Essa aula demonstra fundamentos essenciais para entrevistas em Python"). Aguarde feedback do usuário para ajustes ou a próxima aula.

---

## Diretrizes de Estilo e Linguagem

Para garantir a clareza e a eficácia do aprendizado, seguir as seguintes diretrizes:

* Conteúdo das aulas (docstrings, comentários, explicações em .md) em português para facilitar o aprendizado. Nomes de variáveis, diretórios, arquivos e termos Python (ex: `if`, `for`, nomes de funções) em inglês, seguindo PEP 8 e boas práticas de programação.

## TODO: Estrutura Completa do Curso

Esta lista TODO descreve todas as aulas a serem criadas ou reposicionadas, seguindo a estrutura modular. Aulas existentes serão movidas para novos diretórios. Use [x] para concluídas, [ ] para pendentes. Diretórios: `module_XX/XX_submodule/XX_topic/`. Aulas práticas: `main.py`; Teóricas: `topic.md`.

### Módulo 1: Fundamentos (O Básico)

#### 1.1. Introdução e Configuração

* [x] O que é Python? (Filosofia, usos) - `module_01/01_introduction/01_import_this/main.py`
* [ ] Instalar Python (e a diferença entre Python 2 vs 3) - `module_01/01_introduction/02_python_installation/python_installation.md`
* [ ] Configurando o Ambiente de Desenvolvimento (IDEs como VS Code, PyCharm) - `module_01/01_introduction/03_development_environment/development_environment.md`
* [ ] Usando o Interpretador (REPL) - `module_01/01_introduction/04_interpreter_repl/interpreter_repl.md` e `main.py`
* [x] Seu primeiro programa: `print("Olá, Mundo!")` - `module_01/01_introduction/05_hello_world/main.py`

#### 1.2. Sintaxe Básica

* [x] Variáveis (Nomenclatura e atribuição) - `module_01/02_basic_syntax/06_variables/main.py` (reposicionar de 02-variables-and-types)
* [x] Tipos de Dados Primitivos: Inteiros (`int`), Ponto flutuante (`float`), Strings (`str`) e formatação (f-strings), Booleanos (`bool`) - `module_01/02_basic_syntax/07_data_types/main.py` (reposicionar de 02-variables-and-types)
* [x] Operadores (Aritméticos, de Comparação, Lógicos) - `module_01/02_basic_syntax/08_arithmetic_operators/main.py` (reposicionar de 03-arithmetic-operators)
* [ ] Entrada e Saída (`input()` e `print()`) - `module_01/02_basic_syntax/09_input_output/main.py`
* [ ] Comentários e Indentação (a regra mais importante do Python) - `module_01/02_basic_syntax/10_comments_indentation/comments_indentation.md` e `main.py`

### Módulo 2: Estruturas de Controle e Lógica

#### 2.1. Lógica Condicional

* [ ] `if`, `elif`, `else` - `module_02/01_conditional_logic/11_if_elif_else/main.py`

#### 2.2. Estruturas de Repetição (Loops)

* [ ] `for` (iterando sobre sequências) - `module_02/02_loops/12_for_loops/main.py`
* [ ] `while` (loops baseados em condição) - `module_02/02_loops/13_while_loops/main.py`
* [ ] Controle de loops: `break` e `continue` - `module_02/02_loops/14_loop_control/main.py`
* [ ] A função `range()` - `module_02/02_loops/15_range_function/main.py`

### Módulo 3: Estruturas de Dados

#### 3.1. Sequências e Coleções

* [ ] Listas (Lists): Mutáveis, ordenadas (criação, indexação, fatiamento, métodos como `.append()`, `.pop()`) - `module_03/01_sequences_collections/16_lists/main.py`
* [ ] Tuplas (Tuples): Imutáveis, ordenadas - `module_03/01_sequences_collections/17_tuples/main.py`
* [ ] Dicionários (Dictionaries): Pares chave-valor, desordenados (até Python 3.6), mutáveis - `module_03/01_sequences_collections/18_dictionaries/main.py`
* [ ] Conjuntos (Sets): Itens únicos, desordenados, operações de conjunto (união, interseção) - `module_03/01_sequences_collections/19_sets/main.py`
* [ ] Métodos de iteração para cada estrutura - `module_03/01_sequences_collections/20_iteration_methods/main.py`

### Módulo 4: Funções e Modularidade

#### 4.1. Funções

* [ ] Definindo funções (`def`) - `module_04/01_functions/21_defining_functions/main.py`
* [ ] Argumentos e Parâmetros (posicionais, nomeados, padrão) - `module_04/01_functions/22_arguments_parameters/main.py`
* [ ] Retornando valores (`return`) - `module_04/01_functions/23_return_values/main.py`
* [ ] Escopo de Variáveis (Local vs. Global) - `module_04/01_functions/24_variable_scope/main.py`
* [ ] Funções Anônimas (`lambda`) - `module_04/01_functions/25_lambda_functions/main.py`

#### 4.2. Modularidade

* [ ] Importando módulos (`import`, `from ... import`) - `module_04/02_modularity/26_importing_modules/main.py`
* [ ] Módulos da Biblioteca Padrão (ex: `math`, `random`, `datetime`) - `module_04/02_modularity/27_standard_library/main.py`
* [ ] Criando seus próprios módulos (arquivos `.py`) - `module_04/02_modularity/28_custom_modules/main.py`

#### 4.3. Gerenciamento de Pacotes

* [ ] Introdução ao Pip (instalando pacotes externos, ex: `pip install requests`) - `module_04/03_package_management/29_pip_introduction/pip_introduction.md`
* [ ] O arquivo `requirements.txt` - `module_04/03_package_management/30_requirements_txt/requirements_txt.md`
* [ ] Ambientes Virtuais (`venv`) - Um conceito crucial para projetos - `module_04/03_package_management/31_virtual_environments/virtual_environments.md`

### Módulo 5: Programação Orientada a Objetos (POO)

#### 5.1. Conceitos de POO

* [ ] Classes e Objetos (Instâncias) - `module_05/01_oop_concepts/32_classes_objects/main.py`
* [ ] Atributos (dados da classe/objeto) - `module_05/01_oop_concepts/33_attributes/main.py`
* [ ] Métodos (funções da classe) - `module_05/01_oop_concepts/34_methods/main.py`
* [ ] Construtores (`__init__`) e o parâmetro `self` - `module_05/01_oop_concepts/35_constructors_self/main.py`

#### 5.2. Pilares da POO

* [ ] Herança: Criando subclasses que herdam de classes-mãe - `module_05/02_oop_pillars/36_inheritance/main.py`
* [ ] Encapsulamento: Protegendo dados (atributos privados/públicos) - `module_05/02_oop_pillars/37_encapsulation/main.py`
* [ ] Polimorfismo: Objetos de diferentes classes respondendo ao mesmo método - `module_05/02_oop_pillars/38_polymorphism/main.py`
* [ ] Métodos Mágicos (Métodos Dunder), como `__str__` e `__repr__` - `module_05/02_oop_pillars/39_magic_methods/main.py`

### Módulo 6: Tópicos Intermediários

#### 6.1. Manipulação de Erros

* [ ] Tratamento de Exceções: `try`, `except`, `else`, `finally` - `module_06/01_error_handling/40_exception_handling/main.py`
* [ ] Lançando exceções (`raise`) - `module_06/01_error_handling/41_raising_exceptions/main.py`

#### 6.2. Manipulação de Arquivos

* [ ] Lendo e escrevendo arquivos (`open()`, `with open(...)`) - `module_06/02_file_handling/42_file_handling/main.py`
* [ ] Trabalhando com formatos comuns (CSV, JSON) - Bibliotecas: `csv` e `json` (da biblioteca padrão) - `module_06/02_file_handling/43_csv_json/main.py`

#### 6.3. Tópicos "Pythônicos"

* [ ] Compreensões de Lista (Forma concisa de criar listas) - `module_06/03_pythonic_topics/44_list_comprehensions/main.py`
* [ ] Geradores (`yield`) e Expressões Geradoras - `module_06/03_pythonic_topics/45_generators/main.py`
* [ ] Decoradores (`@decorator`) - `module_06/03_pythonic_topics/46_decorators/main.py`

### Módulo 7: Especializações (Bibliotecas e Frameworks)

#### 7.1: Desenvolvimento Web (Backend)

* [ ] Conceitos: HTTP (GET, POST), APIs REST, ORM (Mapeador Objeto-Relacional) - `module_07/01_web_development/47_web_concepts/web_concepts.md`
* [ ] Frameworks: Flask (micro-framework, ótimo para começar e APIs menores) - `module_07/01_web_development/48_flask/flask.md` e `main.py`
* [ ] Frameworks: Django (framework "completo", com bateria incluída, painel de admin, ORM próprio, sistema de autenticação) - `module_07/01_web_development/49_django/django.md` e `main.py`
* [ ] Frameworks: FastAPI (framework moderno de alta performance para criar APIs, com validação de dados e documentação automática) - `module_07/01_web_development/50_fastapi/fastapi.md` e `main.py`
* [ ] Bibliotecas Comuns: SQLAlchemy (ORM principal do Python, usado com Flask/FastAPI) - `module_07/01_web_development/51_sqlalchemy/sqlalchemy.md` e `main.py`
* [ ] Bibliotecas Comuns: Requests (para fazer requisições HTTP, consumindo outras APIs) - `module_07/01_web_development/52_requests/requests.md` e `main.py`

#### 7.2: Ciência de Dados e Machine Learning

* [ ] Análise e Manipulação de Dados: NumPy (biblioteca fundamental para computação numérica, arrays N-dimensionais) - `module_07/02_data_science/53_numpy/numpy.md` e `main.py`
* [ ] Análise e Manipulação de Dados: Pandas (a biblioteca mais importante para manipulação e análise de dados, DataFrames) - `module_07/02_data_science/54_pandas/pandas.md` e `main.py`
* [ ] Visualização de Dados: Matplotlib (biblioteca-base para gráficos e plots) - `module_07/02_data_science/55_matplotlib/matplotlib.md` e `main.py`
* [ ] Visualização de Dados: Seaborn (baseado no Matplotlib, para visualizações estatísticas mais bonitas) - `module_07/02_data_science/56_seaborn/seaborn.md` e `main.py`
* [ ] Machine Learning (ML): Scikit-learn (sklearn) (biblioteca principal para algoritmos clássicos de ML: regressão, classificação, clustering) - `module_07/02_data_science/57_scikit_learn/scikit_learn.md` e `main.py`
* [ ] Deep Learning (Tópico Avançado de ML): TensorFlow (desenvolvido pelo Google) - `module_07/02_data_science/58_tensorflow/tensorflow.md` e `main.py`
* [ ] Deep Learning: Keras (API de alto nível, agora integrada ao TensorFlow) - `module_07/02_data_science/59_keras/keras.md` e `main.py`
* [ ] Deep Learning: PyTorch (desenvolvido pelo Facebook, muito popular em pesquisa) - `module_07/02_data_science/60_pytorch/pytorch.md` e `main.py`

#### 7.3: Automação e Scripting

* [ ] Automação Web (Web Scraping/Testing): Selenium (controla um navegador web como Chrome, Firefox para automação e testes) - `module_07/03_automation_scripting/61_selenium/selenium.md` e `main.py`
* [ ] Automação Web: Beautiful Soup 4 (BS4) (para extrair dados de arquivos HTML e XML, web scraping) - `module_07/03_automation_scripting/62_beautiful_soup/beautiful_soup.md` e `main.py`
* [ ] Automação Web: Scrapy (um framework completo para web scraping and crawling) - `module_07/03_automation_scripting/63_scrapy/scrapy.md` e `main.py`
* [ ] Automação de Tarefas: Bibliotecas da biblioteca padrão: `os`, `shutil` (manipular arquivos/pastas), `subprocess` (executar comandos do sistema) - `module_07/03_automation_scripting/64_task_automation/task_automation.md` e `main.py`
* [ ] Automação de Tarefas: PyAutoGUI (para controlar mouse e teclado) - `module_07/03_automation_scripting/65_pyautogui/pyautogui.md` e `main.py`

#### 7.4: Desenvolvimento de Interfaces Gráficas (Desktop)

* [ ] Tkinter (biblioteca padrão de GUI do Python) - `module_07/04_gui_development/66_tkinter/tkinter.md` e `main.py`
* [ ] PyQt ou PySide (*bindings* para o framework Qt, muito poderoso e profissional) - `module_07/04_gui_development/67_pyqt_pyside/pyqt_pyside.md` e `main.py`
* [ ] Kivy (framework para criar aplicações multiplataforma: Windows, Mac, Linux, iOS e Android com a mesma base de código) - `module_07/04_gui_development/68_kivy/kivy.md` e `main.py`

### Módulo 8: Tópicos Avançados e Boas Práticas

#### 8.1. Testes Automatizados

* [ ] Conceitos de Teste (Unitário, Integração) - `module_08/01_automated_testing/69_testing_concepts/testing_concepts.md`
* [ ] Bibliotecas: `unittest` (padrão) e Pytest (preferido pela comunidade) - `module_08/01_automated_testing/70_unittest_pytest/main.py`

#### 8.2. Código Limpo e Padrões

* [ ] PEP 8 (guia oficial de estilo do Python) - `module_08/02_clean_code/71_pep8/pep8.md`
* [ ] Linters e Formatadores (Flake8, Black) - `module_08/02_clean_code/72_linters_formatters/linters_formatters.md`

#### 8.3. Tópicos Avançados da Linguagem

* [ ] Programação Assíncrona (`asyncio`, `async`/`await`) - `module_08/03_advanced_topics/73_asyncio/main.py`
* [ ] Metaclasses e Programação Concorrente (Threads vs. Processos) - `module_08/03_advanced_topics/74_metaclasses_concurrency/main.py`

#### 8.4. Produção e Deploy

* [ ] Docker (empacotando aplicações em contêineres) - `module_08/04_production_deploy/75_docker/docker.md`
* [ ] Conceitos de CI/CD (Integração Contínua / Entrega Contínua) - `module_08/04_production_deploy/76_ci_cd/ci_cd.md`
