import encriptador
import desencriptador


def test_desencriptar_mensaje_simple():
    # Prueba la desencriptación de un mensaje simple
    mensaje_original = "Hola"
    llave = "mi_llave_secreta"
    mensaje_encriptado = encriptador.encriptar(mensaje_original, llave)
    mensaje_desencriptado = desencriptador.desencriptar(mensaje_encriptado, llave)
    assert mensaje_desencriptado == mensaje_original


def test_desencriptar_mensaje_complejo():
    # Prueba la desencriptación de un mensaje más largo con caracteres especiales
    mensaje_original = "Este es un mensaje más largo con caracteres especiales @#¢∞¬"
    llave = "una llave diferente"
    mensaje_encriptado = encriptador.encriptar(mensaje_original, llave)
    mensaje_desencriptado = desencriptador.desencriptar(mensaje_encriptado, llave)
    assert mensaje_desencriptado == mensaje_original


def test_desencriptar_mensaje_2():
    # Prueba la desencriptación de un mensaje con caracteres especiales y espacios
    mensaje_original = "/SY hdgs [] -- Ñ @#¢∞¬"
    llave = "una llave diferente"
    mensaje_encriptado = encriptador.encriptar(mensaje_original, llave)
    mensaje_desencriptado = desencriptador.desencriptar(mensaje_encriptado, llave)
    assert mensaje_desencriptado == mensaje_original


def test_desencriptar_mensaje_simple():
    mensaje_original = "Hola"
    llave = "mi_llave_secreta"
    mensaje_encriptado = encriptador.encriptar(mensaje_original, llave)
    mensaje_desencriptado = desencriptador.desencriptar(mensaje_encriptado, llave)
    assert mensaje_desencriptado == mensaje_original


def test_desencriptar_mensaje_complejo():
    mensaje_original = "Este es un mensaje más largo con caracteres especiales @#¢∞¬"
    llave = "una llave diferente"
    mensaje_encriptado = encriptador.encriptar(mensaje_original, llave)
    mensaje_desencriptado = desencriptador.desencriptar(mensaje_encriptado, llave)
    assert mensaje_desencriptado == mensaje_original


def test_desencriptar_mensaje_2():
    mensaje_original = "/SY hdgs [] -- Ñ @#¢∞¬"
    llave = "una llave diferente"
    mensaje_encriptado = encriptador.encriptar(mensaje_original, llave)
    mensaje_desencriptado = desencriptador.desencriptar(mensaje_encriptado, llave)
    assert mensaje_desencriptado == mensaje_original
