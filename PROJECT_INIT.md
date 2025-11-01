# Projeto: Curso Pessoal de Python

## Visão Geral

Este projeto tem como objetivo criar um curso de Python completo e prático, com todas as aulas, exemplos de código e explicações documentadas e versionadas em um repositório Git. A metodologia de ensino será incremental, começando pelos conceitos mais básicos e avançando gradualmente para tópicos mais complexos.

## Objetivos Principais do Curso

1. **Fundamentos Sólidos:** Ensinar os conceitos fundamentais da linguagem Python, garantindo que o aluno tenha uma base sólida para construir conhecimentos mais avançados.
2. **Aprendizagem Prática:** Focar em exemplos de código práticos e exercícios que demonstrem o uso real dos conceitos ensinados em cada aula.
3. **Estrutura Modular:** Organizar o curso em módulos e aulas sequenciais, facilitando o acompanhamento e a revisão do conteúdo. A estrutura de diretórios reflete essa modularidade (ex: `01-hello-world`, `02-variables-and-types`, etc.).
4. **Versionamento com Git:** Utilizar o Git e o GitHub para documentar todo o progresso, permitindo que o aluno (e a IA) possa revisitar o histórico de aprendizado e gerenciar o código de forma eficiente.
5. **Automação da Tutoria:** Capacitar a IA a assistir na criação das aulas, na escrita dos códigos, na documentação e na gestão do repositório, seguindo as diretrizes estabelecidas.
6. **Integração de Tecnologias Avançadas:** Introduzir conceitos de backend (FastAPI, SQLAlchemy), frontend básico e IA generativa, simulando projetos do mundo real para construir um portfólio competitivo.

## Estado Atual

O projeto já foi iniciado e as seguintes aulas foram criadas, cada uma com código comentado e exemplos práticos seguindo as melhores práticas de Python (PEP 8 e "The Zen of Python"):

* [01-hello-world](http://_vscodecontentref_/1): Introdução básica ao Python com o comando `print()`.
* [02-variables-and-types](http://_vscodecontentref_/2): Conceitos de variáveis e tipos de dados primitivos.

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
