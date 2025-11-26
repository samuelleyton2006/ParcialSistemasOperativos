#!/usr/bin/env python3
from scapy.all import *
IFACE = "enp0s3"

def handle(pkt):
    if pkt.haslayer(Raw):
        print("== Frame capturado ==")
        print("Src MAC:", pkt.src)
        print("Dst MAC:", pkt.dst)
        print("EtherType: 0x%04x" % pkt.type)
        try:
            print("Payload:", pkt[Raw].load)
        except Exception as e:
            print("No pudo leer payload:", e)
        print("----------------------\n")

print(f"Escuchando en {IFACE} (Ctrl-C para salir)")
sniff(iface=IFACE, prn=handle, store=0)
