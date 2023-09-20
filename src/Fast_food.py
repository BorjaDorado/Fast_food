import re


def limpiar_texto(texto):
    # Eliminar caracteres especiales y espacios innecesarios
    texto_limpio = re.sub(r"[^a-zA-Z0-9\s]", "", texto)
    texto_limpio = re.sub(r"\s+", " ", texto_limpio).strip()

    # Escapar comillas simples
    texto_limpio = re.sub(r"'", "''", texto_limpio)

    return texto_limpio