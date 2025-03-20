from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый абстрактный класс для Product"""
    @abstractmethod
    def __add__(self, other):
        pass


class InitMixin:
    """Класс-миксин для  печати в консоль информации при создании объекта, то есть при работе метода __init__"""
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return (
            f"{self.__class__.__name__}({self.name}, {self.description}, "
            f"{self.price}, {self.quantity})"
        )


class Product(BaseProduct, InitMixin):
    """Класс для описания товаров"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is self.__class__:
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, params):
        return cls(**params)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price
