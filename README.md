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

### Primeira Etapa

A tabela abaixo apresenta os tempos médios de execução do script `hydration.py` para a criação de cada arquivo de texto com dados aleatórios:

| Arquivo            | Tempo Médio |
| ------------------ | ----------- |
| movimentations.txt | ~7.51ms     |
| bets.txt           | ~4.83ms     |
| clients.txt        | ~2.04ms     |
| games.txt          | ~0.44ms     |

### Segunda Etapa

A tabela seguinte demonstra os tempos médios necessários para o carregamento dos arquivos de texto pelo programa principal durante sua inicialização:

| Arquivo            | Tempo Médio |
| ------------------ | ----------- |
| movimentations.txt | ~0.27ms     |
| bets.txt           | ~0.26ms     |
| clients.txt        | ~0.21ms     |
| games.txt          | ~0.14ms     |
