# Projeto: Curso Pessoal de Python

## Visão Geral

Este projeto tem como objetivo criar um curso de Python completo e prático, seguindo uma estrutura modular incremental, com todas as aulas, exemplos de código e explicações documentadas e versionadas em um repositório Git. A progressão vai do básico ao avançado, incluindo especializações em web, dados e automação.

---

## Objetivos Principais do Curso

1. **Fundamentos Sólidos:** Ensinar os conceitos fundamentais da linguagem Python, garantindo que o aluno tenha uma base sólida para construir conhecimentos mais avançados.
2. **Aprendizagem Prática:** Focar em exemplos de código práticos e exercícios que demonstrem o uso real dos conceitos ensinados em cada aula.
3. **Estrutura Modular:** Organizar o curso em módulos e aulas sequenciais, facilitando o acompanhamento e a revisão do conteúdo. A estrutura de diretórios reflete essa modularidade (ex: `01-hello-world`, `02-variables-and-types`, etc.).
4. **Versionamento com Git:** Utilizar o Git e o GitHub para documentar todo o progresso, permitindo que o aluno (e a IA) possa revisitar o histórico de aprendizado e gerenciar o código de forma eficiente.
5. **Automação da Tutoria:** Capacitar a IA a assistir na criação das aulas, na escrita dos códigos, na documentação e na gestão do repositório, seguindo as diretrizes estabelecidas.
6. **Integração de Tecnologias Avançadas:** Introduzir conceitos de backend (FastAPI, SQLAlchemy), frontend básico e IA generativa, simulando projetos do mundo real para construir um portfólio competitivo.

---

## Estrutura Geral do Curso

O curso é dividido em 8 módulos, do básico ao avançado. Cada aula prática tem um `main.py` com docstring, comentários, exemplos e exercício. Aulas teóricas usam `.md` bem formatados. Diretórios seguem `module_XX/submodule/YY-topic/`.

---

## Estado Atual

O projeto já foi iniciado com algumas aulas básicas, que serão reposicionadas para a nova estrutura modular (ex: `00-import-this` vai para `module_01/introduction/00-import-this/`). As aulas existentes incluem introdução ao Python e conceitos iniciais. A nova estrutura TODO lista todas as lições a serem desenvolvidas ou movidas, priorizando Módulos 1 e 2 para respeitar a ordem sequencial.

---

## Próximos Passos para a IA

Para dar continuidade ao curso de onde paramos, a IA deve seguir o seguinte fluxo para cada nova aula:

1. **Aguardar o Tópico:** Esperar que o aluno/usuário defina o tema da próxima aula (ex: "Operadores Aritméticos").
2. **Criar a Estrutura:**
    * Criar um novo diretório para a aula, seguindo o padrão de numeração sequencial (ex: `03-operators`).
    * Dentro do novo diretório, criar um arquivo `main.py`.
3. **Desenvolver o Conteúdo:**
    * No arquivo `main.py`, escrever o código Python que exemplifica o tópico da aula.
    * Utilizar comentários no código para explicar cada conceito de forma clara e didática, como se fosse o professor.
4. **Documentar e Versionar:**
    * Adicionar os novos arquivos (`<numero>-<topico>/main.py`) ao controle de versão (`git add .`).
    * Gerar uma mensagem de commit clara e descritiva, seguindo o padrão "feat: Create lesson on <TÓPICO DA AULA>" (ex: "feat: Create lesson on arithmetic operators").
    * Realizar o commit das mudanças.
