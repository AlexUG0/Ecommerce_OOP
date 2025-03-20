from src.product import Product


class Category:
    """ Класс для описания категорий товаров """
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        prods_quantity = 0
        for product in self.__products:
            prods_quantity += product.quantity
        return f"{self.name}, количество продуктов: {prods_quantity} шт."

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    @property
    def product_in_list(self):
        return self.__products
