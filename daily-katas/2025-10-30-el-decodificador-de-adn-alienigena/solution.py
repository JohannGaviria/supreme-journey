def decode_alien_dna(dna_sequence):
    """
    Cuenta el número de formas diferentes de decodificar una secuencia de ADN alienígena.
    
    El ADN alienígena usa números del 1 al 26 para representar letras A-Z.
    Una secuencia puede decodificarse de múltiples maneras si los números pueden
    agruparse de diferentes formas.
    
    Args:
        dna_sequence: String conteniendo solo dígitos
    
    Returns:
        Entero con el número de decodificaciones posibles (0 si es inválida)
    
    Ejemplos:
        >>> decode_alien_dna("12")
        2
        >>> decode_alien_dna("226")
        3
        >>> decode_alien_dna("0")
        0
        >>> decode_alien_dna("10")
        1
    """
    # TODO: Implementar la solución
    
    # Enfoque sugerido:
    # 1. Validar casos base (string vacío, comienza con 0, etc.)
    # 2. Usar programación dinámica o recursión con memorización
    # 3. Para cada posición, considerar:
    #    - Tomar 1 dígito (si es válido: 1-9)
    #    - Tomar 2 dígitos (si es válido: 10-26)
    # 4. Manejar ceros cuidadosamente (solo válidos en 10, 20)
    
    pass


# Enfoque alternativo con hints más específicos:
def decode_alien_dna_dp(dna_sequence):
    """
    Versión con programación dinámica iterativa (bottom-up).
    
    Idea: dp[i] = número de formas de decodificar dna_sequence[0:i]
    """
    # TODO: Implementar usando DP iterativo
    pass


def decode_alien_dna_memo(dna_sequence):
    """
    Versión con recursión + memorización (top-down).
    
    Idea: Usar un diccionario para cachear resultados de subproblemas.
    """
    # TODO: Implementar usando recursión con memoization
    
    def helper(index, memo):
        # Caso base: llegamos al final
        # Caso recursivo: probar tomar 1 o 2 dígitos
        # Validar que los números estén en rango 1-26
        pass
    
    pass


# Puedes implementar cualquiera de las versiones anteriores
# o crear tu propia solución