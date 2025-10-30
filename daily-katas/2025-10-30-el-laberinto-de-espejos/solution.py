def trace_light_beam(grid, entry_side, entry_position):
    """
    Simula el recorrido de un rayo de luz en un laberinto de espejos.
    
    Args:
        grid: Lista de strings representando el laberinto
        entry_side: Lado de entrada ("north", "south", "east", "west")
        entry_position: Posición de entrada (0-indexed)
    
    Returns:
        Diccionario con 'exit_side' y 'exit_position'
        Si hay bucle: {'exit_side': 'loop', 'exit_position': None}
    
    Ejemplos:
        >>> grid = ["...", "./.", "..."]
        >>> trace_light_beam(grid, "west", 1)
        {'exit_side': 'north', 'exit_position': 1}
    """
    # TODO: Implementar la solución
    
    # Paso 1: Definir las direcciones como vectores (row_delta, col_delta)
    # Ejemplo: "right" podría ser (0, 1), "down" podría ser (1, 0)
    
    # Paso 2: Crear un diccionario de reflexiones
    # Clave: (dirección_actual, tipo_espejo)
    # Valor: nueva_dirección
    
    # Paso 3: Determinar posición y dirección inicial según entry_side
    
    # Paso 4: Simular el movimiento del rayo
    # - Llevar registro de estados visitados (posición + dirección)
    # - En cada paso: mover, verificar si salió o si hay espejo
    # - Si hay espejo: cambiar dirección según las reglas
    # - Si el estado se repite: es un loop
    
    # Paso 5: Retornar el resultado
    
    pass


# Puedes usar estas constantes si te ayudan:
# DIRECTIONS = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1)
# }
#
# REFLECTIONS = {
#     ("right", "/"): "up",
#     ("right", "\\"): "down",
#     # ... completar el resto
# }