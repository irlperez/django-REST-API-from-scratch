# after test_sum 1 and 2 i moved on to pytest.
# https://docs.pytest.org/en/7.1.x/getting-started.html
# pip3 install -U pytest > created a sample file > run 'pytest'

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

'''
pytest will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories. More generally, it follows standard test discovery rules.
'''