from unittest.mock import patch

from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_created(new_prod_param):
    product1 = Product.new_product(new_prod_param)
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_price_getter():
    product1 = Product(name="Пармезан", description="Натуральные сыры", price=99.99, quantity=10)
    assert product1.price == 99.99


def test_price_setter():
    product1 = Product(name="Пармезан", description="Натуральные сыры", price=99.99, quantity=10)
    product1.price = 120.00
    assert product1.price == 120.00
    with patch("builtins.input", return_value="no"):
        product1.price = - 121.00
        assert product1.price == 120.00


def test_product_str(product):
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(product, product2):
    assert (product + product2) == 1334000.0


def test_init_mixin(capsys):
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)"

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"


def test_middle_price(category, category_without_product):
    assert category.middle_price() == 140333.33333333334
    assert category_without_product.middle_price() == 0
