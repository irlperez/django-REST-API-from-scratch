import unittest

### requirements ###
# - put our tests into classes as methods
# - use a series of special assertion methods in the unittest.TestCase class instead of the built-in 'assert' statement

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1,2,3]), 6, 'should be 6')
    
    def test_sum_tuple(self):
        self.assertEqual(sum([1,2,2]), 6, 'should be 6')

if __name__ == '__main__':
    unittest.main()

### results ###
# . = pass
# f = fail
'''
Ran 2 tests in 0.000s

FAILED (failures=2)
❯ python3 2test_sum_unittest.py
.F
======================================================================
FAIL: test_sum_tuple (__main__.TestSum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/perez/Documents/coding/github/irlperez/django-REST-API-from-scratch/2test_sum_unittest.py", line 12, in test_sum_tuple
    self.assertEqual(sum([1,2,2]), 6, 'should be 6')
AssertionError: 5 != 6 : should be 6

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)


'''