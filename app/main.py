from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/orders/{id}")
async def get_order_by_id(id):
    orders = [
        {
            "id": "1",
            "created": "2024-09-10 12:00:00",
            "paid": False,
            "subtotal": 0,
            "taxes": 0,
            "discounts": 0,
            "items": [
                {
                    "name": "Quilmes",
                    "price_per_unit": 120,
                    "total": 5
                },
                {
                    "name": "Corona",
                    "price_per_unit": 115,
                    "total": 2
                },
                {
                    "name": "Club Colombia",
                    "price_per_unit": 110,
                    "total": 2
                }
            ],
            "rounds": [
                {
                    "created":  "2024-09-10 12:00:30",
                    "items": [
                        {
                            "name": "Corona",
                            "quantity": 2
                        },
                        {
                            "name": "Club Colombia",
                            "quantity": 1
                        }
                    ]
                },
                {
                    "created":  "2024-09-10 12:20:31",
                    "items": [
                        {
                            "name": "Club Colombia",
                            "quantity": 1
                        },
                        {
                            "name": "Quilmes",
                            "price": 2
                        }
                    ]
                },
                {
                    "created":  "2024-09-10 12:43:21",
                    "items": [
                        {
                            "name": "Quilmes",
                            "quantity": 3
                        }
                    ]
                }
            ]
        }
    ]
    order = [ order for order in orders if order["id"] == id ]
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    result = order[0]
    del result["id"]
    return result
