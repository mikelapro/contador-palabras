def contar_palabras(texto):
    """
    Devuelve la cantidad de palabras del `texto` especificado.

    Args:
        texto (string): Texto sobre el cual se deben contar las palabras.

    Returns:
        int: Cantidad de palabras contadas.
    """

    palabras = texto.split()
    return len(palabras)

# TODO: TP Metodologia de Estudio - 04/05/2025.
# Ejemplo de uso.

# Lee el texto de un archivo y lo asigna en una variable.
archivo_io = open("space_x.txt", encoding="utf-8")
TEXTO = archivo_io.read()
archivo_io.close()

cantidad = contar_palabras(TEXTO)
print(f"La cantidad de palabras es: {cantidad}")
