class Shop:

    total_sales = 0

    def __init__(self, name, sales_number):
        self.name = name
        self.sales_number = sales_number

    def increase_sales(self, sales_number):
        self.sales_number += sales_number
        self.__class__.total_sales += sales_number

    @classmethod
    def increase_total_sales(cls, sales_number):
        cls.total_sales += sales_number


shop1 = Shop('Silpo', 4000)
shop2 = Shop('ATB', 8000)

Shop.increase_total_sales(340)