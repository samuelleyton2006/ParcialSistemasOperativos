from scapy.all import *

iface = "enp0s1"
src = get_if_hwaddr(iface)
dst = "ff:ff:ff:ff:ff:ff"

pkt = Ether(src=src, dst=dst, type=0x1234)/Raw(load=b"Hola desde capa 2!")

sendp(pkt, iface=iface, count=5)
