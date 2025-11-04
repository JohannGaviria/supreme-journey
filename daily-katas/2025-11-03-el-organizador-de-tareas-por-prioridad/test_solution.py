import pytest
from solution import organize_tasks


def test_basic_sorting():
    """Caso básico: ordenar por prioridad descendente"""
    tasks = [
        {"title": "Tarea A", "priority": 2, "completed": False},
        {"title": "Tarea B", "priority": 5, "completed": False},
        {"title": "Tarea C", "priority": 3, "completed": False},
    ]
    result = organize_tasks(tasks)
    
    assert len(result) == 3
    assert result[0]["priority"] == 5
    assert result[1]["priority"] == 3
    assert result[2]["priority"] == 2


def test_filter_completed():
    """Debe filtrar tareas completadas"""
    tasks = [
        {"title": "Tarea A", "priority": 5, "completed": True},
        {"title": "Tarea B", "priority": 3, "completed": False},
        {"title": "Tarea C", "priority": 4, "completed": False},
    ]
    result = organize_tasks(tasks)
    
    assert len(result) == 2
    assert result[0]["title"] == "Tarea C"
    assert result[1]["title"] == "Tarea B"


def test_empty_list():
    """Lista vacía debe retornar lista vacía"""
    result = organize_tasks([])
    assert result == []


def test_all_completed():
    """Si todas están completadas, retorna lista vacía"""
    tasks = [
        {"title": "Tarea A", "priority": 5, "completed": True},
        {"title": "Tarea B", "priority": 3, "completed": True},
    ]
    result = organize_tasks(tasks)
    assert result == []


def test_all_pending():
    """Si todas están pendientes, todas deben aparecer ordenadas"""
    tasks = [
        {"title": "Tarea A", "priority": 1, "completed": False},
        {"title": "Tarea B", "priority": 5, "completed": False},
        {"title": "Tarea C", "priority": 3, "completed": False},
    ]
    result = organize_tasks(tasks)
    
    assert len(result) == 3
    priorities = [task["priority"] for task in result]
    assert priorities == [5, 3, 1]


def test_same_priority_maintains_order():
    """Tareas con la misma prioridad mantienen orden original"""
    tasks = [
        {"title": "Tarea A", "priority": 3, "completed": False},
        {"title": "Tarea B", "priority": 3, "completed": False},
        {"title": "Tarea C", "priority": 3, "completed": False},
    ]
    result = organize_tasks(tasks)
    
    titles = [task["title"] for task in result]
    assert titles == ["Tarea A", "Tarea B", "Tarea C"]


def test_single_task_pending():
    """Una sola tarea pendiente"""
    tasks = [{"title": "Única", "priority": 4, "completed": False}]
    result = organize_tasks(tasks)
    
    assert len(result) == 1
    assert result[0]["title"] == "Única"


def test_single_task_completed():
    """Una sola tarea completada"""
    tasks = [{"title": "Única", "priority": 4, "completed": True}]
    result = organize_tasks(tasks)
    assert result == []


def test_mixed_priorities():
    """Mezcla de prioridades del 1 al 5"""
    tasks = [
        {"title": "P1", "priority": 1, "completed": False},
        {"title": "P5", "priority": 5, "completed": False},
        {"title": "P3", "priority": 3, "completed": False},
        {"title": "P2", "priority": 2, "completed": False},
        {"title": "P4", "priority": 4, "completed": False},
    ]
    result = organize_tasks(tasks)
    
    priorities = [task["priority"] for task in result]
    assert priorities == [5, 4, 3, 2, 1]


def test_original_list_not_modified():
    """La lista original no debe modificarse"""
    tasks = [
        {"title": "A", "priority": 2, "completed": False},
        {"title": "B", "priority": 5, "completed": False},
    ]
    original_order = [task["title"] for task in tasks]
    
    result = organize_tasks(tasks)
    
    # La lista original debe mantener su orden
    current_order = [task["title"] for task in tasks]
    assert original_order == current_order


def test_return_type():
    """Verificar que retorna una lista"""
    tasks = [{"title": "A", "priority": 3, "completed": False}]
    result = organize_tasks(tasks)
    assert isinstance(result, list)


def test_result_contains_dicts():
    """Los elementos del resultado deben ser diccionarios"""
    tasks = [
        {"title": "A", "priority": 3, "completed": False},
        {"title": "B", "priority": 2, "completed": False},
    ]
    result = organize_tasks(tasks)
    
    for item in result:
        assert isinstance(item, dict)
        assert "title" in item
        assert "priority" in item
        assert "completed" in item


def test_all_result_items_are_pending():
    """Todos los items del resultado deben tener completed=False"""
    tasks = [
        {"title": "A", "priority": 5, "completed": False},
        {"title": "B", "priority": 3, "completed": True},
        {"title": "C", "priority": 4, "completed": False},
    ]
    result = organize_tasks(tasks)
    
    for task in result:
        assert task["completed"] == False


def test_high_priority_first():
    """La tarea con mayor prioridad debe estar primera"""
    tasks = [
        {"title": "Baja", "priority": 1, "completed": False},
        {"title": "Media", "priority": 3, "completed": False},
        {"title": "Crítica", "priority": 5, "completed": False},
    ]
    result = organize_tasks(tasks)
    
    assert result[0]["title"] == "Crítica"
    assert result[0]["priority"] == 5


def test_low_priority_last():
    """La tarea con menor prioridad debe estar última"""
    tasks = [
        {"title": "Alta", "priority": 5, "completed": False},
        {"title": "Media", "priority": 3, "completed": False},
        {"title": "Baja", "priority": 1, "completed": False},
    ]
    result = organize_tasks(tasks)
    
    assert result[-1]["title"] == "Baja"
    assert result[-1]["priority"] == 1


def test_realistic_scenario():
    """Escenario realista con múltiples tareas"""
    tasks = [
        {"title": "Fix critical bug", "priority": 5, "completed": False},
        {"title": "Write documentation", "priority": 2, "completed": False},
        {"title": "Code review", "priority": 3, "completed": True},
        {"title": "Deploy to production", "priority": 4, "completed": False},
        {"title": "Update dependencies", "priority": 2, "completed": False},
        {"title": "Refactor code", "priority": 3, "completed": False},
    ]
    result = organize_tasks(tasks)
    
    # Debe haber 5 tareas (excluye "Code review" que está completada)
    assert len(result) == 5
    
    # Orden esperado: 5 → 4 → 3 → 2 → 2
    expected_priorities = [5, 4, 3, 2, 2]
    actual_priorities = [task["priority"] for task in result]
    assert actual_priorities == expected_priorities


def test_performance_large_list():
    """Test de rendimiento con muchas tareas"""
    import time
    
    # Crear 1000 tareas
    tasks = [
        {
            "title": f"Tarea {i}",
            "priority": (i % 5) + 1,
            "completed": i % 3 == 0  # 1/3 están completadas
        }
        for i in range(1000)
    ]
    
    start = time.time()
    result = organize_tasks(tasks)
    elapsed = time.time() - start
    
    # Debe completarse en menos de 0.1 segundos
    assert elapsed < 0.1
    
    # Verificar que se filtraron correctamente
    assert len(result) < len(tasks)
    assert all(not task["completed"] for task in result)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])