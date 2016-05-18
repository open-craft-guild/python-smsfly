from httmock import all_requests


@all_requests
def getbalance_success(url, request):
    return """
        <?xml version="1.0" encoding="utf-8"?>
        <message>
            <balance>123.156</balance>
        </message>
        """
