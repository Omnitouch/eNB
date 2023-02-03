import argparse
import subprocess
from binascii import unhexlify
import toml

# todo move to more appropriate location
def config_load(filename):
    config = toml.load(filename)
    return config

def parse_cla():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', dest='config_file', type=str, required=True, help='A TOML config file to load')
    args = parser.parse_args()

    return args

def get_session_dict_items_from_config(config_dict):
    cla_session_dict_items = {}

    # Get items needed from dict
    enb_ip             = config_dict.get('enb_ip', None)
    mme_ip             = config_dict.get('mme_ip', None)
    gateway_ip_address = config_dict.get('gateway_ip_address', None)
    serial_interface   = config_dict.get('serial_interface', None)
    imsi               = config_dict.get('imsi', None)
    imei               = config_dict.get('imei', None)
    ki                 = config_dict.get('ki', None)
    op                 = config_dict.get('op', None)
    opc                = config_dict.get('opc', None)
    plmn               = config_dict.get('plmn', None)

    if mme_ip is None:
        print('MME IP Required. Exiting.')
        exit(1)
    if enb_ip is None:
        print('eNB Local IP Required! Exiting.')
        exit(1)
    if gateway_ip_address is not None:
        subprocess.call("route add " + mme_ip + "/32 gw " + gateway_ip_address, shell=True)
        cla_session_dict_items['GATEWAY'] = gateway_ip_address
    else:
        cla_session_dict_items['GATEWAY'] = None    
        
    if serial_interface is None:
        cla_session_dict_items['LOCAL_KEYS'] = True
    else:
        cla_session_dict_items['LOCAL_KEYS'] = False
        cla_session_dict_items['SERIAL-INTERFACE'] = serial_interface
        cla_session_dict_items['LOCAL_MILENAGE'] = False

    if imsi is None:
        cla_session_dict_items['IMSI'] = None
    else:
        cla_session_dict_items['IMSI'] = imsi

    if imei is None:
        cla_session_dict_items['IMEISV'] = None
    else:
        cla_session_dict_items['IMEISV'] = imei

    if ki is not None and (op is not None or opc is not None):
        cla_session_dict_items['LOCAL_KEYS'] = False
        cla_session_dict_items['LOCAL_MILENAGE'] = True
        cla_session_dict_items['KI'] = unhexlify(ki)
        if op is not None:
            cla_session_dict_items['OP'] = unhexlify(op)
            cla_session_dict_items['OPC'] = None
        elif opc is not None:
            cla_session_dict_items['OPC'] = unhexlify(opc)
            cla_session_dict_items['OP'] = None
    else:
        cla_session_dict_items['LOCAL_MILENAGE'] = False

    if plmn is not None:
        cla_session_dict_items['PLMN'] = plmn
    else:
        cla_session_dict_items['PLMN'] = PLMN

    return cla_session_dict_items