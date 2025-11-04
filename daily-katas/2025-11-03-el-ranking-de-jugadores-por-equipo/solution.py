def rank_players_by_team(players):
    """
    Crea un ranking mostrando los top 3 jugadores activos de cada equipo.
    
    Procesa la lista de jugadores:
    1. Filtra solo los activos
    2. Agrupa por equipo
    3. Ordena por puntuación (mayor a menor)
    4. Limita a top 3 por equipo
    
    Args:
        players: Lista de diccionarios con formato:
                 {"name": str, "team": str, "score": int, "active": bool}
    
    Returns:
        Diccionario donde las claves son equipos y los valores son listas
        de máximo 3 jugadores ordenados por score descendente.
        Solo incluye equipos con al menos un jugador activo.
    
    Ejemplos:
        >>> players = [
        ...     {"name": "Alice", "team": "Dragons", "score": 1500, "active": True},
        ...     {"name": "Bob", "team": "Dragons", "score": 1800, "active": True},
        ... ]
        >>> result = rank_players_by_team(players)
        >>> result["Dragons"][0]["name"]
        'Bob'
    """
    # TODO: Implementar la solución
    
    # PASO 1: Filtrar solo jugadores activos
    # Usa list comprehension (como ejercicio #3)
    # active_players = [player for player in players if player["active"]]
    
    # PASO 2: Agrupar jugadores por equipo
    # Crea un diccionario donde cada equipo tiene una lista de jugadores
    # teams = {}
    # for player in active_players:
    #     team_name = player["team"]
    #     if team_name not in teams:
    #         teams[team_name] = []
    #     teams[team_name].append(player)
    
    # Alternativa con setdefault:
    # teams.setdefault(team_name, []).append(player)
    
    # PASO 3: Para cada equipo, ordenar jugadores por score y tomar top 3
    # for team_name in teams:
    #     # Ordenar por score descendente
    #     teams[team_name] = sorted(
    #         teams[team_name],
    #         key=lambda p: p["score"],
    #         reverse=True
    #     )[:3]  # Tomar solo los primeros 3
    
    # PASO 4: Retornar el diccionario de rankings
    # return teams
    
    pass


# DESAFÍO OPCIONAL 1: Versión más compacta
def rank_players_by_team_compact(players):
    """
    Versión más compacta usando técnicas avanzadas.
    ¿Puedes hacerlo con menos líneas?
    """
    # TODO: Intenta una versión más concisa
    pass


# DESAFÍO OPCIONAL 2: Con información agregada
def rank_players_with_stats(players):
    """
    Además del ranking, incluye estadísticas del equipo:
    - Número total de jugadores activos
    - Puntuación promedio del top 3
    
    Returns:
        {
            "TeamName": {
                "players": [...],
                "total_active": 5,
                "avg_score": 1600.0
            }
        }
    """
    # TODO: Implementar versión extendida (más desafiante)
    pass


# DESAFÍO OPCIONAL 3: Top N configurable
def rank_players_top_n(players, n=3):
    """
    Versión que permite configurar cuántos jugadores mostrar (en lugar de 3 fijo).
    
    Args:
        players: Lista de jugadores
        n: Número de jugadores top a mostrar por equipo (default: 3)
    """
    # TODO: Implementar con parámetro n
    pass
