from scapy.all import *

def recibir(packet):
    if Raw in packet:
        print("Payload recibido:", packet[Raw].load)

sniff(prn=recibir, iface="eth0")
