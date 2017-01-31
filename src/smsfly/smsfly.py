import logging
import os

import requests as req
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup as bs

from .util import parse_xml_response


logger = logging.getLogger(__name__)


class SMSFlyAPI:
    API_URL = 'http://sms-fly.com/api/api.php'

    def __init__(self, account_id=os.getenv('SMSFLY_ID'), account_pass=os.getenv('SMSFLY_PASS')):
        session = req.Session()
        session.auth = HTTPBasicAuth(account_id, account_pass)
        self.__http = session
        logger.debug('SMS-Fly API wrapper has been initialized')

    @parse_xml_response
    def __request(self, request_xml_body):
        req_body = str(request_xml_body).encode('utf-8')
        logger.debug('Submitting POST request to SMS-Fly API {}.\nRequest body: {}'.
                     format(self.API_URL, req_body))
        return self.__http.post(self.API_URL, data=req_body)

    def __construct_xml_payload_base(self, *, operation):
        soup = bs(features='lxml-xml')
        soup.append(soup.new_tag('request'))
        op = soup.new_tag('operation')
        op.string = operation
        soup.request.append(op)
        return soup

    def send_sms_to_recipient(self, *, start_time, end_time, lifetime, rate, desc, source, body, recipient):
        return self.__sendsms(start_time, end_time, lifetime, rate, desc, source,
                              message_pairs=((recipient, body), ), individual_mode=False)

    def send_sms_to_recipients(self, *, start_time, end_time, lifetime, rate, desc, source, body, recipients):
        message_pairs = list(map(lambda r: [r], recipients))
        message_pairs[0][1] = body
        return self.__sendsms(start_time, end_time, lifetime, rate, desc,
                              source, message_pairs, individual_mode=False)

    def send_sms_pairs(self, *, start_time, end_time, lifetime, rate, desc, source, message_pairs):
        return self.__sendsms(start_time, end_time, lifetime, rate, desc,
                              source, message_pairs, individual_mode=True)

    def __sendsms(self, start_time, end_time, lifetime, rate, desc,
                  source, message_pairs, individual_mode=False):
        add_body = True
        xml_req = self.__construct_xml_payload_base(operation='SENDSMS')
        msg = xml_req.new_tag('message', start_time=start_time, end_time=end_time,
                              lifetime=lifetime, rate=rate, desc=desc, source=source)
        xml_req.request.append(msg)
        for recipient, body in message_pairs:
            if not individual_mode:
                if add_body:
                    add_body = not add_body
                    xml_req.request.message.append(xml_req.new_tag('body'))
                    xml_req.request.message.body.append(body)
            else:
                bod = xml_req.new_tag('body')
                bod.append(body)
                xml_req.request.message.append(bod)
            rec = xml_req.new_tag('recipient')
            rec.append(recipient)
            xml_req.request.message.append(rec)
        return self.__request(xml_req)

    def __getcampaigninfo(self, *, campaign_id):
        xml_req = self.__construct_xml_payload_base(operation='GETCAMPAIGNINFO')
        xml_req.request.append(xml_req.new_tag('message', campaignID=str(campaign_id)))
        return self.__request(xml_req)

    getcampaigninfo = __getcampaigninfo

    def __getcampaigndetail(self, *, campaign_id):
        xml_req = self.__construct_xml_payload_base(operation='GETCAMPAIGNDETAIL')
        xml_req.request.append(xml_req.new_tag('message', campaignID=str(campaign_id)))
        return self.__request(xml_req)

    getcampaigndetail = __getcampaigndetail

    def __getmessagestatus(self, *, campaign_id, recipient):
        xml_req = self.__construct_xml_payload_base(operation='GETCAMPAIGNINFO')
        message = xml_req.new_tag('message', campaignID=str(campaign_id), recipient=str(recipient))
        xml_req.request.append(message)
        return self.__request(xml_req)

    getmessagestatus = __getmessagestatus

    def __getbalance(self):
        return self.__request(self.__construct_xml_payload_base(operation='GETBALANCE'))

    def getbalance(self):
        return float(self.__getbalance().message.balance.text)

    def add_alphaname(self, alphaname):
        return self.__managealfaname(command_id='ADDALFANAME', alfaname=alphaname)

    def check_alphaname(self, alphaname):
        return self.__managealfaname(command_id='CHECKALFANAME', alfaname=alphaname)

    def get_alphanames_list(self):
        return self.__managealfaname(command_id='GETALFANAMESLIST')

    def __managealfaname(self, *, command_id, alfaname=None):
        xml_req = self.__construct_xml_payload_base(operation='MANAGEALFANAME')
        xml_req.request.append(xml_req.new_tag('command', id=command_id))

        if alfaname:
            xml_req.request.command['alfaname'] = alfaname

        return self.__request(xml_req)
