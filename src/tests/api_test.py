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

    @httpretty.activate
    def test_sendsms(self):
        def request_callback(request, uri, headers):
            return (200, headers, request.body)

        httpretty.register_uri(httpretty.POST, 'http://sms-fly.com/api/api.php', body=request_callback)

        message = self.api._SMSFlyAPI__sendsms(
            start_time='2016-05-31 12:25:41',
            end_time='2016-05-31 12:25:41',
            lifetime='400',
            rate='120',
            desc='Test campaign',
            source='TEST',
            message_pairs=[('380950110101', 'Hello')]
        )

        expected = ('<?xml version="1.0" encoding="utf-8"?>\n<request>'
                    '<operation>SENDSMS</operation><message desc="Test campaign"'
                    ' end_time="2016-05-31 12:25:41" lifetime="400" rate="120"'
                    ' source="TEST" start_time="2016-05-31 12:25:41">'
                    '<body>Hello</body><recipient>380950110101</recipient></message></request>')

        self.assertEqual(str(message), expected)
