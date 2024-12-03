# https://www.codewars.com/kata/514a024011ea4fb54200004b
import re
import pytest
url = "http://google.com"

def domain_name(url):
    regex = r"(?:https?:\/\/)?(?:www\.)?([a-zA-Z0-9-]+)\."
    temp = re.search(regex,url)
    domain = temp.group(1)
    return domain

@pytest.mark.parametrize("url,expected_name", [
    ('http://google.com', 'google'),
    ('http://google.co.jp', 'google'),
    ('https://hyphen-site.org', 'hyphen-site'),
    ('http://www.codewars.com/kata/', 'codewars')
])
def test_domain_name(url,expected_name):
    name = domain_name(url)
    assert name == expected_name
