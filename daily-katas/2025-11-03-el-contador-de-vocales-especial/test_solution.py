import pytest
from solution import count_vowels


def test_simple_word():
    """Caso básico con una palabra común"""
    result = count_vowels("Hola")
    assert result == {'a': 1, 'e': 0, 'i': 0, 'o': 1, 'u': 0}


def test_phrase_with_spaces():
    """Frase con espacios y mayúsculas mezcladas"""
    result = count_vowels("Hola Mundo")
    assert result == {'a': 1, 'e': 0, 'i': 0, 'o': 2, 'u': 1}


def test_empty_string():
    """String vacío debe retornar todos los conteos en 0"""
    result = count_vowels("")
    assert result == {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}


def test_no_vowels():
    """Texto sin vocales"""
    result = count_vowels("xyz")
    assert result == {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}


def test_only_vowels():
    """Solo vocales en mayúsculas y minúsculas"""
    result = count_vowels("AeIoU")
    assert result == {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}


def test_repeated_vowels():
    """Vocales repetidas"""
    result = count_vowels("aaaaeeee")
    assert result == {'a': 4, 'e': 4, 'i': 0, 'o': 0, 'u': 0}


def test_with_numbers_and_symbols():
    """Texto con números y símbolos"""
    result = count_vowels("Python3.11 es genial!")
    assert result == {'a': 1, 'e': 2, 'i': 1, 'o': 1, 'u': 0}


def test_all_uppercase():
    """Todas las letras en mayúscula"""
    result = count_vowels("PROGRAMMING")
    assert result == {'a': 1, 'e': 0, 'i': 1, 'o': 1, 'u': 0}


def test_all_lowercase():
    """Todas las letras en minúscula"""
    result = count_vowels("programming")
    assert result == {'a': 1, 'e': 0, 'i': 1, 'o': 1, 'u': 0}


def test_mixed_case():
    """Mezcla de mayúsculas y minúsculas"""
    result = count_vowels("PyThOn")
    assert result == {'a': 0, 'e': 0, 'i': 0, 'o': 1, 'u': 0}


def test_special_characters():
    """Caracteres especiales y puntuación"""
    result = count_vowels("¡Hola! ¿Cómo estás?")
    # Nota: las tildes NO se cuentan en esta versión
    assert result == {'a': 1, 'e': 1, 'i': 0, 'o': 2, 'u': 0}


def test_numbers_only():
    """Solo números"""
    result = count_vowels("123456789")
    assert result == {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}


def test_single_character_vowel():
    """Un solo carácter que es vocal"""
    result = count_vowels("a")
    assert result == {'a': 1, 'e': 0, 'i': 0, 'o': 0, 'u': 0}


def test_single_character_consonant():
    """Un solo carácter que es consonante"""
    result = count_vowels("b")
    assert result == {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}


def test_long_text():
    """Texto más largo para verificar que funciona correctamente"""
    text = "La programación es una habilidad esencial en el mundo moderno"
    result = count_vowels(text)
    assert result == {'a': 8, 'e': 5, 'i': 5, 'o': 4, 'u': 2}


def test_return_type():
    """Verificar que el retorno es un diccionario"""
    result = count_vowels("test")
    assert isinstance(result, dict)


def test_all_keys_present():
    """Verificar que todas las vocales están presentes como claves"""
    result = count_vowels("xyz")
    assert set(result.keys()) == {'a', 'e', 'i', 'o', 'u'}


def test_performance_large_input():
    """Test de rendimiento con entrada grande"""
    import time
    
    # Crear un texto de ~10,000 caracteres
    large_text = "Esta es una prueba de rendimiento. " * 250
    
    start = time.time()
    result = count_vowels(large_text)
    elapsed = time.time() - start
    
    # Debe completarse en menos de 0.1 segundos
    assert elapsed < 0.1
    # Verificar que el resultado tiene sentido
    assert isinstance(result, dict)
    assert len(result) == 5


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
