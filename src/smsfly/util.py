from functools import wraps
from bs4 import BeautifulSoup as bs

from .errors import (
    XMLError, PhoneError, StartTimeError,
    EndTimeError, LifetimeError, SpeedError,
    AlphanameError, TextError, InsufficientFundsError,
    AuthError
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
        res_text = f(*args, **kwargs).text

        if res_text == 'Access denied!':
            raise AuthError

        res_xml = bs(res_text, features='lxml-xml')
        res_state = res_xml.message.state

        try:
            if res_state:
                raise ERROR_MAP[res_state['code'].text]
        except KeyError:
            return res_xml
        else:
            return res_xml

    return wrapper
