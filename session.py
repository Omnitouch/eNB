def session_dict_initialization(session_dict, plmn, apn, imeisv, e_nas):

    #Examples. Customize at your needs
    NON_IP_PACKET_1 = '0102030405060708090a'
    NON_IP_PACKET_2 = '0102030405060708090a0102030405060708090a'
    NON_IP_PACKET_3 = '0102030405060708090a0102030405060708090a0102030405060708090a'
    NON_IP_PACKET_4 = '0102030405060708090a0102030405060708090a0102030405060708090a0102030405060708090a'


    session_dict['STATE'] = 0
    session_dict['ENB-UE-S1AP-ID'] = 1000
    session_dict['ENB-NAME'] = 'Fabricio-eNB'
    session_dict['ENB-PLMN'] = plmn
    session_dict['XRES'] = b'xresxres'

    session_dict['KASME'] = b'kasme   kasme   kasme   kasme   '
    # hex: 6b61736d652020206b61736d652020206b61736d652020206b61736d65202020
 
    session_dict['ENB-GTP-ADDRESS-INT'] = ''
    
    session_dict['RAB-ID'] = []
    session_dict['SGW-GTP-ADDRESS'] = []
    session_dict['SGW-TEID'] = []
    
    session_dict['EPS-BEARER-IDENTITY'] = []
    session_dict['EPS-BEARER-TYPE'] = []  # default 0, dedicated 1
    session_dict['EPS-BEARER-STATE']  = [] # active 1, inactive 0
    session_dict['EPS-BEARER-APN'] = []
    session_dict['PDN-ADDRESS'] = []

    session_dict['PDN-ADDRESS-IPV4'] = None
    session_dict['PDN-ADDRESS-IPV6'] = None
    
    session_dict['ENB-TAC1'] = b'\x00\x01'
    session_dict['ENB-TAC2'] = b'\x00\x03'
    session_dict['ENB-TAC'] = session_dict['ENB-TAC1']
    session_dict['ENB-TAC-NBIOT'] = b'\x00\x02'     
    session_dict['ENB-ID'] = 1
    session_dict['ENB-CELLID'] = 1000000
    
    session_dict['UP-COUNT'] = -1    
    session_dict['DOWN-COUNT'] = -1
  
    session_dict['ENC-ALG'] = 0
    session_dict['INT-ALG'] = 0 
    session_dict['ENC-KEY'] = None
    session_dict['INT-KEY'] = None  
    session_dict['APN'] = apn
    
    
    session_dict['NAS-SMS-MT'] = None
    
    if session_dict['LOCAL_KEYS'] == True:
        if session_dict['IMSI'] == None:
            session_dict['IMSI'] = IMSI
        
    else:
        if session_dict['IMSI'] == None:
            try:
                session_dict['IMSI'] = return_imsi(session_dict['SERIAL-INTERFACE'])
                if session_dict['IMSI'] == None:
                    session_dict['LOCAL_KEYS'] = True
                    session_dict['IMSI'] = IMSI                
            except:
                if session_dict['LOCAL_MILENAGE'] == False:
                    session_dict['LOCAL_KEYS'] = True
                session_dict['IMSI'] = IMSI
        
    if session_dict['IMEISV'] == None:
        session_dict['IMEISV'] = imeisv
    
    session_dict['ENCODED-IMSI'] = e_nas.encode_imsi(session_dict['IMSI'])
    session_dict['ENCODED-IMEI'] = e_nas.encode_imei(imeisv)
    session_dict['ENCODED-GUTI'] = e_nas.encode_guti(int(session_dict['PLMN']),32769,1,12345678)
    
    session_dict['S-TMSI'] = None
    
    session_dict['TMSI'] = None
    session_dict['LAI'] = None
    
    session_dict['CPSR-TYPE'] = 0
    
    session_dict['S1-TYPE'] = "4G"
    session_dict['MOBILE-IDENTITY'] = session_dict['ENCODED-IMSI'] 
    session_dict['MOBILE-IDENTITY-TYPE'] = "IMSI" 
    session_dict['SESSION-SESSION-TYPE'] = "NONE"
    session_dict['SESSION-TYPE'] = "4G"
    session_dict['SESSION-TYPE-TUN'] = 1
    session_dict['PDP-TYPE'] = 1
    session_dict['ATTACH-PDN'] = None
    session_dict['ATTACH-TYPE'] = 1
    session_dict['TAU-TYPE'] = 0
    session_dict['SMS-UPDATE-TYPE'] = False
    session_dict['NBIOT-SESSION-TYPE'] = "NONE"
    session_dict['CPSR-TYPE'] = 0

    session_dict['UECONTEXTRELEASE-CSFB'] = False
    
    session_dict['PROCESS-PAGING'] = True
    session_dict['PCSCF-RESTORATION'] = False

    session_dict['NAS-KEY-SET-IDENTIFIER'] = 0
    
    session_dict['LOG'] = []
    
    session_dict['NON-IP-PACKET'] = 1
    session_dict['NON-IP-PACKETS'] = [NON_IP_PACKET_1, NON_IP_PACKET_2, NON_IP_PACKET_3, NON_IP_PACKET_4]

    return session_dict

