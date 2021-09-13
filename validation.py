from logging import raiseExceptions
import psycopg2
from setup import *

import datetime
import re
# from methods import SuperAdmin, Admin
import unittest
# RegEX patterns
name_pattern = r'^([a-zA-Zа-щА-ЩЬьЮюЯяЇїІіЄєҐґ]+)\-?([a-zA-Zа-щА-ЩЬьЮюЯяЇїІіЄєҐґ]+)$'
email_pattern = r'^([a-zA-Z0-9-_\*\.]+)@([a-zA-Z0-9-]+)(\.[a-zA-Z0-9]+)+$'
password_pattern = r'^((?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{6,}))|((?=.*[a-z])(?=.*[A-Z])(?=.*[^A-Za-z0-9])(?=.{8,}))$'
phone_pattern = r'^\+\d{12}$'
date_pattern = r'^(0?[1-9]|[12][0-9]|3[01])[-\.\/](0?[1-9]|1[012])[-\.\/]([0-9]{4})'
address_pattern = r"[A-Za-z0-9'\.\-\s\,]"
role_pattern = r'^(admin|user|super)$'
discount_pattern = ""
number_pattern = r'^\d+\.?[0-9]*$'


# models
USERS = {"id": [int, number_pattern],
         "first_name": [str, name_pattern],
         "last_name": [str, name_pattern],
         "date_of_bitrth": [str, date_pattern],
         "phone": [str, phone_pattern],
         "address": [str, address_pattern],
         "password": [str, password_pattern],
         "email": [str, email_pattern],
         "role": [str, role_pattern],
         "discount": [int, number_pattern]}

ORDERS = {
    "id":[int, number_pattern],
    "date_of_order" :[str, date_pattern],
    "customer_id" : [int, number_pattern],
    "product_id": [int, number_pattern],
    "price":[int, number_pattern]
}

PRODUCT = {
    "id":[int, number_pattern],
    "code":[int, number_pattern],
    "product_name":[str],
    "unit_price":[int, number_pattern],
    "count":[int, number_pattern],
    "description":[str],
    "img":[str],
    "sub_category_id":[int, number_pattern]
}

PRODUCT_CATEGORY = {
    "id":[int, number_pattern],
    "category_name":[str]
}

PRODUCT_SUBCATEGORY = {
    "id":[int, number_pattern],
    "subcategory_name":[str],
    "category_name":[int, number_pattern]
}


class Validate(unittest.TestCase):
    def validate(self, request, model, model_name):
        for key in request:
            self.assertIn(
                key, model, f'Field "{key}" is not in {model_name} model. Incorrect field name!')
            self.assertIsInstance(
                request[key], model[key][0], f'Field "{key}" has invalid type for {model_name} model, it must been {model[key][0].__name__}. Type error!')
            value = request[key].strip() if isinstance(
                request[key], str) else str(request[key])
            self.assertRegex(
                value, model[key][1].strip(), f'Field "{key}" has incorrect value for {model_name} model, it must been {model[key][0]}. Value error!')


if __name__ == '__main__':

    admin_1_data = [{
        "first_name": "Billssss",
        "last_name": "Bobb",
        "date_of_bitrth": "02.05.1684",
        "phone": "+380966809260",
        "address": "Streee1.\\-\\,\\s",
        "password": "Sd111%11",
        "email": "opa@mail.dog",
        "role": "admin",
        "discount": 20
    }]
    Validate().validate(admin_1_data[0], USERS, 'users')
    # admin_1 = SuperAdmin('asdas@gmail.com', 'Sd111%11')
    # admin_1.add_admin(admin_1_data)
