import okex.api_v5 as OKEx5
import json,os,configparser
import datetime

def get_timestamp():
    now = datetime.datetime.now()
    t = now.isoformat("T", "milliseconds")
    return t + "Z"

time = get_timestamp()



appconfig_path = os.getcwd().split('\\')[0] + "\\" + os.getcwd().split('\\')[1]
AppConfig = configparser.ConfigParser()
AppConfig.read(os.path.join(appconfig_path,"AppConfig.ini"))


if __name__ == '__main__':

    api_key = AppConfig["OKEx"]["api_key_v5_main"]
    secret_key = AppConfig["OKEx"]["api_secret_v5_main"]
    passphrase = "00145216"


    OKEx5_API = OKEx5.RestAPIV5(api_key, secret_key, passphrase, False)

    # response = OKEx5_API.get_positions(instrument_name_str="FIL-USDT-SWAP,LUNA-USDT-SWAP")
    response = OKEx5_API.get_billing_detail_7days(instType="SWAP",type="8")
    # response = OKEx5_API.get_billing_detail_7days()
    print(response)
    print()