# Relatório - Las Vegas Casino

## 1. Introdução

Este documento apresenta o sistema de gerenciamento de cassino desenvolvido como projeto da disciplina de Programação 1. O sistema implementa funcionalidades completas de CRUD (Create, Read, Update, Delete) para gerenciamento de apostas, clientes, jogos e movimentações financeiras, utilizando arquivos de texto como mecanismo de persistência de dados.

## 2. Decisões de Projeto

### 2.1 Estrutura de Diretórios

A estrutura do projeto foi organizada de forma hierárquica, priorizando a separação clara
entre código-fonte, dados de entrada e saídas do sistema.

### 2.2 Modelagem das Classes

A modelagem dos agragados foi concebida como uma representação direta da estrutura dos arquivos. Assim, cada classe do sistema corresponde a um arquivo específico, onde suas propriedades mapeiam as colunas do arquivo.

<div style="page-break-after: always;"></div>

#### 2.2.1 Classe Bet (Aposta)

Representa uma aposta realizada por um cliente em um jogo específico, mantendo registro completo da transação incluindo valor apostado, resultado obtido e pagamento efetuado.

```python
- id: int (chave primária)
- client_id: str (referência ao cliente)
- game_id: int (referência ao jogo)
- amount: float (valor apostado)
- outcome: str (resultado da aposta)
- payout: float (valor do pagamento)
- datetime: str (data e hora)
- odds_breakdown: list (detalhamento das odds)
```

#### 2.2.2 Classe Client (Cliente)

Encapsula as informações cadastrais e financeiras dos clientes do cassino, incluindo dados pessoais, saldo disponível e nível de privilégio no sistema.

```python
- id: int (chave primária)
- first_name: str (primeiro nome)
- last_name: str (sobrenome)
- country: str (país de origem)
- balance: float (saldo disponível)
- vip_level: int (nível VIP)
- payment_methods: list (métodos de pagamento)
```

#### 2.2.3 Classe Game (Jogo)

Define as características operacionais de cada jogo disponível no cassino, estabelecendo parâmetros como limites de apostas, categoria e regras específicas.

```python
- id: int (chave primária)
- name: str (nome do jogo)
- house_edge: float (vantagem da casa)
- min_bet: float (aposta mínima)
- max_bet: float (aposta máxima)
- category: str (categoria do jogo)
- active: bool (status de ativação)
- rules: list (regras do jogo)
```

<div style="page-break-after: always;"></div>

#### 2.2.4 Classe Movimentation (Movimentação)

Registra todas as transações financeiras realizadas no sistema, proporcionando rastreabilidade completa das operações monetárias entre diferentes entidades.

```python
- transaction_id: int (chave primária)
- sender: str (remetente)
- recipient: str (destinatário)
- amount: float (valor da transação)
- datetime: str (data e hora)
- transaction_type: str (tipo de transação)
- tags: list (etiquetas)
```

### 2.3 Simplicidade do script principal

O arquivo `main.py` foi mantido intencionalmente minimalista, delegando toda a complexidade para a
classe auxiliar `Program`:

```python
from src.structures.Program import Program

print("============================")
print("===== LAS VEGAS CASINO =====")
print("============================")

app = Program()
app.init()
app.loop()
app.close()
```

<div style="page-break-after: always;"></div>

## 3. Análise de Desempenho

Com o objetivo de avaliar a eficiência das operações, foram realizadas medições de tempo em cada etapa individual do projeto.

### 3.1 Primeira Etapa - Geração de Dados

A tabela abaixo apresenta os tempos médios de execução do script `hydration.py`:

| **Arquivo**          | **Tempo Médio** |
| -------------------- | --------------- |
| `movimentations.txt` | ~7.51 ms        |
| `bets.txt`           | ~4.83 ms        |
| `clients.txt`        | ~2.04 ms        |
| `games.txt`          | ~0.44 ms        |

### 3.2 Segunda Etapa - Carregamento Inicial

A tabela seguinte demonstra os tempos médios necessários para o carregamento dos arquivos de texto pelo programa principal durante sua inicialização:

| **Arquivo**          | **Tempo Médio** |
| -------------------- | --------------- |
| `movimentations.txt` | ~0.27 ms        |
| `bets.txt`           | ~0.26 ms        |
| `clients.txt`        | ~0.21 ms        |
| `games.txt`          | ~0.14 ms        |

<div style="page-break-after: always;"></div>

### 3.3 Terceira Etapa - Operações CRUD

As tabelas a seguir apresentam os tempos de execução das operações de manipulação de dados para cada entidade do sistema.

#### 3.3.1 Apostas

| **Ações**  | **Tempo de Execução** |
| ---------- | --------------------- |
| Listar     | 147.58 ms             |
| Visualizar | 1.34 ms               |
| Adicionar  | 0.08 ms               |
| Editar     | 0.07 ms               |
| Excluir    | 0.32 ms               |

#### 3.3.2 Clientes

| **Ações**  | **Tempo de Execução** |
| ---------- | --------------------- |
| Listar     | 67.73 ms              |
| Visualizar | 1.41 ms               |
| Adicionar  | 0.06 ms               |
| Editar     | 0.04 ms               |
| Excluir    | 0.37 ms               |

<div style="page-break-after: always;"></div>

#### 3.3.3 Jogos

A entidade jogos apresenta os menores tempos de listagem, resultado da quantidade reduzida de dados comparado às demais entidades.

| **Ações**  | **Tempo de Execução** |
| ---------- | --------------------- |
| Listar     | 6.74 ms               |
| Visualizar | 1.30 ms               |
| Adicionar  | 0.05 ms               |
| Editar     | 0.05 ms               |
| Excluir    | 0.37 ms               |

#### 3.3.4 Movimentações

As movimentações financeiras exibem o maior tempo de listagem dentre todas as entidades, o que é esperado considerando o alto volume de transações registradas.

| **Ações**  | **Tempo de Execução** |
| ---------- | --------------------- |
| Listar     | 295.84 ms             |
| Visualizar | 1.43 ms               |
| Adicionar  | 0.05 ms               |
| Editar     | 0.04 ms               |
| Excluir    | 0.51 ms               |

### 3.4 Persistência de Dados ao Encerramento

Ao finalizar o programa, os dados são persistidos em arquivos de saída localizados no diretório `output/`. O tempo médio necessário para a geração completa desses arquivos é de aproximadamente **399.62 ms**, garantindo que todas as alterações realizadas durante a execução do programa sejam preservadas.
