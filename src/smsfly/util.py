from functools import wraps
from bs4 import BeautifulSoup as bs

from .errors import (
    XMLError, PhoneError, StartTimeError,
    EndTimeError, LifetimeError, SpeedError,
    AlphanameError, TextError, InsufficientFundsError
)


ERROR_MAP = {
    'XMLERROR': XMLError,
    'ERRPHONES': PhoneError,
    'ERRSTARTTIME': StartTimeError,
    'ERRENDTIME': EndTimeError,
    'ERRLIFETIME': LifetimeError,
    'ERRSPEED': SpeedError,
    'ERRALFANAME': AlphanameError,
    'ERRTEXT': TextError,
    'INSUFFICIENTFUNDS': InsufficientFundsError
}

def parse_xml_response(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        res_xml = bs(f(*args, **kwargs), features='lxml-xml')
        state_code = res_xml.message.state['code']
        try:
            raise ERROR_MAP[state_code]
        except KeyError:
            return res_xml
    return wrapper
