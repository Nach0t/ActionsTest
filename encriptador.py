import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend


def procesar_llave(llave: str) -> bytes:
    llave_bytes = llave.encode()
    if len(llave_bytes) < 16:
        # Completa con ceros hasta 16 bytes
        llave_bytes = llave_bytes.ljust(16, b"\0")
    else:
        # Si es mayor, se trunca a 16 bytes
        llave_bytes = llave_bytes[:16]
    return llave_bytes


def encriptar(mensaje: str, llave: str) -> bytes:
    """Encripta un mensaje usando AES en modo CBC con una llave de 16 bytes.

    Args:
        mensaje (str): El mensaje a encriptar.
        llave (str): La llave utilizada para la encriptación.
                     Se completará o truncará para que tenga 16 bytes.

    Returns:
        bytes: El mensaje encriptado en formato de bytes.
    """
    llave = procesar_llave(llave)
    iv = b"a" * 16  # Vector de inicialización fijo (no recomendado para producción)

    cipher = Cipher(algorithms.AES(llave), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    mensaje_rellenado = padder.update(mensaje.encode()) + padder.finalize()

    mensaje_encriptado = encryptor.update(mensaje_rellenado) + encryptor.finalize()
    return mensaje_encriptado


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python encriptador.py <mensaje> <llave>")
        sys.exit(1)

    mensaje = sys.argv[1]
    llave = sys.argv[2]

    mensaje_encriptado = encriptar(mensaje, llave)
    print("Texto Encriptado:", mensaje_encriptado.hex())
