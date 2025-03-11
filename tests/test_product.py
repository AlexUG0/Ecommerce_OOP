from unittest.mock import patch

from src.product import Product


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