import json


#### PYTHON APP ####
cart = {
    'strawberry': {
        'quantity': 3,
        'total_price': 100
    },
    'tomato': {
        'quantity': 1,
        'total_price': 20
    },
    'is_paid': True,
    'distinct_products': ['strawberry', 'tomato']

}


res = json.dumps(cart)
print(res)

#### ANOTHER LANGUAGE APPLICATION ###

deserealized_obj = json.loads(res)
print(type(deserealized_obj))