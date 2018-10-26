import unittest
import rpn


class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('2 3 +')
		self.assertEqual(5, result)

	def test_sub(self):
		result = rpn.calculate('4 6 -')
		self.assertEqual(-2, result)

	def test_toomany_add(self)
		with self.assertRaises(ValueError):
			result = rpn.calculate('1 2 3 +')

	def test_toomany_sub(self)
		with self.assertRaises(ValueError):
			result = rpn.calculate('1 2 3 -')
