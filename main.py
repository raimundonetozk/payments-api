from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import uuid

app = FastAPI(title="Payments API")

# "Banco de dados" em memória
payments_db: dict[str, dict] = {}


class PaymentCreate(BaseModel):
    amount: float = Field(..., gt=0, description="Valor do pagamento, deve ser positivo")
    currency: str = Field(..., min_length=3, max_length=3, description="Código da moeda, ex: BRL")
    payer: str
    payee: str


class PaymentResponse(BaseModel):
    id: str
    status: str
    amount: float
    currency: str
    payer: str
    payee: str


@app.post("/payments", response_model=PaymentResponse, status_code=201)
def create_payment(payment: PaymentCreate):
    payment_id = f"pay_{uuid.uuid4().hex[:8]}"
    record = {
        "id": payment_id,
        "status": "created",
        "amount": payment.amount,
        "currency": payment.currency.upper(),
        "payer": payment.payer,
        "payee": payment.payee,
    }
    payments_db[payment_id] = record
    return record
