import unittest
import re
from methods import Admin, SuperAdmin
from validation import Validate, USERS
from connection import Connection


class SuperAdminTests(unittest.TestCase):

    VALID_INIT = ("Correct@email.com", 'AQwe12!_', )
    VALID_EMAIL = 'Correct@email.com'
    VALID_PASSWORD = 'AQwe12!_'
    # invalid data
    INVALID_INIT = ("Incorrect@@email.com", 12345678, )
    INVALID_EMAIL = 'Incorrect@email.com'
    INVALID_PASSWORD = 12345678
    ADMIN_DATA = [{
        "first_name": "Billssss",
        "last_name": "Bobb",
        "date_of_bitrth": "02.05.1684",
        "phone": "+380966809260",
        "address": "Streee1..qewqwe.",
        "password": "123Afsdf!",
        "email": "opa@mail.dog",
        "role": "admin",
        "discount": 20
    }]
    INVALID_ADMIN_DATA = [{
        "first_name": "Billssss",
        "last_name": "Bobb",
        "date_of_bitrth": "02.05.1684",
        "phone": "+380966809260",
        "address": "Streee1..qewqwe.",
        "password": "123Afsdf!",
        "email": "opa@mail.dog",
        "role": "admin",
        "discount": 20
    }]

    def setUp(self):

        # create SuperAdmin
        self.super_admin = SuperAdmin(self.VALID_EMAIL, self.VALID_PASSWORD)
        # return super().setUp()

    def tearDown(self):
        # selector = Connection.getNextId('users',)-1
        # self.super_admin.delete_admin(selector)
        return super().tearDown()

    def clear_record(self, table):
        selector = Connection.getNextId(table)-1
        self.super_admin.delete_admin(selector)

    def validate_fields(self, request, model, model_name):
        pass

    def test_create_SuperAdmin(self):

        super_admin_valid = SuperAdmin(self.VALID_EMAIL, self.VALID_PASSWORD)
        self.assertIsInstance(super_admin_valid, SuperAdmin)

        print('Test 1.1: pass.')

    def test_create_invalid_SuperAdmin(self):
        super_admin = SuperAdmin(self.INVALID_EMAIL, self.INVALID_PASSWORD)
        self.assertRaises(ValueError, msg='Incorrect email!gggg')
        self.assertIsInstance(self.INVALID_EMAIL, str)
        self.assertIsInstance(self.INVALID_PASSWORD,
                              str)
        self.assertIsInstance(super_admin, SuperAdmin, 'Error')
        print('Test 1.2: pass.')

        strong_pattern = re.compile(
            r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z])(?=.*[*.!@$%^&(){}[\]:;<>,.?\/~_+-=|\\]).{8,}$')

    def test_add_admin(self):
        Validate().validate(self.ADMIN_DATA[0], USERS, 'Users')
        response = self.super_admin.add_admin(self.ADMIN_DATA)
        self.assertEqual(response, 'Insert done!')
        print('Test 1.3: pass.')
        self.clear_record('users')


if __name__ == '__main__':
    unittest.main()
