import pytest
from solution import find_repeated_words


def test_simple_repetition():
    """Caso básico con una palabra repetida dos veces"""
    result = find_repeated_words("hola mundo hola")
    assert result == {'hola': 2}


def test_multiple_repetitions():
    """Múltiples palabras repetidas con diferentes conteos"""
    result = find_repeated_words("esto esto esto es genial genial")
    assert result == {'esto': 3, 'genial': 2}


def test_no_repetitions():
    """Ninguna palabra se repite"""
    result = find_repeated_words("cada palabra es unica")
    assert result == {}


def test_empty_string():
    """String vacío debe retornar diccionario vacío"""
    result = find_repeated_words("")
    assert result == {}


def test_single_word():
    """Una sola palabra no puede repetirse"""
    result = find_repeated_words("hola")
    assert result == {}


def test_case_insensitive():
    """Mayúsculas y minúsculas deben tratarse igual"""
    result = find_repeated_words("Python python PYTHON")
    assert result == {'python': 3}


def test_mixed_case_multiple_words():
    """Varias palabras con mayúsculas mezcladas"""
    result = find_repeated_words("Hola MUNDO hola mundo")
    assert result == {'hola': 2, 'mundo': 2}


def test_all_words_repeated():
    """Todas las palabras están repetidas"""
    result = find_repeated_words("a a b b c c")
    assert result == {'a': 2, 'b': 2, 'c': 2}


def test_one_word_many_times():
    """Una palabra repetida muchas veces"""
    result = find_repeated_words("si si si si si")
    assert result == {'si': 5}


def test_multiple_spaces():
    """Texto con múltiples espacios entre palabras"""
    result = find_repeated_words("hola    hola    mundo")
    assert result == {'hola': 2}


def test_with_numbers():
    """Palabras que son números"""
    result = find_repeated_words("123 456 123")
    assert result == {'123': 2}


def test_alphanumeric_words():
    """Palabras alfanuméricas"""
    result = find_repeated_words("Python3 python3 Java")
    assert result == {'python3': 2}


def test_return_type():
    """Verificar que el retorno es un diccionario"""
    result = find_repeated_words("test test")
    assert isinstance(result, dict)


def test_only_counts_above_one():
    """El diccionario solo debe contener palabras con conteo >= 2"""
    result = find_repeated_words("a a b c c d")
    # 'b' y 'd' aparecen solo 1 vez, no deben estar en el resultado
    assert 'b' not in result
    assert 'd' not in result
    assert result == {'a': 2, 'c': 2}


def test_long_text():
    """Texto más largo con múltiples repeticiones"""
    text = "el perro es el mejor amigo del hombre el perro es leal"
    result = find_repeated_words(text)
    assert result == {'el': 3, 'perro': 2, 'es': 2}


def test_single_letter_words():
    """Palabras de una sola letra"""
    result = find_repeated_words("a b a c b a")
    assert result == {'a': 3, 'b': 2}


def test_with_punctuation_simple():
    """
    Palabras con puntuación (versión simple: NO limpia puntuación)
    Si implementaste limpieza, ajusta este test
    """
    result = find_repeated_words("hola mundo hola")
    assert result == {'hola': 2}


def test_trailing_spaces():
    """Texto con espacios al inicio y final"""
    result = find_repeated_words("  hola mundo hola  ")
    assert result == {'hola': 2}


def test_performance_large_input():
    """Test de rendimiento con muchas palabras"""
    import time
    
    # Crear un texto con ~1000 palabras
    words = ["palabra" + str(i % 50) for i in range(1000)]
    large_text = " ".join(words)
    
    start = time.time()
    result = find_repeated_words(large_text)
    elapsed = time.time() - start
    
    # Debe completarse en menos de 0.1 segundos
    assert elapsed < 0.1
    # Todas las palabras deberían aparecer ~20 veces
    assert len(result) > 0


def test_real_world_sentence():
    """Frase del mundo real"""
    text = "La programación es difícil pero la práctica hace que la programación sea más fácil"
    result = find_repeated_words(text)
    assert result == {'la': 3, 'programación': 2}


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
