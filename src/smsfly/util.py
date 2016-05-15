from functools import wraps
from bs4 import BeautifulSoup as bs


def parse_xml_response(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        # TODO: implement exception detection
        return bs(f(*args, **kwargs), features='lxml-xml')
    return wrapper
