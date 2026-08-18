# Payments API

API simples de pagamentos construída com FastAPI, criada para praticar o fluxo de
versionamento `dev → stage → prod` com Git e Pull Requests.

## Requisitos

- Python 3.10+
- pip

## Como rodar

```bash
# 1. Criar e ativar um ambiente virtual (opcional, mas recomendado)
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Rodar o servidor
uvicorn main:app --reload
```

A API sobe em `http://127.0.0.1:8000`.
Documentação interativa (Swagger) disponível em `http://127.0.0.1:8000/docs`.

## Endpoints

### `POST /payments`

Cria um novo pagamento.

**Request:**
```json
{
  "amount": 100.00,
  "currency": "BRL",
  "payer": "alice",
  "payee": "bob"
}
```

**Response (201):**
```json
{
  "id": "pay_a1b2c3d4",
  "status": "created",
  "amount": 100.0,
  "currency": "BRL",
  "payer": "alice",
  "payee": "bob"
}
```

### `GET /payments`

Lista todos os pagamentos criados (adicionado na Parte 4 do desafio).

## Estrutura

- `main.py` — aplicação FastAPI e definição dos endpoints.
- `requirements.txt` — dependências do projeto.
- Os dados são mantidos em memória (não há banco de dados).
