import pytest

from src.category import Category
from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


@pytest.fixture
def product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product2():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def product3():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def category():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        [Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),

         Product("Iphone 15", "512GB, Gray space", 210000.0, 8),

         Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)]
    )


@pytest.fixture
def new_prod_param():
    return {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
            "quantity": 5}


@pytest.fixture
def smartphone1():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra",
                      256, "Серый")


@pytest.fixture
def smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def grass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
