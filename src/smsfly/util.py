import logging

from functools import wraps
from bs4 import BeautifulSoup as bs

from .errors import (
    XMLError, PhoneError, StartTimeError,
    EndTimeError, LifetimeError, SpeedError,
    AlphanameError, TextError, InsufficientFundsError,
    AuthError
)


logger = logging.getLogger(__name__)

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
        logger.debug('Raw API response: {}'.format(res_text))

        if res_text == 'Access denied!':
            logger.error('Oops.. Authentication data is invalid')
            raise AuthError

        res_xml = bs(res_text, features='lxml-xml')

        try:
            res_state = res_xml.message.state
            if res_state:
                logger.debug("There's state specified in API response: {}. "
                             "Checking whether it's an error message...".
                             format(res_state))
                exc = ERROR_MAP[res_state.attrs['code']]
                logger.error('Exception happened: {}'.format(exc))
                raise exc
        except (KeyError, AttributeError):
            logger.debug('No error stated in <state> tag of API response: {}')
            return res_xml
        else:
            logger.debug('No exception has been raised while processing API response')
            return res_xml

    return wrapper
