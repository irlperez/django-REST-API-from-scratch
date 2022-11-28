# learning about python testing
# https://realpython.com/python-testing/

# assert sum([1,2,3]) == 6, 'should be 6' # won't show anything in console
# assert sum([1,1,1]) == 6, 'should be 6' # will show the error message

def test_sum():
    assert sum([1,2,3]) == 6, 'should be 6' # placed within a function

def test_sum_tuple():
    assert sum([(1,2,2)]) == 6, 'should be 6' # placed within a function

if __name__ == '__main__':
    test_sum() # call the test
    print('everything passed') # tests will run > nothing will be returned > then this message is printed