import pytest
from solution import rank_players_by_team


def test_basic_top_3():
    """Caso básico: un equipo con 4 jugadores, debe mostrar top 3"""
    players = [
        {"name": "Alice", "team": "Dragons", "score": 1500, "active": True},
        {"name": "Bob", "team": "Dragons", "score": 1800, "active": True},
        {"name": "Carol", "team": "Dragons", "score": 1200, "active": True},
        {"name": "Dave", "team": "Dragons", "score": 1600, "active": True},
    ]
    result = rank_players_by_team(players)
    
    assert len(result["Dragons"]) == 3
    assert result["Dragons"][0]["name"] == "Bob"  # Mayor score
    assert result["Dragons"][1]["name"] == "Dave"
    assert result["Dragons"][2]["name"] == "Alice"
    # Carol no debe aparecer (4° lugar)


def test_filter_inactive():
    """Debe filtrar jugadores inactivos"""
    players = [
        {"name": "Alice", "team": "Tigers", "score": 2000, "active": True},
        {"name": "Bob", "team": "Tigers", "score": 2500, "active": False},
        {"name": "Carol", "team": "Tigers", "score": 1800, "active": True},
    ]
    result = rank_players_by_team(players)
    
    assert len(result["Tigers"]) == 2
    assert result["Tigers"][0]["name"] == "Alice"
    assert result["Tigers"][1]["name"] == "Carol"
    # Bob no debe aparecer (inactivo)


def test_multiple_teams():
    """Múltiples equipos con rankings independientes"""
    players = [
        {"name": "Alice", "team": "Dragons", "score": 1500, "active": True},
        {"name": "Bob", "team": "Tigers", "score": 1800, "active": True},
        {"name": "Carol", "team": "Dragons", "score": 1700, "active": True},
        {"name": "Dave", "team": "Tigers", "score": 1600, "active": True},
    ]
    result = rank_players_by_team(players)
    
    assert len(result) == 2
    assert "Dragons" in result
    assert "Tigers" in result
    assert result["Dragons"][0]["name"] == "Carol"
    assert result["Tigers"][0]["name"] == "Bob"


def test_empty_list():
    """Lista vacía debe retornar diccionario vacío"""
    result = rank_players_by_team([])
    assert result == {}


def test_team_without_active_players():
    """Equipo sin jugadores activos no debe aparecer"""
    players = [
        {"name": "Alice", "team": "Dragons", "score": 1500, "active": False},
        {"name": "Bob", "team": "Tigers", "score": 1800, "active": True},
    ]
    result = rank_players_by_team(players)
    
    assert "Dragons" not in result
    assert "Tigers" in result


def test_single_player():
    """Un solo jugador activo"""
    players = [
        {"name": "Alice", "team": "Dragons", "score": 1500, "active": True},
    ]
    result = rank_players_by_team(players)
    
    assert len(result["Dragons"]) == 1
    assert result["Dragons"][0]["name"] == "Alice"


def test_exactly_three_players():
    """Equipo con exactamente 3 jugadores activos"""
    players = [
        {"name": "Alice", "team": "Dragons", "score": 1500, "active": True},
        {"name": "Bob", "team": "Dragons", "score": 1800, "active": True},
        {"name": "Carol", "team": "Dragons", "score": 1200, "active": True},
    ]
    result = rank_players_by_team(players)
    
    assert len(result["Dragons"]) == 3


def test_less_than_three_players():
    """Equipo con menos de 3 jugadores activos"""
    players = [
        {"name": "Alice", "team": "Dragons", "score": 1500, "active": True},
        {"name": "Bob", "team": "Dragons", "score": 1800, "active": True},
    ]
    result = rank_players_by_team(players)
    
    assert len(result["Dragons"]) == 2


def test_score_ordering():
    """Verificar que el orden es por score descendente"""
    players = [
        {"name": "Low", "team": "Test", "score": 1000, "active": True},
        {"name": "High", "team": "Test", "score": 3000, "active": True},
        {"name": "Mid", "team": "Test", "score": 2000, "active": True},
    ]
    result = rank_players_by_team(players)
    
    scores = [p["score"] for p in result["Test"]]
    assert scores == [3000, 2000, 1000]


def test_same_scores():
    """Jugadores con el mismo score (mantiene orden estable)"""
    players = [
        {"name": "Alice", "team": "Dragons", "score": 1500, "active": True},
        {"name": "Bob", "team": "Dragons", "score": 1500, "active": True},
        {"name": "Carol", "team": "Dragons", "score": 1500, "active": True},
    ]
    result = rank_players_by_team(players)
    
    # Todos deben aparecer, el orden específico puede variar pero es estable
    assert len(result["Dragons"]) == 3


