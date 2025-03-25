import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend


def desencriptar(mensaje_encriptado: bytes, llave: str) -> str:
    """Desencripta un mensaje usando AES en modo CBC con relleno PKCS7.

    Args:
        mensaje_encriptado (bytes): El mensaje encriptado en formato de bytes.
        llave (str): La llave utilizada para la desencriptación
        (se ajustará a 16 bytes si es más corta o se truncará si es más larga).

    Returns:
        str: El mensaje desencriptado en formato de texto.
    """
    # Ajustar la llave a exactamente 16 bytes (rellenando con \0 si es necesario)
    llave = llave.encode().ljust(16, b"\0")[:16]

    iv = b"a" * 16  # Vector de inicialización fijo (NO recomendado para producción)

    cipher = Cipher(algorithms.AES(llave), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    mensaje_rellenado = decryptor.update(mensaje_encriptado) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    mensaje = unpadder.update(mensaje_rellenado) + unpadder.finalize()
    return mensaje.decode()


if __name__ == "__main__":
    """Ejecuta el script desde la terminal"""

    if len(sys.argv) != 3:
        print("Uso: python desencriptador.py <mensaje_encriptado> <llave>")
        sys.exit(1)

    mensaje_encriptado = bytes.fromhex(sys.argv[1])
    llave = sys.argv[2]

    try:
        mensaje_desencriptado = desencriptar(mensaje_encriptado, llave)
        print("Texto Desencriptado:", mensaje_desencriptado)
    except Exception as e:
        print("Error al desencriptar:", str(e))
        sys.exit(1)
