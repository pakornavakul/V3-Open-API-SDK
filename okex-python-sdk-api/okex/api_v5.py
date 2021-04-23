from .client import Client
from .consts import *
from .constv5 import *


class RestAPIV5(Client):

    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, test=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, test, first)


    def get_account_position_risk(self,instType=None):
        # return self._request_without_params(GET, SPOT_ACCOUNT_INFO)
        '''
        :param instType:
        :return: reponse['data'][0]  has 3 keys "AdjEq","balData","posData"
            inside bal and pos
            eq is the amount (size)
            disEq is supposedly discount equity in USD?

        e.g
            'ccy': 'USDT',
            'instId': 'THETA-USDT-SWAP',
            'instType': 'SWAP',
            'mgnMode': 'cross',
            'notionalCcy': '120', Quantity of positions coin
            'notionalUsd': '1413.157469076541602', 	Quantity of positions usd
            'pos': '-12', Number of contracts (-) is short
            'posCcy': '', Position currency, only applicable to MARGIN positions.
            'posId': '297688116329086977',
            'posSide': 'short'}
        '''
        if instType is None:
            return self._request_without_params(GET, ACCOUNT_POS_RISK)
        else:
            params = {}
            params['instType'] = instType
            return self._request_with_params(GET, ACCOUNT_POS_RISK,params)

    def get_account_balance(self,instrument_name_str:str=""):
        # return self._request_without_params(GET, SPOT_ACCOUNT_INFO)
        if instrument_name_str == "":
            '''
            This guys returns
            "data": [{
            "uTime": "1614846244194",
            "totalEq": "91884.8502560037982063",
            "adjEq": "91884.8502560037982063",
            "isoEq": "0",
            "ordFroz": "0",
            "imr": "0",
            "mmr": "0",
            "mgnRatio": "100000",
            "details": [{'availBal': '',
                         'availEq': '1494.2351002724993685',
                         'cashBal': '3455.965925386858', Cash Balance
                         'ccy': 'USDT', 
                         'crossLiab': '0',
                         'disEq': '3464.3631841988994745',
                         'eq': '3460.5565719697327685',
                         'frozenBal': '1966.3214716972334', 
                         'interest': '0',
                         'isoEq': '0',
                         'isoLiab': '0',
                         'liab': '0',
                         'mgnRatio': '',
                         'ordFrozen': '0',
                         'uTime': '1618819207687',
                         'upl': '4.5906465828747685',
                         'uplLiab': '0'},
                        {'availBal': '',
                         'availEq': '199.88',
                         'cashBal': '199.88', Cash Balance, because the amount you have
                         'ccy': 'OMG', 
                         'crossLiab': '0', Cross Liabilities of the currency
                         'disEq': '1351.108848', discount equity of the currency in USD level. 
                         'eq': '199.88', Equity of the currency
                         'frozenBal': '0', 	Frozen balance of the currency
                         'interest': '0', Interest of the currency
                         'isoEq': '0', 
                         'isoLiab': '0', Isolated Liabilities of the currency
                         'liab': '0',
                         'mgnRatio': '',
                         'ordFrozen': '0', Margin frozen for open orders
                         'uTime': '1617246583906', 
                         'upl': '0',
                         'uplLiab': '0'},
                        {'availBal': '',
                         'availEq': '9.994',
                         'cashBal': '9.994',
                         'ccy': 'FIL',
                         'crossLiab': '0',
                         'disEq': '1346.1698132',
                         'eq': '9.994',
                         'frozenBal': '0',
                         'interest': '0',
                         'isoEq': '0',
                         'isoLiab': '0',
                         'liab': '0',
                         'mgnRatio': '',
                         'ordFrozen': '0',
                         'uTime': '1617344750004',
                         'upl': '0',
                         'uplLiab': '0'},
                        {'availBal': '',
                         'availEq': '97.9412',
                         'cashBal': '97.9412',
                         'ccy': 'LUNA',
                         'crossLiab': '0',
                         'disEq': '0',
                         'eq': '97.9412',
                         'frozenBal': '0',
                         'interest': '0',
                         'isoEq': '0',
                         'isoLiab': '0',
                         'liab': '0',
                         'mgnRatio': '',
                         'ordFrozen': '0',
                         'uTime': '1618458097719',
                         'upl': '0',
                         'uplLiab': '0'} 
            
            
            ]
            '''
            return self._request_without_params(GET, ACCOUNT_BALANCE)
        else:
            params = {}
            params['ccy'] = instrument_name_str
            return self._request_with_params(GET, ACCOUNT_BALANCE,params)


    def get_positions(self,instrument_name_str:str=""):
        # return self._request_without_params(GET, SPOT_ACCOUNT_INFO)
        if instrument_name_str == "":
            return self._request_without_params(GET, ACCOUNT_POSITION)
        else:
            params = {}
            params['instId'] = instrument_name_str
            return self._request_with_params(GET, ACCOUNT_POSITION, params)

    '''
    get bill detail? do I need this?
    Retrieve the bills of the account. The bill refers to all transaction records that result in changing
     the balance of an account. Pagination is supported, and the response is sorted with the most 
     recent first. This endpoint can retrieve data from the last 7 days. OH can do fundingrate record
    '''
    def get_billing_detail_7days(self,instType:str="",ccy:str="",mgnMode:str="",ctType:str="",
                                 type:str="",subType:str="",after:str="",before:str="",limit:str="100"):

        params ={}
        if instType != "":
            params['instType'] =instType
        if ccy != "":
            params['ccy'] =ccy
        if mgnMode != "":
            params['mgnMode'] =mgnMode
        if ctType != "":
            params['ctType'] =ctType
        if type != "":
            params['type'] =type
        if subType != "":
            params['subType'] =subType
        if after != "":
            params['after'] =after
        if before != "":
            params['before'] =before
        if limit != "":
            params['limit'] =limit

        if len(params)>0:
            return self._request_with_params(GET, ACCOUNT_BILLS, params)
        else:
        # pass
            return self._request_without_params(GET, ACCOUNT_BILLS)

    def get_billing_detail_3M(self,instType:str="",ccy:str="",mgnMode:str="",ctType:str="",
                                 type:str="",subType:str="",after:str="",before:str="",limit:str="100"):

        params ={}
        if instType != "":
            params['instType'] =instType
        if ccy != "":
            params['ccy'] =ccy
        if mgnMode != "":
            params['mgnMode'] =mgnMode
        if ctType != "":
            params['ctType'] =ctType
        if type != "":
            params['type'] =type
        if subType != "":
            params['subType'] =subType
        if after != "":
            params['after'] =after
        if before != "":
            params['before'] =before
        if limit != "":
            params['limit'] =limit

        if len(params)>0:
            return self._request_with_params(GET, ACCOUNT_BILLS_3M, params)
        else:
        # pass
            return self._request_without_params(GET, ACCOUNT_BILLS_3M)

    def get_server_time(self):
            return self._request_without_params(GET, SERVER_TIMESTAMP_URL)


    def place_order(self,instId:str,tdMode:str,side:str,posSide:str,ordType:str,sz:str,px:str="",ccy:str="",
                    clOrdId:str="",tag:str="",reduceOnly:str=False):


        params ={}

        params['instId']=instId
        params['tdMode']=tdMode
        params['side']=side
        params['posSide']=posSide
        params['ordType']=ordType
        params['sz']=sz
        if px !="":
            params['px']=px
        if ccy !="":
            params['ccy']=ccy
        if clOrdId !="":
            params['clOrdId']=clOrdId
        if tag !="":
            params['tag']=tag

        params['reduceOnly']=reduceOnly


        return self._request_with_params(POST, PLACE_ORDER, params)

    def place_batch_order(self, instId: str, tdMode: str, side: str, posSide: str, ordType: str, sz: str, px: str = "",
                    ccy: str = "",
                    clOrdId: str = "", tag: str = "", reduceOnly:str=False):
        pass
        # params = {}
        #
        # params['instId'] = instId
        # params['tdMode'] = tdMode
        # params['side'] = side
        # params['posSide'] = posSide
        # params['ordType'] = ordType
        # params['sz'] = sz
        # if px != "":
        #     params['px'] = px
        # if ccy != "":
        #     params['ccy'] = ccy
        # if clOrdId != "":
        #     params['clOrdId'] = clOrdId
        # if tag != "":
        #     params['tag'] = tag
        # if reduceOnly != "":
        #     params['reduceOnly'] = reduceOnly
        #
        # return self._request_with_params(POST, PLACE_ORDER, params)

    # @staticmethod
    # def create_placeorder_dict

    def cancel_order(self,instId:str,ordId:str="",clOrdId:str=""):
        params ={}

        params['instId']=instId
        if ordId !="":
            params['ordId']=ordId
        if clOrdId !="":
            params['clOrdId']=clOrdId


        return self._request_with_params(POST, CANCEL_ORDER, params)

    def cancel_multiple_orders(self,list_of_dictionary):
        return self._request_with_params(POST, CANCEL_BATCH_ORDER, list_of_dictionary)


    def amend_order(self,instId:str,cxlOnFail:bool=False,ordId:str="",clOrdId:str="",reqId:str="",
                    newSz:str="",newPx:str=""):

        params ={}
        params['instId'] =instId
        params['cxlOnFail']=cxlOnFail
        if ordId !="":
            params['ordId']=ordId
        if clOrdId !="":
            params['clOrdId']=clOrdId
        if reqId !="":
            params['reqId']=reqId
        if newSz !="":
            params['newSz']=newSz
        if newPx !="":
            params['newPx']=newPx

        return self._request_with_params(POST, AMEND_ORDER, params)


    def close_positions(self,instId:str,posSide:str="",mgnMode:str="",ccy:str=""):

        '''
        Closes all specified instrument's orders via market order...
        So I cannot close specific amount...?
        :param instId:
        :param posSide:
        :param mgnMode:
        :param ccy:
        :return:
        '''
        params ={}
        params['instId'] =instId
        if posSide !="":
            params['posSide'] =posSide
        if mgnMode !="":
            params['mgnMode'] =mgnMode
        if ccy !="":
            params['ccy'] =ccy
        pass


        return self._request_with_params(POST, CLOSE_ALL_POSITION, params)


    def get_order_list(self,instType:str="",uly:str="",instId:str="",ordType:str="",state:str="",
                       after:str="",before:str="",limit:str=""):
        params ={}

        if instType !="":
            params['instType'] =instType
        if instId !="":
            params['instId'] =instId
        if uly !="":
            params['uly'] =uly
        if ordType !="":
            params['ordType'] =ordType
        if state !="":
            params['state'] =state
        if after !="":
            params['after'] =after
        if before !="":
            params['before'] =before
        if limit !="":
            params['limit'] =limit

        if len(params)>0:
            return self._request_with_params(GET, LIST_ORDER, params)
        else:
            return self._request_without_params(GET, LIST_ORDER)

    def get_system_status(self):
        return self._request_without_params(GET, SERVER_STATUS_URL)

    def get_instruments(self,instType:str,uly:str="",instId:str=""):

        params = {}
        params['instType'] = instType
        if uly != "":
            params['uly'] = uly
        if instId != "":
            params["instId"] = instId
        return self._request_with_params(GET, GET_INSTRUMENTS, params)

    def get_funding_rate(self,instId:str):

        params = {}
        params["instId"] = instId
        return self._request_with_params(GET, GET_FUNDINGRATE, params)



