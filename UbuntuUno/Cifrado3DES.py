import subprocess
import base64

def cifrar_3des_openssl(texto, key):
    # Guardar mensaje en archivo temporal
    with open("msg.txt", "w") as f:
        f.write(texto)

    # Ejecutar openssl 3DES en modo ECB
    subprocess.run([
        "openssl", "enc", "-des-ede3", "-in", "msg.txt",
        "-out", "msg.enc", "-K", key
    ])

    # Leer archivo cifrado y convertirlo a base64 para enviarlo fácil
    with open("msg.enc", "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# USO:
key = "0123456789ABCDEFFEDCBA9876543210"  # 24 bytes (48 hex chars)
mensaje = "hola mundo"

cifrado = cifrar_3des_openssl(mensaje, key)
print("Cifrado 3DES:", cifrado)
