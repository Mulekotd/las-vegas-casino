# Relatório - Las Vegas Casino

## Introdução

Este relatório apresenta o projeto desenvolvido para a disciplina de Programação 1, que consiste em um sistema de gerenciamento de cassino.

## Estrutura do Projeto

A organização do projeto foi planejada de forma modular para facilitar a manutenção e compreensão do código. A estrutura de diretórios adotada é apresentada a seguir:

```bash
.
├── README.md
├── database
│   ├── bets.txt
│   ├── clients.txt
│   ├── games.txt
│   └── movimentations.txt
├── hydration.py
├── main.py
└── src
    ├── __init__
    ├── structures
    │   ├── Bet.py
    │   ├── Client.py
    │   ├── File.py
    │   ├── Game.py
    │   ├── Movimentation.py
    │   ├── Program.py
    │   └── __init__
    └── utils.py
```

## Descrição dos Componentes

### Diretório Raiz

No diretório raiz do projeto encontram-se dois scripts Python principais:

- **main.py:** arquivo responsável por servir como ponto de entrada do programa principal, inicializando a aplicação e gerenciando o fluxo de execução.

- **hydration.py:** script desenvolvido para gerar arquivos de texto contendo dados aleatórios.

### Diretório database/

O diretório `database/` armazena os arquivos de texto que funcionam como base de dados persistente do sistema, contendo informações sobre apostas, clientes, jogos e movimentações financeiras.

### Diretório src/

O diretório `src/` contém os módulos auxiliares necessários para o funcionamento adequado do programa:

- **structures/:** subdiretório que agrupa as classes principais do sistema (Bet, Client, File, Game, Movimentation e Program), representando as entidades e estruturas de dados do projeto.

- **utils.py:** módulo contendo funções utilitárias utilizadas em diversas partes do sistema.

## Análise de Desempenho

Com o objetivo de avaliar a eficiência das operações, foram realizadas medições de tempo em cada etapa individual do projeto.

### Primeira Etapa - Geração de Dados

A tabela abaixo apresenta os tempos médios de execução do script `hydration.py`:

| **Arquivo**          | **Tempo Médio** |
| -------------------- | --------------- |
| `movimentations.txt` | ~7.51 ms        |
| `bets.txt`           | ~4.83 ms        |
| `clients.txt`        | ~2.04 ms        |
| `games.txt`          | ~0.44 ms        |

### Segunda Etapa - Carregamento Inicial

A tabela seguinte demonstra os tempos médios necessários para o carregamento dos arquivos de texto pelo programa principal durante sua inicialização:

| **Arquivo**          | **Tempo Médio** |
| -------------------- | --------------- |
| `movimentations.txt` | ~0.27 ms        |
| `bets.txt`           | ~0.26 ms        |
| `clients.txt`        | ~0.21 ms        |
| `games.txt`          | ~0.14 ms        |

### Terceira Etapa - Operações CRUD

As tabelas a seguir apresentam os tempos de execução das operações CRUD (Create, Read, Update, Delete) para cada entidade do sistema. É importante observar que a operação de listagem possui tempo significativamente maior devido à necessidade de processar e exibir todos os registros existentes, enquanto as demais operações atuam sobre registros individuais.

#### Apostas

| **Ações**  | **Tempo de Execução** |
| ---------- | --------------------- |
| Listar     | 147.58 ms             |
| Visualizar | 1.34 ms               |
| Adicionar  | 0.08 ms               |
| Editar     | 0.07 ms               |
| Excluir    | 0.32 ms               |

#### Clientes

| **Ações**  | **Tempo de Execução** |
| ---------- | --------------------- |
| Listar     | 67.73 ms              |
| Visualizar | 1.41 ms               |
| Adicionar  | 0.06 ms               |
| Editar     | 0.04 ms               |
| Excluir    | 0.37 ms               |

#### Jogos

A entidade Jogos apresenta os menores tempos de listagem, resultado da quantidade reduzida de jogos disponíveis no cassino comparado às demais entidades.

| **Ações**  | **Tempo de Execução** |
| ---------- | --------------------- |
| Listar     | 6.74 ms               |
| Visualizar | 1.30 ms               |
| Adicionar  | 0.05 ms               |
| Editar     | 0.05 ms               |
| Excluir    | 0.37 ms               |

#### Movimentações

As movimentações financeiras exibem o maior tempo de listagem dentre todas as entidades, o que é esperado considerando o alto volume de transações registradas.

| **Ações**  | **Tempo de Execução** |
| ---------- | --------------------- |
| Listar     | 295.84 ms             |
| Visualizar | 1.43 ms               |
| Adicionar  | 0.05 ms               |
| Editar     | 0.04 ms               |
| Excluir    | 0.51 ms               |
