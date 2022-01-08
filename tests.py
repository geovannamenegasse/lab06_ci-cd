import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
  
  def setUp(self):
    self.calculator = Calculator()

  def testAddPositiveNumber(self):
    r = self.calculator.add(1, 2)
    self.assertEqual(3, r)

  def testAddNegativeNumber(self):
    r = self.calculator.add(1, -2)
    self.assertEqual(-1, r)

  def testSubPositiveNumber(self):
    r = self.calculator.sub(2, 1)
    self.assertEqual(1, r)

  def testSubNegativeNumber(self):
    r = self.calculator.sub(2, -1)
    self.assertEqual(3, r)

  def testMulByPositiveNumber(self):
    r = self.calculator.mul(2, 1)
    self.assertEqual(2, r)

  def testMulByNegativeNumber(self):
    r = self.calculator.mul(2, -1)
    self.assertEqual(-2, r)
  
  def testMulByZero(self):
    r = self.calculator.mul(2, 0)
    self.assertEqual(0, r)

  def testDivByPositiveNumber(self):
    r = self.calculator.div(2, 1)
    self.assertEqual(2, r)

  def testDivByNegativeNumber(self):
    r = self.calculator.div(2, -1)
    self.assertEqual(-2, r)

  def testDivByZero(self):
    r = lambda:self.calculator.div(2, 0)
    self.assertRaises(ZeroDivisionError, r)