def test_return_type():
    """Verificar tipos de retorno"""
    players = [
        {"name": "Alice", "team": "Dragons", "score": 1500, "active": True},
    ]
    result = rank_players_by_team(players)
    
    assert isinstance(result, dict)
    assert isinstance(result["Dragons"], list)
    assert isinstance(result["Dragons"][0], dict)


def test_player_structure_preserved():
    """Los jugadores en el resultado deben mantener toda su estructura"""
    players = [
        {"name": "Alice", "team": "Dragons", "score": 1500, "active": True},
    ]
    result = rank_players_by_team(players)
    
    player = result["Dragons"][0]
    assert "name" in player
    assert "team" in player
    assert "score" in player
    assert "active" in player


def test_original_list_not_modified():
    """La lista original no debe modificarse"""
    players = [
        {"name": "Alice", "team": "Dragons", "score": 1500, "active": True},
        {"name": "Bob", "team": "Dragons", "score": 1800, "active": True},
    ]
    original_length = len(players)
    
    result = rank_players_by_team(players)
    
    assert len(players) == original_length


def test_all_inactive():
    """Todos los jugadores inactivos"""
    players = [
        {"name": "Alice", "team": "Dragons", "score": 1500, "active": False},
        {"name": "Bob", "team": "Tigers", "score": 1800, "active": False},
    ]
    result = rank_players_by_team(players)
    
    assert result == {}


def test_large_score_range():
    """Jugadores con rangos de puntuación muy variados"""
    players = [
        {"name": "Noob", "team": "Test", "score": 100, "active": True},
        {"name": "Pro", "team": "Test", "score": 50000, "active": True},
        {"name": "Mid", "team": "Test", "score": 25000, "active": True},
    ]
    result = rank_players_by_team(players)
    
    assert result["Test"][0]["name"] == "Pro"
    assert result["Test"][1]["name"] == "Mid"
    assert result["Test"][2]["name"] == "Noob"


def test_many_teams():
    """Muchos equipos diferentes"""
    players = [
        {"name": f"Player{i}", "team": f"Team{i % 5}", "score": i * 100, "active": True}
        for i in range(20)
    ]
    result = rank_players_by_team(players)
    
    # Debe haber 5 equipos
    assert len(result) == 5
    # Cada equipo debe tener máximo 3 jugadores
    for team_players in result.values():
        assert len(team_players) <= 3


def test_realistic_esports_scenario():
    """Escenario realista de eSports"""
    players = [
        # Team Dragons (4 activos, 1 inactivo)
        {"name": "DragonKing", "team": "Dragons", "score": 2500, "active": True},
        {"name": "DragonFire", "team": "Dragons", "score": 2300, "active": True},
        {"name": "DragonWing", "team": "Dragons", "score": 2100, "active": True},
        {"name": "DragonClaw", "team": "Dragons", "score": 1900, "active": True},
        {"name": "DragonOld", "team": "Dragons", "score": 3000, "active": False},
        
        # Team Tigers (2 activos)
        {"name": "TigerStrike", "team": "Tigers", "score": 2800, "active": True},
        {"name": "TigerRoar", "team": "Tigers", "score": 2600, "active": True},
        
        # Team Wolves (todos inactivos)
        {"name": "WolfPack", "team": "Wolves", "score": 2700, "active": False},
    ]
    result = rank_players_by_team(players)
    
    # Solo Dragons y Tigers deben aparecer
    assert len(result) == 2
    assert "Wolves" not in result
    
    # Dragons debe tener top 3
    assert len(result["Dragons"]) == 3
    assert result["Dragons"][0]["name"] == "DragonKing"
    
    # Tigers debe tener solo 2
    assert len(result["Tigers"]) == 2
    assert result["Tigers"][0]["name"] == "TigerStrike"


def test_performance_large_dataset():
    """Test de rendimiento con muchos jugadores"""
    import time
    
    # 10,000 jugadores en 100 equipos
    players = [
        {
            "name": f"Player{i}",
            "team": f"Team{i % 100}",
            "score": (i * 7) % 10000,
            "active": i % 4 != 0  # 75% activos
        }
        for i in range(10000)
    ]
    
    start = time.time()
    result = rank_players_by_team(players)
    elapsed = time.time() - start
    
    # Debe completarse en menos de 0.5 segundos
    assert elapsed < 0.5
    
    # Verificaciones básicas
    assert len(result) <= 100
    for team_players in result.values():
        assert len(team_players) <= 3
        assert all(p["active"] for p in team_players)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
