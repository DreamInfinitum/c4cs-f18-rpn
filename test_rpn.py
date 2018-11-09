import unittest
import rpn


class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('2 3 +')
		self.assertEqual(5, result)

	def test_sub(self):
		result = rpn.calculate('4 6 -')
		self.assertEqual(-2, result)

	def test_exp(self):
		result = rpn.calculate('4 8 ^')
		self.assertEqual(65536, result)

	def test_per(self):
		result = rpn.calculate('64 25 %')
		self.assertEqual(16, result)

	def test_div(self):
		result = rpn.calculate('72 3 /')
		self.assertEqual(24, result)

	def test_and(self):
		result = rpn.calculate('63 63 &')
		self.assertEqual(63, result)

	def test_or(self):
		result = rpn.calculate('63 64 |')
		self.assertEqual(127, result)

	def test_not(self):
		result = rpn.calculate('6 ~')
		self.assertEqual(-7, result)

	def test_toomany_add(self):
		with self.assertRaises(ValueError):
			result = rpn.calculate('1 2 3 +')

	def test_toomany_sub(self):
		with self.assertRaises(ValueError):
			result = rpn.calculate('1 2 3 -')

	def test_toomany_exp(self):
		with self.assertRaises(ValueError):
			result = rpn.calculate('1 2 3 ^')
