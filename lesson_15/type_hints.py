from typing import Tuple, List, Union, Optional, Any


def delete_o(string: str):
    return string.replace('o', '')


def count_products(products: Tuple[str, ...]):
    return len(products)


# def get_sum(arg: List[Union[Tuple[str, int], float, int]]) -> Union[int, float]:
#     return sum(arg)


def test_func(a: Optional[int] = 40):
    print(a)


test_func('100')


# get_sum([1, 2, 3, 4, 5, 100.0, 204.12312, ('123', '1')])


products_cart = ('strawberry', 'milk', 'potato', 'tomato')
count_products(products_cart)

