from scapy.all import *
from Crypto.Cipher import DES3
import base64

# ---------------------------
#  CIFRADO CESAR
# ---------------------------
def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for c in texto:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            resultado += chr((ord(c) - base + desplazamiento) % 26 + base)
        else:
            resultado += c
    return resultado

# ---------------------------
#  CIFRADO 3DES
# ---------------------------
def cifrar_3des(mensaje, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    padded = mensaje + (8 - len(mensaje) % 8) * " "
    encrypted = cipher.encrypt(padded.encode())
    return base64.b64encode(encrypted).decode()

# ---------------------------
# ENVIAR PAQUETES L2
# ---------------------------

dest_mac = "AA:BB:CC:DD:EE:FF"  # PON LA MAC DE Ubuntu2 !!
iface = "eth0"  # UTM normalmente usa enp0s3 o eth0 → revisa con: ip a

msg = "hola mundo"
cesar = cifrado_cesar(msg, 3)

key = b"1234567890ABCDEFGHIJ"
tresdes = cifrar_3des(msg, key)

print("César:", cesar)
print("3DES:", tresdes)

# Paquete 1: Cesar
paquete1 = Ether(dst=dest_mac) / Raw(load=cesar.encode())
sendp(paquete1, iface=iface)

# Paquete 2: 3DES
paquete2 = Ether(dst=dest_mac) / Raw(load=tresdes.encode())
sendp(paquete2, iface=iface)

print("Paquetes enviados.")
