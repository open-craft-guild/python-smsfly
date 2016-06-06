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
        httpretty.register_uri(httpretty.POST, SMSFlyAPI.API_URL,
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

        httpretty.register_uri(httpretty.POST, SMSFlyAPI.API_URL, body=request_callback)

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

    @httpretty.activate
    def test_add_alphaname(self):
        httpretty.register_uri(httpretty.POST, SMSFlyAPI.API_URL,
                               body="""<?xml version="1.0" encoding="utf-8"?>
                                       <message>
                                           <state alfaname="TEST_ALPHANAME" status="MODERATE" />
                                       </message>
                                    """)

        alphaname_res = self.api.add_alphaname('TEST_ALPHANAME')
        self.assertEqual(alphaname_res.state.attrs['alfaname'], 'TEST_ALPHANAME')  # it's `alfaname` due to docs :(
        self.assertEqual(alphaname_res.state.attrs['status'], 'MODERATE')

    @httpretty.activate
    def test_check_alphaname(self):
        httpretty.register_uri(httpretty.POST, SMSFlyAPI.API_URL,
                               body="""<?xml version="1.0" encoding="utf-8"?>
                                       <message>
                                           <state alfaname="TEST_ALPHANAME" status="ACTIVE" />
                                       </message>
                                    """)

        alphaname_res = self.api.check_alphaname('TEST_ALPHANAME')
        self.assertEqual(alphaname_res.state.attrs['alfaname'], 'TEST_ALPHANAME')  # it's `alfaname` due to docs :(
        self.assertEqual(alphaname_res.state.attrs['status'], 'ACTIVE')

    @httpretty.activate
    def test_get_alphanames_list(self):
        expected_results = (
            ('TEST_ALPHANAME', 'ACTIVE'),
            ('GRAMMAR_NAZI', 'ACTIVE'),
            ('LALALA', 'MODERATE'),
        )

        httpretty.register_uri(httpretty.POST, SMSFlyAPI.API_URL,
                               body="""<?xml version="1.0" encoding="utf-8"?>
                                       <message>
                                           <state alfaname="TEST_ALPHANAME" status="ACTIVE" />
                                           <state alfaname="GRAMMAR_NAZI" status="ACTIVE" />
                                           <state alfaname="LALALA" status="MODERATE" />
                                       </message>
                                    """)

        alphaname_res = self.api.get_alphanames_list()
        for n, state in enumerate(alphaname_res.findAll('state')):
            self.assertEqual(state.attrs['alfaname'], expected_results[n][0])  # it's `alfaname` due to docs :(
            self.assertEqual(state.attrs['status'], expected_results[n][1])