5. **Confirmar e Avançar:** Informar ao usuário que a aula foi criada e comitada, e aguardar a instrução para a próxima aula ou qualquer outra solicitação.
6. **Refinar e Conectar ao Mercado:** Após o commit, sugerir atualizações no [README.md](http://_vscodecontentref_/3) principal com um resumo da aula. Explicar como essa habilidade agrega valor ao portfólio (ex: "Essa aula demonstra fundamentos essenciais para entrevistas em Python"). Aguarde feedback do usuário para ajustes ou a próxima aula.

---

## Diretrizes de Estilo e Linguagem

Para garantir a clareza e a eficácia do aprendizado, seguir as seguintes diretrizes:

* Conteúdo das aulas (docstrings, comentários, explicações em .md) em português para facilitar o aprendizado. Nomes de variáveis, diretórios, arquivos e termos Python (ex: `if`, `for`, nomes de funções) em inglês, seguindo PEP 8 e boas práticas de programação.

## TODO: Estrutura Completa do Curso

Esta lista TODO descreve todas as aulas a serem criadas ou reposicionadas, seguindo a estrutura modular. Aulas existentes serão movidas para novos diretórios. Use [x] para concluídas, [ ] para pendentes. Diretórios: `module_XX/submodule/YY-topic/`. Aulas práticas: `main.py`; Teóricas: `topic.md`.

### Módulo 1: Fundamentos (O Básico)

#### 1.1. Introdução e Configuração

* [x] O que é Python? (Filosofia, usos) - `module_01/introduction/00-import-this/main.py`
* [ ] Instalar Python (e a diferença entre Python 2 vs 3) - `module_01/introduction/01-python-installation/python_installation.md`
* [ ] Configurando o Ambiente de Desenvolvimento (IDEs como VS Code, PyCharm) - `module_01/introduction/02-development-environment/development_environment.md`
* [ ] Usando o Interpretador (REPL) - `module_01/introduction/03-interpreter-repl/interpreter_repl.md` e `main.py`
* [x] Seu primeiro programa: `print("Olá, Mundo!")` - `module_01/introduction/04-hello-world/main.py`

#### 1.2. Sintaxe Básica

* [x] Variáveis (Nomenclatura e atribuição) - `module_01/basic-syntax/05-variables/main.py` (reposicionar de 02-variables-and-types)
* [x] Tipos de Dados Primitivos: Inteiros (`int`), Ponto flutuante (`float`), Strings (`str`) e formatação (f-strings), Booleanos (`bool`) - `module_01/basic-syntax/06-data-types/main.py` (reposicionar de 02-variables-and-types)
* [x] Operadores (Aritméticos, de Comparação, Lógicos) - `module_01/basic-syntax/07-arithmetic-operators/main.py` (reposicionar de 03-arithmetic-operators)
* [ ] Entrada e Saída (`input()` e `print()`) - `module_01/basic-syntax/08-input-output/main.py`
* [ ] Comentários e Indentação (a regra mais importante do Python) - `module_01/basic-syntax/09-comments-indentation/comments_indentation.md` e `main.py`

### Módulo 2: Estruturas de Controle e Lógica

#### 2.1. Lógica Condicional

* [ ] `if`, `elif`, `else` - `module_02/control-structures/10-conditional-logic/main.py`

#### 2.2. Estruturas de Repetição (Loops)

* [ ] `for` (iterando sobre sequências) - `module_02/control-structures/11-for-loops/main.py`
* [ ] `while` (loops baseados em condição) - `module_02/control-structures/12-while-loops/main.py`
* [ ] Controle de loops: `break` e `continue` - `module_02/control-structures/13-loop-control/main.py`
* [ ] A função `range()` - `module_02/control-structures/14-range-function/main.py`

### Módulo 3: Estruturas de Dados

#### 3.1. Sequências e Coleções

* [ ] Listas (Lists): Mutáveis, ordenadas (criação, indexação, fatiamento, métodos como `.append()`, `.pop()`) - `module_03/data-structures/15-lists/main.py`
* [ ] Tuplas (Tuples): Imutáveis, ordenadas - `module_03/data-structures/16-tuples/main.py`
* [ ] Dicionários (Dictionaries): Pares chave-valor, desordenados (até Python 3.6), mutáveis - `module_03/data-structures/17-dictionaries/main.py`
* [ ] Conjuntos (Sets): Itens únicos, desordenados, operações de conjunto (união, interseção) - `module_03/data-structures/18-sets/main.py`
* [ ] Métodos de iteração para cada estrutura - `module_03/data-structures/19-iteration-methods/main.py`

### Módulo 4: Funções e Modularidade

#### 4.1. Funções

* [ ] Definindo funções (`def`) - `module_04/functions-modularity/20-defining-functions/main.py`
* [ ] Argumentos e Parâmetros (posicionais, nomeados, padrão) - `module_04/functions-modularity/21-arguments-parameters/main.py`
* [ ] Retornando valores (`return`) - `module_04/functions-modularity/22-return-values/main.py`
* [ ] Escopo de Variáveis (Local vs. Global) - `module_04/functions-modularity/23-variable-scope/main.py`
* [ ] Funções Anônimas (`lambda`) - `module_04/functions-modularity/24-lambda-functions/main.py`

#### 4.2. Modularidade

* [ ] Importando módulos (`import`, `from ... import`) - `module_04/functions-modularity/25-importing-modules/main.py`
* [ ] Módulos da Biblioteca Padrão (ex: `math`, `random`, `datetime`) - `module_04/functions-modularity/26-standard-library/main.py`
* [ ] Criando seus próprios módulos (arquivos `.py`) - `module_04/functions-modularity/27-custom-modules/main.py`

#### 4.3. Gerenciamento de Pacotes

* [ ] Introdução ao Pip (instalando pacotes externos, ex: `pip install requests`) - `module_04/functions-modularity/28-pip-introduction/pip_introduction.md`
* [ ] O arquivo `requirements.txt` - `module_04/functions-modularity/29-requirements-txt/requirements_txt.md`
* [ ] Ambientes Virtuais (`venv`) - Um conceito crucial para projetos - `module_04/functions-modularity/30-virtual-environments/virtual_environments.md`

### Módulo 5: Programação Orientada a Objetos (POO)

#### 5.1. Conceitos de POO

* [ ] Classes e Objetos (Instâncias) - `module_05/oop/31-classes-objects/main.py`
* [ ] Atributos (dados da classe/objeto) - `module_05/oop/32-attributes/main.py`
* [ ] Métodos (funções da classe) - `module_05/oop/33-methods/main.py`
* [ ] Construtores (`__init__`) e o parâmetro `self` - `module_05/oop/34-constructors-self/main.py`

#### 5.2. Pilares da POO

* [ ] Herança: Criando subclasses que herdam de classes-mãe - `module_05/oop/35-inheritance/main.py`
* [ ] Encapsulamento: Protegendo dados (atributos privados/públicos) - `module_05/oop/36-encapsulation/main.py`
* [ ] Polimorfismo: Objetos de diferentes classes respondendo ao mesmo método - `module_05/oop/37-polymorphism/main.py`
* [ ] Métodos Mágicos (Métodos Dunder), como `__str__` e `__repr__` - `module_05/oop/38-magic-methods/main.py`

### Módulo 6: Tópicos Intermediários

#### 6.1. Manipulação de Erros

* [ ] Tratamento de Exceções: `try`, `except`, `else`, `finally` - `module_06/intermediate/39-exception-handling/main.py`
* [ ] Lançando exceções (`raise`) - `module_06/intermediate/40-raising-exceptions/main.py`

#### 6.2. Manipulação de Arquivos

* [ ] Lendo e escrevendo arquivos (`open()`, `with open(...)`) - `module_06/intermediate/41-file-handling/main.py`
* [ ] Trabalhando com formatos comuns (CSV, JSON) - Bibliotecas: `csv` e `json` (da biblioteca padrão) - `module_06/intermediate/42-csv-json/main.py`

#### 6.3. Tópicos "Pythônicos"

* [ ] Compreensões de Lista (Forma concisa de criar listas) - `module_06/intermediate/43-list-comprehensions/main.py`
* [ ] Geradores (`yield`) e Expressões Geradoras - `module_06/intermediate/44-generators/main.py`
* [ ] Decoradores (`@decorator`) - `module_06/intermediate/45-decorators/main.py`

### Módulo 7: Especializações (Bibliotecas e Frameworks)

#### 7.A: Desenvolvimento Web (Backend)

* [ ] Conceitos: HTTP (GET, POST), APIs REST, ORM (Mapeador Objeto-Relacional) - `module_07/specializations/46-web-concepts/web_concepts.md`
* [ ] Frameworks: Flask (micro-framework, ótimo para começar e APIs menores) - `module_07/specializations/47-flask/flask.md` e `main.py`
* [ ] Frameworks: Django (framework "completo", com bateria incluída, painel de admin, ORM próprio, sistema de autenticação) - `module_07/specializations/48-django/django.md` e `main.py`
* [ ] Frameworks: FastAPI (framework moderno de alta performance para criar APIs, com validação de dados e documentação automática) - `module_07/specializations/49-fastapi/fastapi.md` e `main.py`
* [ ] Bibliotecas Comuns: SQLAlchemy (ORM principal do Python, usado com Flask/FastAPI) - `module_07/specializations/50-sqlalchemy/sqlalchemy.md` e `main.py`
* [ ] Bibliotecas Comuns: Requests (para fazer requisições HTTP, consumindo outras APIs) - `module_07/specializations/51-requests/requests.md` e `main.py`

#### 7.B: Ciência de Dados e Machine Learning

* [ ] Análise e Manipulação de Dados: NumPy (biblioteca fundamental para computação numérica, arrays N-dimensionais) - `module_07/specializations/52-numpy/numpy.md` e `main.py`
* [ ] Análise e Manipulação de Dados: Pandas (a biblioteca mais importante para manipulação e análise de dados, DataFrames) - `module_07/specializations/53-pandas/pandas.md` e `main.py`
* [ ] Visualização de Dados: Matplotlib (biblioteca-base para gráficos e plots) - `module_07/specializations/54-matplotlib/matplotlib.md` e `main.py`
* [ ] Visualização de Dados: Seaborn (baseado no Matplotlib, para visualizações estatísticas mais bonitas) - `module_07/specializations/55-seaborn/seaborn.md` e `main.py`
* [ ] Machine Learning (ML): Scikit-learn (sklearn) (biblioteca principal para algoritmos clássicos de ML: regressão, classificação, clustering) - `module_07/specializations/56-scikit-learn/scikit_learn.md` e `main.py`
* [ ] Deep Learning (Tópico Avançado de ML): TensorFlow (desenvolvido pelo Google) - `module_07/specializations/57-tensorflow/tensorflow.md` e `main.py`
* [ ] Deep Learning: Keras (API de alto nível, agora integrada ao TensorFlow) - `module_07/specializations/58-keras/keras.md` e `main.py`
* [ ] Deep Learning: PyTorch (desenvolvido pelo Facebook, muito popular em pesquisa) - `module_07/specializations/59-pytorch/pytorch.md` e `main.py`

#### 7.C: Automação e Scripting

* [ ] Automação Web (Web Scraping/Testing): Selenium (controla um navegador web como Chrome, Firefox para automação e testes) - `module_07/specializations/60-selenium/selenium.md` e `main.py`
* [ ] Automação Web: Beautiful Soup 4 (BS4) (para extrair dados de arquivos HTML e XML, web scraping) - `module_07/specializations/61-beautiful-soup/beautiful_soup.md` e `main.py`
* [ ] Automação Web: Scrapy (um framework completo para web scraping e crawling) - `module_07/specializations/62-scrapy/scrapy.md` e `main.py`
* [ ] Automação de Tarefas: Bibliotecas da biblioteca padrão: `os`, `shutil` (manipular arquivos/pastas), `subprocess` (executar comandos do sistema) - `module_07/specializations/63-task-automation/task_automation.md` e `main.py`
* [ ] Automação de Tarefas: PyAutoGUI (para controlar mouse e teclado) - `module_07/specializations/64-pyautogui/pyautogui.md` e `main.py`

#### 7.D: Desenvolvimento de Interfaces Gráficas (Desktop)

* [ ] Tkinter (biblioteca padrão de GUI do Python) - `module_07/specializations/65-tkinter/tkinter.md` e `main.py`
* [ ] PyQt ou PySide (*bindings* para o framework Qt, muito poderoso e profissional) - `module_07/specializations/66-pyqt-pyside/pyqt_pyside.md` e `main.py`
* [ ] Kivy (framework para criar aplicações multiplataforma: Windows, Mac, Linux, iOS e Android com a mesma base de código) - `module_07/specializations/67-kivy/kivy.md` e `main.py`

### Módulo 8: Tópicos Avançados e Boas Práticas

#### 8.1. Testes Automatizados

* [ ] Conceitos de Teste (Unitário, Integração) - `module_08/advanced/68-testing-concepts/testing_concepts.md`
* [ ] Bibliotecas: `unittest` (padrão) e Pytest (preferido pela comunidade) - `module_08/advanced/69-unittest-pytest/main.py`

#### 8.2. Código Limpo e Padrões

* [ ] PEP 8 (guia oficial de estilo do Python) - `module_08/advanced/70-pep8/pep8.md`
* [ ] Linters e Formatadores (Flake8, Black) - `module_08/advanced/71-linters-formatters/linters_formatters.md`

#### 8.3. Tópicos Avançados da Linguagem

* [ ] Programação Assíncrona (`asyncio`, `async`/`await`) - `module_08/advanced/72-asyncio/main.py`
* [ ] Metaclasses e Programação Concorrente (Threads vs. Processos) - `module_08/advanced/73-metaclasses-concurrency/main.py`

#### 8.4. Produção e Deploy

* [ ] Docker (empacotando aplicações em contêineres) - `module_08/advanced/74-docker/docker.md`
* [ ] Conceitos de CI/CD (Integração Contínua / Entrega Contínua) - `module_08/advanced/75-ci-cd/ci_cd.md`
