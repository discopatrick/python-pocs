from unittest import TestCase
from src.functions import *
from src.classes import *

class FunctionTest(TestCase):

    def test_function_returns_a_value(self):

        val = return_a_value()

        self.assertIsNotNone(val)

class ClassTest(TestCase):

    def test_class_can_be_instantiated(self):

        my_object = Person()

        self.assertIsInstance(my_object, Person)
