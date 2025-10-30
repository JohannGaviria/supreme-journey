import pytest
from solution import trace_light_beam


def test_simple_reflection_north_exit():
    """Caso básico: una reflexión que sale por el norte"""
    grid = [
        "...",
        "./.",
        "..."
    ]
    result = trace_light_beam(grid, "west", 1)
    assert result["exit_side"] == "north"
    assert result["exit_position"] == 1


def test_straight_path_no_mirrors():
    """El rayo atraviesa sin encontrar espejos"""
    grid = [
        "....",
        "....",
        "...."
    ]
    result = trace_light_beam(grid, "west", 1)
    assert result["exit_side"] == "east"
    assert result["exit_position"] == 1


def test_multiple_reflections():
    """Múltiples reflexiones antes de salir"""
    grid = [
        r"\/",
        r"/\\"
    ]
    result = trace_light_beam(grid, "west", 0)
    # El rayo debería rebotar varias veces y salir
    assert result["exit_side"] in ["north", "south", "east", "west"]
    assert result["exit_position"] is not None


def test_infinite_loop_detection():
    """Detectar cuando el rayo queda atrapado en un bucle"""
    grid = [
        r"\/",
        r"\/"
    ]
    result = trace_light_beam(grid, "west", 0)
    assert result["exit_side"] == "loop"
    assert result["exit_position"] is None


def test_entry_from_north():
    """Entrada desde el norte (arriba)"""
    grid = [
        r"\..",
        "...",
        "..."
    ]
    result = trace_light_beam(grid, "north", 0)
    assert result["exit_side"] == "west"
    assert result["exit_position"] == 0


def test_entry_from_south():
    """Entrada desde el sur (abajo)"""
    grid = [
        "...",
        "...",
        "../"
    ]
    result = trace_light_beam(grid, "south", 2)
    assert result["exit_side"] == "east"
    assert result["exit_position"] == 2


def test_complex_maze():
    """Laberinto más complejo con múltiples espejos"""
    grid = [
        r"..\/.",
        r".\/\.",
        r"./\..",
        r"....\\"
    ]
    result = trace_light_beam(grid, "west", 2)
    # Solo verificamos que no lanza excepciones y retorna formato válido
    assert "exit_side" in result
    assert "exit_position" in result
    if result["exit_side"] != "loop":
        assert isinstance(result["exit_position"], int)


def test_single_cell_mirror():
    """Grid de 1x1 con espejo"""
    grid = ["/"]
    result = trace_light_beam(grid, "west", 0)
    assert result["exit_side"] == "north"
    assert result["exit_position"] == 0


def test_edge_case_large_grid():
    """Test de rendimiento con grid grande (10x10)"""
    import time
    
    # Crear un grid 10x10 con patrón de espejos
    grid = []
    for i in range(10):
        row = ""
        for j in range(10):
            if (i + j) % 3 == 0:
                row += "/"
            elif (i + j) % 3 == 1:
                row += "\\"
            else:
                row += "."
        grid.append(row)
    
    start = time.time()
    result = trace_light_beam(grid, "west", 5)
    elapsed = time.time() - start
    
    # Debe completarse en menos de 1 segundo
    assert elapsed < 1.0
    assert "exit_side" in result
    assert "exit_position" in result


def test_backslash_mirror_reflection():
    """Test específico para espejo \\ (backslash)"""
    grid = [
        r"...",
        r".\.",
        r"..."
    ]
    result = trace_light_beam(grid, "west", 1)
    assert result["exit_side"] == "south"
    assert result["exit_position"] == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
