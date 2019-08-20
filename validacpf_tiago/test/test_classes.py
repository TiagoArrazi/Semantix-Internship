import unittest
from source.utils.validator import Validator


class Tester(unittest.TestCase):

    def test_format_(self):
        self.assertEqual(Validator.format_('123-456-789-09'), '12345678909')

    def test_validate(self):
        self.assertTrue(Validator.validate('123-456-789-09'))
        self.assertFalse(Validator.validate('123-456-789-10'))
        self.assertFalse(Validator.validate('111.111.111-11'))


if __name__ == '__main__':
    unittest.main()
