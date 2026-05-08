# Desafio MBA Engenharia de Software com IA - Full Cycle

# RAG Chat com PGVector + OpenAI

Aplicação Python de RAG (Retrieval-Augmented Generation) utilizando:

- OpenAI Embeddings
- PostgreSQL + PGVector
- LangChain
- OpenAI LLM
- Chat via terminal

O sistema:

1. Recebe uma pergunta do usuário
2. Vetoriza a pergunta
3. Busca os documentos mais relevantes no PGVector
4. Monta um contexto
5. Envia o prompt para a LLM
6. Retorna uma resposta baseada apenas no contexto encontrado

---

# Arquitetura

```text
Usuário
   ↓
Pergunta
   ↓
OpenAI Embeddings
   ↓
PGVector Similarity Search
   ↓
Top K documentos
   ↓
Construção do Prompt
   ↓
LLM OpenAI
   ↓
Resposta
```

# Estrutura do Projeto

```
├── docker-compose.yml
├── requirements.txt      # Dependências
├── .env.example          # Template da variável OPENAI_API_KEY
├── src/
│   ├── ingest.py         # Script de ingestão do PDF
│   ├── search.py         # Script de busca
│   ├── chat.py           # CLI para interação com usuário
├── document.pdf          # PDF para ingestão
└── README.md             # Instruções de execução
```

# Requisitos

- Python 3.10+
- PostgreSQL
- Extensão PGVector habilitada
- Chave da OpenAI

# Criar ambiente virtual

## Linux / Mac

```bash
python -m venv venv
source venv/bin/activate
```

## Windows

```bash
python -m venv venv
venv\Scripts\activate
```

# Instalar dependências

```bash
pip install -r requirements.txt
```

ou

## Se der erro de versão

```bash
pip install langchain langchain-community langchain-postgres langchain-openai langchain-google-genai python-dotenv beautifulsoup4 pypdf
```

## Recriar o requirements.txt atualizado

```bash
pip freeze > requirements.txt
```

# Ordem de execução

1. Subir o banco de dados:

```bash
docker compose up -d
```

2. Executar ingestão do PDF:

```bash
python src/ingest.py
```

3. Rodar o chat:

```bash
python src/chat.py
```

# Exemplo de uso

```
=== CHAT RAG ===
Digite 'sair' para encerrar.

Faça sua pergunta:

PERGUNTA: Qual o faturamento da Empresa SuperTechIABrazil?
RESPOSTA: O faturamento foi de 10 milhões de reais.

PERGUNTA: sair
```

# Exemplo de uso fora de contexto

```
=== CHAT RAG ===
Digite 'sair' para encerrar.

Faça sua pergunta:

PERGUNTA: Quantos clientes temos em 2024?
RESPOSTA: Não tenho informações necessárias para responder sua pergunta.

PERGUNTA: sair
```

# Encerrar o chat

Digite sair ou exit
