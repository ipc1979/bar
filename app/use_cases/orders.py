from app.providers.orders_repository import IOrdersRepository


def get_order_by_id(id: str, repository: IOrdersRepository):
    order = repository.get_order_by_id(id=id)
    if order:
        del order["id"]
    return order

