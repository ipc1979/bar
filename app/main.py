from fastapi import FastAPI, HTTPException
from app.use_cases.orders import get_order_by_id

app = FastAPI()

@app.get("/orders/{id}")
async def controller_get_order_by_id(id):
    
    try:
        order = get_order_by_id(id)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    return order

