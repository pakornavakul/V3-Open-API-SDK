from .client import Client
from .consts import *
from .constv5 import *


class RestAPIV5(Client):

    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, test=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, test, first)


    def get_account_position_risk(self,instType=None):
        # return self._request_without_params(GET, SPOT_ACCOUNT_INFO)
        if instType is None:
            return self._request_without_params(GET, ACCOUNT_POS_RISK)
        else:
            params = {}
            params['instType'] = instType
            return self._request_with_params(GET, ACCOUNT_POS_RISK,params)

