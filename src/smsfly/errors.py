class XMLError(SyntaxError):
    """Incorrect XML was sent to API"""


class PhoneError(ValueError):
    """Incorrect phone of recipient"""


class StartTimeError(ValueError):
    """Incorrect start time for sending messages"""


class EndTimeError(ValueError):
    """Incorrect end time of campaign"""


class StartTimeError(ValueError):
    """Incorrect start time of campaign"""


class LifetimeError(ValueError):
    """Incorrect lifetime of campaign"""


class SpeedError(ValueError):
    """Incorrect speed for sending messages"""


class AlphanameError(NameError):
    """The name is forbidden for use, or there's an error in it"""


class TextError(ValueError):
    """Incorrect text of message"""


class InsufficientFundsError(Exception):
    """Insufficient funds. Unable to send messages"""
