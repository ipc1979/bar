from fastapi import FastAPI, HTTPException
from app.domain.order import Order
from app.repositories.orders import OrdersRepository
from app.use_cases.orders import get_order_by_id

app = FastAPI()

@app.get("/orders/{id}", response_model=Order)
async def controller_get_order_by_id(id):

    try:
        order = get_order_by_id(id=id, repository=OrdersRepository())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {repr(e)}")
    
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    return order

