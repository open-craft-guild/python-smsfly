class XMLError(SyntaxError):
    """Incorrect XML was sent to API"""
    pass


class PhoneError(ValueError):
    """Incorrect phone of recipient"""
    pass


class StartTimeError(ValueError):
    """Incorrect start time for sending messages"""
    pass


class EndTimeError(ValueError):
    """Incorrect end time of campaign"""
    pass


class LifetimeError(ValueError):
    """Incorrect lifetime of campaign"""
    pass


class SpeedError(ValueError):
    """Incorrect speed for sending messages"""


class AlphanameError(ValueError):
    """The name is forbidden for use, or there's an error in it"""
    pass


class TextError(ValueError):
    """Incorrect text of message"""
    pass


class InsufficientFundsError(Exception):
    """Insufficient funds. Unable to send messages"""
    pass


class AuthError(ValueError):
    """Authentication failed"""
    pass
