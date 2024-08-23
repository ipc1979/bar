from abc import ABC, abstractmethod

from app.domain.order import Order

class IOrdersRepository(ABC):

    @abstractmethod
    def get_order_by_id(self, id: str) -> (dict|None):
        pass