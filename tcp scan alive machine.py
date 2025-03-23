import time
from scapy.all import *
from random import randint

def main():
    ip="192.168.212.129"
    dport = randint(1, 65535)

    packet = IP(dst=ip) / TCP(flags="A", dport=dport)
    response = sr1(packet, timeout=1.0, verbose=0)
    if response:
        # RST标志位
        if int(response[TCP].flags) == 4:
            time.sleep(0.5)
            print(ip + 'is up')
        else:
            print(ip + 'is down')
if __name__ == '__main__':
    main()
