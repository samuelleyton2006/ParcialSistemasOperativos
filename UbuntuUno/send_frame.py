#!/usr/bin/env python3
from scapy.all import *
import sys
# Interfaz: reemplaza por la que tengas, ej: "enp0s3"
IFACE = "enp0s3"
# MAC destino: puedes usar la MAC de la otra VM o broadcast "ff:ff:ff:ff:ff:ff"
DST_MAC = "aa:bb:cc:dd:ee:02"   # cambia a la MAC real de Ubuntu2 o usa broadcast
SRC_MAC = get_if_hwaddr(IFACE)

# Payload simple
payload = b"Hola desde Ubuntu1 - Frame L2"

eth = Ether(dst=DST_MAC, src=SRC_MAC, type=0x88B5) / Raw(load=payload)
print(f"Enviando frame L2 desde {SRC_MAC} a {DST_MAC} por {IFACE}")
sendp(eth, iface=IFACE, count=10, inter=0.5)  # envia 10 frames, medio segundo entre ellos
