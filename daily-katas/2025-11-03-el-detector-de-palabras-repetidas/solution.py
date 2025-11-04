def find_repeated_words(text):
    """
    Encuentra palabras que aparecen más de una vez en un texto.
    
    Las mayúsculas y minúsculas se tratan como iguales.
    Solo retorna palabras que aparecen 2 o más veces.
    
    Args:
        text: String con palabras separadas por espacios
    
    Returns:
        Diccionario con palabras repetidas y su conteo
        Solo incluye palabras con conteo >= 2
        Si no hay repeticiones, retorna {}
    
    Ejemplos:
        >>> find_repeated_words("hola mundo hola")
        {'hola': 2}
        
        >>> find_repeated_words("cada palabra es unica")
        {}
        
        >>> find_repeated_words("Python python PYTHON")
        {'python': 3}
    """
    # TODO: Implementar la solución
    
    # Paso 1: Dividir el texto en palabras
    # Usa: text.split() que divide por espacios
    
    # Paso 2: Crear un diccionario para contar palabras
    # Similar al ejercicio anterior: word_count = {}
    
    # Paso 3: Recorrer cada palabra
    # for word in words:
    
    # Paso 4: Normalizar la palabra a minúsculas
    # word_lower = word.lower()
    
    # Paso 5: Contar la palabra en el diccionario
    # Opción A: if word_lower in word_count: word_count[word_lower] += 1 else: word_count[word_lower] = 1
    # Opción B: word_count[word_lower] = word_count.get(word_lower, 0) + 1
    
    # Paso 6: Filtrar solo las palabras con conteo >= 2
    # Opción A: Crear un nuevo diccionario con un loop
    # Opción B: Usar comprensión de diccionarios
    # repeated = {word: count for word, count in word_count.items() if count >= 2}
    
    # Paso 7: Retornar el diccionario filtrado
    
    pass


# OPCIONAL: Si quieres intentar la versión avanzada que limpia puntuación
def find_repeated_words_clean(text):
    """
    Versión avanzada que limpia signos de puntuación.
    
    Ejemplo: "hola!" y "hola" se consideran la misma palabra.
    """
    # TODO: Implementar limpieza de puntuación
    # Pista: Puedes usar word.strip('.,!?;:') o el módulo string
    
    pass