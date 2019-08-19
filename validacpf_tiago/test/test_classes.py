import unittest
from source.utils.validator import Validator
from source.utils.formatter import Formatter


class Tester(unittest.TestCase):

    def test_format_it(self):
        self.assertEqual(Formatter.format_it('123-456-789-09'), '12345678909')

    def test_validate(self):
        self.assertTrue(Validator.validate('123-456-789-09'))
        self.assertFalse(Validator.validate('123-456-789-10'))
        self.assertFalse(Validator.validate('111.111.111-11'))


if __name__ == '__main__':
    unittest.main()
