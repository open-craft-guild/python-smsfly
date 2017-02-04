.. image:: https://badge.waffle.io/open-craft-guild/python-smsfly.png?label=ready&title=Ready
   :target: https://waffle.io/open-craft-guild/python-smsfly
   :alt: Stories in Ready

.. image:: https://img.shields.io/pypi/v/SMSFly.svg
   :target: https://pypi.org/project/SMSFly

.. image:: https://img.shields.io/travis/open-craft-guild/python-smsfly/master.svg?label=Linux%20build%20%40%20Travis%20CI
   :target: http://travis-ci.org/open-craft-guild/python-smsfly

.. image:: https://img.shields.io/pypi/pyversions/SMSFly.svg

.. image:: https://img.shields.io/pypi/dm/SMSFly.svg

.. image:: https://api.codacy.com/project/badge/Grade/78ef3eba02d94d15bca00c841696fbb6
   :target: https://www.codacy.com/app/webknjaz/python-smsfly?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=open-craft-guild/python-smsfly&amp;utm_campaign=Badge_Grade

.. image:: https://requires.io/github/open-craft-guild/python-smsfly/requirements.svg?branch=master
   :target: https://requires.io/github/open-craft-guild/python-smsfly/requirements/?branch=master
   :alt: Requirements Status

python-smsfly
-------------

SMS-Fly gateway API Python package

Install it
##########

.. code-block:: sh

    pip install SMSFly

Development
###########

.. code-block:: sh

    pip install -e .[test,dev]
    nosetests --ipdb

Testing
#######

.. code-block:: shell

    pip install -e .[test]
    nosetests

Usage
#####

.. code-block:: python
   :number-lines:

    from smsfly import SMSFlyAPI
    api = SMSFlyAPI(account_id='3801234567', account_pass='qwerty')
    api.getbalance()

Other implementations
#####################
* `PHP package <https://github.com/vchizi/SMSFly>`_
