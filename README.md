[![Stories in Ready](https://badge.waffle.io/wk-tech/python-smsfly.png?label=ready&title=Ready)](https://waffle.io/wk-tech/python-smsfly) [![Build Status](https://travis-ci.org/wk-tech/python-smsfly.svg?branch=master)](https://travis-ci.org/wk-tech/python-smsfly) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/78ef3eba02d94d15bca00c841696fbb6)](https://www.codacy.com/app/webknjaz/python-smsfly?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=wk-tech/python-smsfly&amp;utm_campaign=Badge_Grade) [![Requirements Status](https://requires.io/github/wk-tech/python-smsfly/requirements.svg?branch=master)](https://requires.io/github/wk-tech/python-smsfly/requirements/?branch=master)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/SMSFly.svg)](https://pypi.python.org/pypi/SMSFly) [![Version @ PYPI](https://img.shields.io/pypi/v/SMSFly.svg)](https://pypi.python.org/pypi/SMSFly)
# python-smsfly
SMS-Fly gateway API Python package

## Development
```sh
pip install -e .[test,dev]
nosetests --ipdb
```

## Testing
```sh
pip install -e .[test]
nosetests
```

## Usage
```python
from smsfly import SMSFlyAPI
api = SMSFlyAPI(account_id='3801234567', account_pass='qwerty')
api.getbalance()
```

## Other implementations
* [PHP package](https://github.com/vchizi/SMSFly)
