from scapy.all import *
from random import randint

def main():
    ip_id = randint(1,65535)
    icmp_id = randint(1,65535)
    icmp_seq = randint(1,65535)
    package = IP(dst="192.168.80.129",ttl=64,id=ip_id)/ICMP(id=icmp_id,seq=icmp_seq)/b'rootkit'  #ttl叫time to life
    result = sr1(package,timeout=1,verbose=False)
    if result:
        for rcv in result:
            scan_ip = rcv[IP].src
            print(scan_ip+' is alive')
    else:
        print(' is down')