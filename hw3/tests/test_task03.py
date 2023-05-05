#here is test for raw unrefactoring code (test_task03_v1) and for refactored test_task03_v2

import pytest
import os, sys
sys.path.append(os.path.abspath('../'))
from task03_v2 import make_filter, make_positive_even

sample_data  =  [
     {
         "name": "Bill",
         "last_name": "Gilbert",
         "occupation": "was here",
         "type": "person",
     },
     {
         "is_dead": True,
         "kind": "parrot",
         "type": "bird",
         "name": "polly"
     }
]

def test_positive_even():
    seq = make_positive_even()
    for num in seq:
        assert num %2 == 0
        assert num >= 0
        assert isinstance(num, int)



@pytest.mark.parametrize('sample_data, kwargs', [(sample_data, {'name':'polly', 'type':'bird'})])
def test_make_filter(sample_data, kwargs):
    data = make_filter(**kwargs).apply(sample_data)
    for key, value in kwargs.items():
        assert data[0][key] == value

