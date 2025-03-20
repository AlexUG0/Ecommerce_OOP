import pytest

from src.lawngrass import LawnGrass


def test_category_init(category):
    assert category.name == "Смартфоны"
    assert category.description == ("Смартфоны, как средство не только коммуникации, "
                                    "но и получения дополнительных функций для удобства жизни")
    assert len(category.product_in_list) == 3

    assert category.category_count == 1
    assert category.product_count == 3


def test_category_products_property(category, product):
    assert category.products == ("Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
                                 "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
                                 "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
                                 )


def test_add_product(category, product2):
    category.add_product(product2)
    assert category.products == ("Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
                                 "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
                                 "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
                                 "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n")


def test_category_str(category):
    assert str(category) == "Смартфоны, количество продуктов: 27 шт."


def test_add_product_error(grass):
    with pytest.raises(TypeError):
        LawnGrass()
