from scapy.all import *

iface = "enp0s1"

def handle(pkt):
    print(pkt.summary())
    if Raw in pkt:
        print("Payload:", pkt[Raw].load)

sniff(iface=iface, prn=handle)
