import pytest
from solution import decode_alien_dna


def test_simple_two_ways():
    """Caso básico con dos formas de decodificar"""
    assert decode_alien_dna("12") == 2
    # Puede ser: "AB" (1-2) o "L" (12)


def test_three_ways_with_26():
    """Secuencia que incluye el número 26 (Z)"""
    assert decode_alien_dna("226") == 3
    # Puede ser: "BBF" (2-2-6), "BZ" (2-26), "VF" (22-6)


def test_single_digit():
    """Un solo dígito tiene una sola forma"""
    assert decode_alien_dna("5") == 1
    assert decode_alien_dna("9") == 1


def test_invalid_starting_with_zero():
    """Secuencias que comienzan con 0 son inválidas"""
    assert decode_alien_dna("0") == 0
    assert decode_alien_dna("01") == 0


def test_valid_with_ten():
    """El número 10 es válido (representa J)"""
    assert decode_alien_dna("10") == 1
    # Solo puede ser "J" (10)


def test_valid_with_twenty():
    """El número 20 es válido (representa T)"""
    assert decode_alien_dna("20") == 1
    # Solo puede ser "T" (20)


def test_multiple_tens():
    """Secuencia con múltiples números terminados en 0"""
    assert decode_alien_dna("110") == 1
    # Solo puede ser "AJ" (1-10), no "KJ" porque 0 no puede estar solo


def test_invalid_double_zero():
    """Doble cero es inválido"""
    assert decode_alien_dna("100") == 0
    assert decode_alien_dna("1001") == 0


def test_invalid_number_above_26():
    """Números mayores a 26 limitan las opciones"""
    assert decode_alien_dna("27") == 1
    # Solo puede ser "BG" (2-7), no puede ser 27
    assert decode_alien_dna("301") == 0
    # El 30 no es válido, y 0 no puede estar solo


def test_complex_sequence():
    """Secuencia más compleja con múltiples opciones"""
    assert decode_alien_dna("111") == 3
    # Puede ser: "AAA" (1-1-1), "KA" (11-1), "AK" (1-11)


def test_long_sequence_fibonacci_pattern():
    """Secuencia larga que sigue patrón de Fibonacci"""
    # "1111" debería tener 5 formas
    assert decode_alien_dna("1111") == 5
    # "11111" debería tener 8 formas
    assert decode_alien_dna("11111") == 8


def test_alternating_valid_pairs():
    """Números que siempre forman pares válidos"""
    assert decode_alien_dna("1212") == 5
    # Múltiples formas de agrupar 1s y 2s


def test_edge_case_all_zeros_after_valid():
    """Ceros después de números que no los soportan"""
    assert decode_alien_dna("30") == 0
    assert decode_alien_dna("40") == 0
    assert decode_alien_dna("130") == 0


def test_valid_sequence_with_embedded_ten():
    """Secuencia válida con 10 en medio"""
    assert decode_alien_dna("1101") == 1
    # Solo puede ser "AJA" (1-10-1)


def test_boundary_numbers():
    """Probar límites: 26 es válido, 27 no"""
    assert decode_alien_dna("26") == 2
    # Puede ser "BF" (2-6) o "Z" (26)
    assert decode_alien_dna("2627") == 2
    # "ZBG" (26-2-7) o "BFBG" (2-6-2-7)


def test_empty_string():
    """String vacío debería retornar 1 (una forma de decodificar nada)"""
    result = decode_alien_dna("")
    # Puede ser 0 o 1 dependiendo de la interpretación
    # Ambos son válidos, pero debe ser consistente
    assert result in [0, 1]


def test_performance_long_sequence():
    """Test de rendimiento con secuencia larga"""
    import time
    
    # Secuencia de 50 caracteres (todos 1s)
    long_sequence = "1" * 50
    
    start = time.time()
    result = decode_alien_dna(long_sequence)
    elapsed = time.time() - start
    
    # Debe completarse en menos de 1 segundo
    assert elapsed < 1.0
    # Debe retornar un número (no importa cuál exactamente para este test)
    assert isinstance(result, int)
    assert result > 0


def test_mixed_valid_invalid_patterns():
    """Combinación de patrones válidos e inválidos"""
    assert decode_alien_dna("1203") == 0
    # El 03 es inválido (0 no puede estar después de números > 2)
    
    assert decode_alien_dna("1210") == 2
    # Puede ser "ABA-J" (1-2-1-0) o "L-J" (12-10)


def test_all_high_numbers():
    """Secuencia con todos los dígitos altos"""
    assert decode_alien_dna("9999") == 1
    # Solo puede ser "IIII" (9-9-9-9)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
