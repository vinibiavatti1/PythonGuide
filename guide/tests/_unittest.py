"""
Unittest

* The unittest Python module is a module that provides ways to create unit
  tests for your code
* It is based on Erich Gamma's JUnit and Kent Beck's Smalltalk testing
  framework
* This module contains the core framework classes that form the basis of
  specific test cases and suites (TestCase, TestSuite etc.), and also a
  text-based utility class for running the tests and reporting the results
  (TextTestRunner)
* NOTE: As convention, the test methods must has the "test_" signature as
  prefix
* NOTE: The -v argument can be used in the runner to check more details of
  the test execution

TestCase Assertions
###############################################################################
Assert expr.                        Equivalent
###############################################################################
assertEqual(a, b)                   a == b
assertNotEqual(a, b)                a != b
assertTrue(x)                       bool(x) is True
assertFalse(x)                      bool(x) is False
assertIs(a, b)                      a is b
assertIsNot(a, b)                   a is not b
assertIsNone(x)                     x is None
assertIsNotNone(x)                  x is not None
assertIn(a, b)                      a in b
assertNotIn(a, b)                   a not in b
assertIsInstance(a, b)              isinstance(a, b)
assertNotIsInstance(a, b)           not isinstance(a, b)
assertRaises(error, fn, *args)      raise Error
###############################################################################

TestCase Hooks
###############################################################################
Method                              Definition
###############################################################################
setUpClass(cls)                     Execute before the test
setUp(self)                         Execute before each test
tearDownClass(cls)                  Execute after the test
tearDown(self)                      Execute after each test
###############################################################################
"""


###############################################################################
# Imports
###############################################################################


# Importing the unittest module
# * To define the unit tests, the unittest module must be imported
# * The unittest.main method is used to execute the tests
from unittest import TestCase, main
from collections.abc import Iterable


###############################################################################
# Testcase
###############################################################################


# TestCase class
# * To create a test, the TestCase class from unittest module is used as a base
#   class for the test class
# * The test case has some methods to configure the test, and assertions that
#   can be used to validate the values
# * The following code will create an test class
# * The methods inside the class are optionals
class FirstTest(TestCase):

    # setUpClass()
    # * A class method called before tests in an individual class are run.
    #   setUpClass is called with the class as the only argument and must be
    #   decorated as a classmethod()
    @classmethod
    def setUpClass(cls):
        print('Execute before the test')

    # setUp()
    # * Method called to prepare the test fixture. This is called immediately
    #   before calling the test method
    def setUp(self):
        print('Execute before each tests')

    # tearDownClass()
    # * A class method called after tests in an individual class have run.
    #   tearDownClass is called with the class as the only argument and must be
    #   decorated as a classmethod()
    @classmethod
    def tearDownClass(cls):
        print('Execute after the test')

    # tearDown()
    # * Method called immediately after the test method has been called and the
    #   result recorded. This is called even if the test method raised an
    #   exception
    def tearDown(self):
        print('Execute after each test')


###############################################################################
# Testcase assertions
###############################################################################


# Assertions
# * The assertion methods provide by the TestCase class are used to validate
#   the values of the test
# * The following class has the most used asserts
class SecondTest(TestCase):
    def test(self):
        a, b, c, d = 1, True, False, None
        self.assertEqual(a, 1)                # a == b
        self.assertNotEqual(a, 2)             # a != b
        self.assertTrue(b)                    # bool(x) is True
        self.assertFalse(c)                   # bool(x) is False
        self.assertIs(d, None)                # a is b
        self.assertIsNot(d, 1)                # a is not b
        self.assertIsNone(d)                  # x is None
        self.assertIsNotNone(a)               # x is not None
        self.assertIn(a, [0, 1, 2])           # a in b
        self.assertNotIn(a, [3, 4, 5])        # a not in b
        self.assertIsInstance(a, int)         # isinstance(a, b)
        self.assertNotIsInstance(a, str)      # not isinstance(a, b)
        self.assertRaises(TypeError, any, a)  # raise Error


###############################################################################
# Create TestCase
###############################################################################


# Create resource to be tested
# * In this example, we will create a class that will be tests in the test
#   suite
class List:
    def __init__(self):
        self.elements = []

    def add(self, element):
        self.elements.append(element)

    def __len__(self):
        return len(self.elements)

    def get(self, index):
        if index < 0 or index >= len(self.elements):
            raise IndexError('Index out of range')
        return self.elements[index]


# Create TestCase
# * To create the tests, the TestCase class is used as a base class for the
#   test class that will be created
class ListTest(TestCase):

    # Execute before each test
    def setUp(self):
        self.lst = List()

    def test_init(self):
        self.assertIsInstance(self.lst.elements, Iterable)

    def test_add(self):
        self.lst.add('a')
        self.assertIn('a', self.lst.elements)

    def test_len(self):
        self.lst.add('a')
        self.lst.add('b')
        self.assertEqual(len(self.lst), 2)

    def test_get(self):
        self.lst.add('a')
        self.lst.add('b')
        e1 = self.lst.get(0)
        e2 = self.lst.get(1)
        self.assertEqual(e1, 'a')
        self.assertEqual(e2, 'b')

    def test_get_raises_out_of_range(self):
        self.assertRaises(IndexError, self.lst.get, -1)
        self.assertRaises(IndexError, self.lst.get, 999)

    # Execute after each test
    def tearDown(self):
        del self.lst


###############################################################################
# Execute unit tests
###############################################################################


# Execute unit tests
# * To execute the unit test, the main() function of the unittest module must
#   be called
# * It is recommended to call this function in the __name__ validation of the
#   module
if __name__ == '__main__':
    main()
    # Test result:
    """
    .....
    ----------------------------------------------------------------------
    Ran 5 tests in 0.000s

    OK
    """
