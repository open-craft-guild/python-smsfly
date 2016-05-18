try:
    import unittest2 as unittest
except ImportError:
    import unittest

import httpretty

from smsfly import SMSFlyAPI


class APITest(unittest.TestCase):
    def setUp(self):
        self.api = SMSFlyAPI(account_id='3801234567', account_pass='qwerty')
        return super().setUp()

    @httpretty.activate
    def test_getbalance(self):
        httpretty.register_uri(httpretty.POST, 'http://sms-fly.com/api/api.php',
                               body="""<?xml version="1.0" encoding="utf-8"?>
                                       <message>
                                           <balance>123.156</balance>
                                       </message>
                                    """)
        self.assertEqual(self.api.getbalance(), 123.156)

    def test_construct_xml_payload_base(self):
        message = self.api._SMSFlyAPI__construct_xml_payload_base(operation='GETBALANCE')
        expected = '<?xml version="1.0" encoding="utf-8"?>\n<request><operation>GETBALANCE</operation></request>'
        self.assertEqual(str(message), expected)
