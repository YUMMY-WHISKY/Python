from scapy.all import *

def main():
    #所有重要数据都在ans里
    ans,uans = sr(IP(dst="192.168.80.129")/ICMP())
    for snd,rcv in ans:
        print(rcv.sprintf("%IP.src% is alive now"))