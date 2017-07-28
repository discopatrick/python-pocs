from unittest import TestCase

from src.multiple_inheritance import SubClass

class MultipleInheritanceTest(TestCase):

    def test_execution_order_two_parents_with_same_method_name_and_common_parent(self):

        subclass = SubClass()
        subclass.do_this()

        self.assertEqual(subclass.list_, ['common parent', 'second', 'first'])
