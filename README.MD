![CI](https://github.com/Nach0t/ActionsTest/actions/workflows/python_test.yml/badge.svg)   /  ![CI](https://github.com/Nach0t/ActionsTest/actions/workflows/flake8.yml/badge.svg)


# Encriptación con AES


## Requisitos:

- Python 3.12
- Terminal

## Cómo ejecutarlo:

### Paso 1: Instalar dependencias

Ejecuta el siguiente comando en la terminal:

```bash
pip install -r requirements.txt
```

### Paso 2: Encriptar un mensaje

Ejecuta el siguiente comando:

```bash
python encriptador.py "Mensaje_a_encriptar" "mi_llave_secreta"
```

- Devuelve en la terminal el mensaje encriptado utilizando la llave de 16 bytes.
- Si la llave tiene menos de 16 bytes, se rellenará automáticamente hasta alcanzar la longitud requerida.
- Si la llave es mayor a 16 bytes, se truncará.
- Guarda el mensaje encriptado y la llave, ya que serán necesarios para desencriptarlo después.

### Paso 3: Desencriptar un mensaje

Ejecuta el siguiente comando:

```bash
python desencriptador.py "Mensaje_encriptado" "mi_llave_secreta"
```

- Devuelve el mensaje desencriptado en la terminal.
- Si el mensaje encriptado es incorrecto o la llave no coincide, se generará un error.

## Cómo realizar pruebas:

### Requisitos:

- Python
- Pytest
- Terminal

### Paso 1: Ejecutar pruebas unitarias

Para probar el encriptador:

```bash
pytest -v test_encriptador.py
```

Para probar el desencriptador:

```bash
pytest -v test_desencriptador.py
```

- Revisa los resultados. Si se detecta un error inesperado, corrige el código y vuelve a ejecutar las pruebas.
