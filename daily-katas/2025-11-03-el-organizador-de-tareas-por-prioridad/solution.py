def organize_tasks(tasks):
    """
    Organiza tareas filtrando las pendientes y ordenándolas por prioridad.
    
    Filtra solo las tareas no completadas (completed=False) y las ordena
    por prioridad de mayor a menor (5 → 1).
    
    Args:
        tasks: Lista de diccionarios con formato:
               {"title": str, "priority": int, "completed": bool}
    
    Returns:
        Lista de diccionarios con tareas pendientes ordenadas por prioridad
        descendente. Si no hay tareas pendientes, retorna []
    
    Ejemplos:
        >>> tasks = [
        ...     {"title": "A", "priority": 2, "completed": False},
        ...     {"title": "B", "priority": 5, "completed": False},
        ... ]
        >>> organize_tasks(tasks)
        [{"title": "B", "priority": 5, "completed": False},
         {"title": "A", "priority": 2, "completed": False}]
        
        >>> tasks = [{"title": "X", "priority": 5, "completed": True}]
        >>> organize_tasks(tasks)
        []
    """
    # TODO: Implementar la solución
    
    # Paso 1: Filtrar solo las tareas pendientes (completed = False)
    # Usa list comprehension:
    # pending_tasks = [task for task in tasks if task["completed"] == False]
    # O más simple: if not task["completed"]
    
    # Paso 2: Ordenar por prioridad (de mayor a menor)
    # Usa sorted() con key y reverse:
    # sorted(lista, key=lambda x: x["priority"], reverse=True)
    
    # ¿Qué es lambda?
    # lambda x: x["priority"] es una función que dice:
    # "dado un elemento x, devuélveme x['priority']"
    # Es equivalente a:
    # def get_priority(x):
    #     return x["priority"]
    
    # reverse=True ordena de mayor a menor
    
    # Paso 3: Retornar la lista ordenada
    
    pass


# DESAFÍO OPCIONAL: ¿Puedes hacerlo en una sola línea?
def organize_tasks_oneliner(tasks):
    """
    Versión de una línea (más avanzada)
    """
    # TODO: Intenta combinar el filtrado y ordenamiento en una expresión
    pass