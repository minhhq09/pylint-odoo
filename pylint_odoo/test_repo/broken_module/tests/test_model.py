from odoo.tests.common import TransactionCase


class TestModel(TransactionCase):
    def setUp(self):
        super(TestModel, self).setUp()

    def method1(self, example_var):
        return example_var
