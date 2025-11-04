def count_vowels(text):
    """
    Cuenta cuántas veces aparece cada vocal (a, e, i, o, u) en un texto.
    
    Las mayúsculas y minúsculas se tratan como iguales.
    Retorna un diccionario con todas las vocales, incluso si su conteo es 0.
    
    Args:
        text: String a analizar (puede contener cualquier carácter)
    
    Returns:
        Diccionario con formato {'a': int, 'e': int, 'i': int, 'o': int, 'u': int}
    
    Ejemplos:
        >>> count_vowels("Hola")
        {'a': 1, 'e': 0, 'i': 0, 'o': 1, 'u': 0}
        
        >>> count_vowels("Python")
        {'a': 0, 'e': 0, 'i': 0, 'o': 1, 'u': 0}
        
        >>> count_vowels("")
        {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    """
    # TODO: Implementar la solución
    
    # Paso 1: Crear un diccionario con todas las vocales inicializadas en 0
    # Ejemplo: vowel_count = {'a': 0, 'e': 0, ...}
    
    # Paso 2: Recorrer cada carácter del texto
    # Puedes usar: for char in text:
    
    # Paso 3: Convertir el carácter a minúscula para comparación uniforme
    # Usa: char.lower()
    
    # Paso 4: Si el carácter es una vocal, incrementar su contador
    # Verifica si está en el diccionario: if char_lower in vowel_count:
    
    # Paso 5: Retornar el diccionario con los conteos
    
    pass
