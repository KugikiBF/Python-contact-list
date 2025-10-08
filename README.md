# Ultimo_desafio
## 📝 Descrição

Este é um projeto de um sistema de cadastro de pessoas desenvolvido em Python, que roda diretamente no terminal (CLI - Command-Line Interface). A aplicação permite ao usuário visualizar pessoas já cadastradas, adicionar novos registros e sair do sistema de forma segura. Todos os dados são armazenados localmente em um arquivo de texto (`.txt`), garantindo a persistência das informações entre as sessões.

## ✨ Funcionalidades

* **Listar Pessoas:** Exibe uma lista formatada de todas as pessoas cadastradas, com nome e idade.
* **Cadastrar Nova Pessoa:** Solicita o nome e a idade do usuário para adicionar um novo registro.
* **Persistência de Dados:** Salva automaticamente os registros em um arquivo `pessoas_cadastradas.txt`.
* **Criação Automática de Arquivo:** Se o arquivo de banco de dados não existir, o sistema o cria automaticamente na primeira execução.
* **Interface Amigável no Terminal:** Utiliza um menu de opções claro e mensagens coloridas para feedback ao usuário.
* **Tratamento de Erros:** Valida a entrada de dados para garantir que a idade seja um número inteiro e lida com possíveis falhas na leitura ou escrita do arquivo.

## 🚀 Conceitos e Tecnologias Utilizadas

Este projeto foi uma oportunidade para praticar e consolidar conceitos fundamentais da programação com Python:

* **Python 3**
* **Modularização de Código:** O projeto é estruturado em funções, cada uma com uma responsabilidade única.
* **Manipulação de Arquivos:** Abertura, leitura, escrita e criação de arquivos de texto (`open`, `with`, modos `rt`, `wt+`, `at`).
* **Tratamento de Exceções:** Uso de blocos `try...except` para criar um programa robusto e à prova de falhas.
* **Estruturas de Dados:** Uso de listas e strings.
* **Lógica de Programação:** Laços de repetição (`while`) e condicionais (`if`, `elif`, `else`).

