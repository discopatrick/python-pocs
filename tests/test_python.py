from unittest import TestCase
from src.functions import *

class FunctionTest(TestCase):

    def test_function_returns_a_value(self):

        val = return_a_value()

        self.assertIsNotNone(val)
