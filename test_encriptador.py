import encriptador


def test_encriptar_mensaje_simple():
    # Prueba la encriptación de un mensaje simple
    mensaje = "Hola"
    llave = "mi_clave_secerta"
    mensaje_encriptado = encriptador.encriptar(mensaje, llave)
    assert mensaje_encriptado != mensaje.encode()


def test_encriptar_mensaje_complejo():
    # Prueba la encriptación de un mensaje más largo con caracteres especiales
    mensaje = "Este es un mensaje más largo con caracteres especiales @#¢∞¬"
    llave = "una llave diferente"
    mensaje_encriptado = encriptador.encriptar(mensaje, llave)
    assert mensaje_encriptado != mensaje.encode()


def test_encriptar_mensaje_2():
    # Prueba la encriptación de un mensaje con caracteres especiales y espacios
    mensaje = "/SY hdgs [] -- Ñ @#¢∞¬"
    llave = "una llave diferente"
    mensaje_encriptado = encriptador.encriptar(mensaje, llave)
    assert mensaje_encriptado != mensaje.encode()
