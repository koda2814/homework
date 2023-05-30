import pytest
import responses
#responses is usefil library which changes response from server by our local mock-file.
#every time in test func, when we`re trying to reach certain url we will get our mock-file 

import os, sys
sys.path.append(os.path.abspath('../../'))
from task_2_mock_input import count_dots_on_i


mock_body = open('mock_page.html', 'r').read()


@responses.activate
def test_count_dots_on_i():
    responses.add(method=responses.GET, url='https://example.com', body=mock_body, status=200)
    res = count_dots_on_i('https://example.com')
    assert res == 62


@responses.activate
def test_err_code():
    responses.add(method=responses.GET, url='https://example.com', json='{"error": "not found"}', status=404, content_type='application/json')
    with pytest.raises(ValueError):
        res = count_dots_on_i('https://example.com')
        print('ValueError')

#pytest --html=report.html --self-contained-html