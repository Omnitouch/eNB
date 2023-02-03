from optparse import OptionParser
import subprocess
from binascii import unhexlify

def parse_cla():
    parser = OptionParser()    
    parser.add_option("-i", "--ip", dest="eNB_ip", help="eNB Local IP Address")
    parser.add_option("-m", "--mme", dest="mme_ip", help="MME IP Address")
    parser.add_option("-g", "--gateway_ip_address", dest="gateway_ip_address", help="gateway IP address") 
    parser.add_option("-u", "--usb_device", dest="serial_interface", help="modem port (i.e. COMX, or /dev/ttyUSBX), smartcard reader index (0, 1, 2, ...), or server for https")     
    parser.add_option("-I", "--imsi", dest="imsi", help="IMSI (15 digits)")
    parser.add_option("-E", "--imei", dest="imei", help="IMEI-SV (16 digits)")    
    parser.add_option("-K", "--ki", dest="ki", help="ki for Milenage (if not using option -u)")    
    parser.add_option("-P", "--op", dest="op", help="op for Milenage (if not using option -u)")    
    parser.add_option("-C", "--opc", dest="opc", help="opc for Milenage (if not using option -u)")    
    parser.add_option("-o", "--operator", dest="plmn", help="Operator MCC+MNC")
    parser.add_option("-a", "--auto_call", dest="auto_call", help="Menu items in array such as ")

    (options, _args) = parser.parse_args()

    # Perform some extra parsing for the auto_call list
    if options.auto_call is not None:
        options.auto_call = options.auto_call.split(',')
    else:
        options.auto_call = []

    return options

def get_session_dict_items_from_cla(options):

    cla_session_dict_items = {}

    if options.mme_ip is None:
        print('MME IP Required. Exiting.')
        exit(1)
    if options.eNB_ip is None:
        print('eNB Local IP Required! Exiting.')
        exit(1)
    if options.gateway_ip_address is not None:
        subprocess.call("route add " + options.mme_ip + "/32 gw " + options.gateway_ip_address, shell=True)
        cla_session_dict_items['GATEWAY'] = options.gateway_ip_address
    else:
        cla_session_dict_items['GATEWAY'] = None    
        
    if options.serial_interface is None:
        cla_session_dict_items['LOCAL_KEYS'] = True
    else:
        cla_session_dict_items['LOCAL_KEYS'] = False
        cla_session_dict_items['SERIAL-INTERFACE'] = options.serial_interface
        cla_session_dict_items['LOCAL_MILENAGE'] = False

    if options.imsi is None:
        cla_session_dict_items['IMSI'] = None
    else:
        cla_session_dict_items['IMSI'] = options.imsi

    if options.imei is None:
        cla_session_dict_items['IMEISV'] = None
    else:
        cla_session_dict_items['IMEISV'] = options.imei

    if options.ki is not None and (options.op is not None or options.opc is not None):
        cla_session_dict_items['LOCAL_KEYS'] = False
        cla_session_dict_items['LOCAL_MILENAGE'] = True
        cla_session_dict_items['KI'] = unhexlify(options.ki)
        if options.op is not None:
            cla_session_dict_items['OP'] = unhexlify(options.op)
            cla_session_dict_items['OPC'] = None
        elif options.opc is not None:
            cla_session_dict_items['OPC'] = unhexlify(options.opc)
            cla_session_dict_items['OP'] = None
    else:
        cla_session_dict_items['LOCAL_MILENAGE'] = False

    if options.plmn is not None:
        cla_session_dict_items['PLMN'] = options.plmn
    else:
        cla_session_dict_items['PLMN'] = PLMN

    return cla_session_dict_items