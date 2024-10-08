from fastapi.testclient import TestClient
import pytest

from .main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_get_order_by_id(client):
    response = client.get("/orders/1")
    assert response.status_code == 200
    assert response.json() == {
        "created": "2024-09-10T12:00:00",
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
                "created":  "2024-09-10T12:00:30",
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
                "created":  "2024-09-10T12:20:31",
                "items": [
                    {
                        "name": "Club Colombia",
                        "quantity": 1
                    },
                    {
                        "name": "Quilmes",
                        "quantity": 2
                    }
                ]
            },
            {
                "created":  "2024-09-10T12:43:21",
                "items": [
                    {
                        "name": "Quilmes",
                        "quantity": 3
                    }
                ]
            }
        ]
    }

def test_get_orders_by_id_when_id_not_found(client):
    response = client.get("/orders/2")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Order not found"
    }

    