import unittest
import datetime
from person import Person  # теперь всё совпадает

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.p = Person('Alice', 1990)

    def test_get_name(self):
        self.assertEqual(self.p.get_name(), 'Alice')

    def test_set_name(self):
        self.p.set_name('Bob')
        self.assertEqual(self.p.get_name(), 'Bob')

    def test_get_age(self):
        current_year = datetime.datetime.now().year
        self.assertEqual(self.p.get_age(), current_year - 1990)

    def test_get_address_default(self):
        self.assertEqual(self.p.get_address(), '')

    def test_set_address(self):
        self.p.set_address('Moscow')
        self.assertEqual(self.p.get_address(), 'Moscow')

    def test_is_homeless_true(self):
        self.assertTrue(self.p.is_homeless())

    def test_is_homeless_false(self):
        self.p.set_address('Moscow')
        self.assertFalse(self.p.is_homeless())

if __name__ == '__main__':
    unittest.main()
