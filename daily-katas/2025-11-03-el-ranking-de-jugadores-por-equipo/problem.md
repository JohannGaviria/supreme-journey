# El Ranking de Jugadores por Equipo

## Contexto

Eres el desarrollador de una plataforma de eSports. Necesitas crear un sistema de rankings que muestre los **mejores jugadores de cada equipo**, pero con reglas específicas:

1. Solo considerar jugadores **activos** (`active = True`)
2. Agrupar jugadores por **equipo**
3. Dentro de cada equipo, ordenar por **puntuación** (de mayor a menor)
4. Mostrar solo los **top 3** jugadores de cada equipo
5. Si un equipo tiene menos de 3 jugadores, mostrar los que tenga

Este problema combina **filtrado, agrupamiento, ordenamiento y limitación**, simulando un escenario real de ranking/leaderboard.

## Entrada

- `players`: Lista de diccionarios, donde cada uno representa un jugador:
  - `"name"`: String con el nombre del jugador
  - `"team"`: String con el nombre del equipo
  - `"score"`: Int con la puntuación del jugador
  - `"active"`: Boolean indicando si está activo

Ejemplo de entrada:
```python
players = [
    {"name": "Alice", "team": "Dragons", "score": 1500, "active": True},
    {"name": "Bob", "team": "Dragons", "score": 1200, "active": True},
    {"name": "Charlie", "team": "Tigers", "score": 1800, "active": False},
]
```

## Salida

- Un diccionario donde:
  - Las **claves** son los nombres de los equipos (strings)
  - Los **valores** son listas de jugadores (diccionarios completos)
  - Cada lista contiene **máximo 3 jugadores**
  - Los jugadores están **ordenados por score descendente**
  - Solo incluye equipos que tengan **al menos un jugador activo**

Formato del resultado:
```python
{
    "TeamName": [
        {"name": "Player1", "team": "TeamName", "score": 2000, "active": True},
        {"name": "Player2", "team": "TeamName", "score": 1800, "active": True},
        {"name": "Player3", "team": "TeamName", "score": 1500, "active": True},
    ],
    "OtherTeam": [...],
}
```

## Ejemplos

### Ejemplo 1: Básico con top 3
```python
# Entrada:
players = [
    {"name": "Alice", "team": "Dragons", "score": 1500, "active": True},
    {"name": "Bob", "team": "Dragons", "score": 1800, "active": True},
    {"name": "Carol", "team": "Dragons", "score": 1200, "active": True},
    {"name": "Dave", "team": "Dragons", "score": 1600, "active": True},
]

# Salida esperada:
{
    "Dragons": [
        {"name": "Bob", "team": "Dragons", "score": 1800, "active": True},
        {"name": "Dave", "team": "Dragons", "score": 1600, "active": True},
        {"name": "Alice", "team": "Dragons", "score": 1500, "active": True},
    ]
}
# Carol (1200) queda fuera porque solo mostramos top 3
```

### Ejemplo 2: Filtrar inactivos
```python
# Entrada:
players = [
    {"name": "Alice", "team": "Tigers", "score": 2000, "active": True},
    {"name": "Bob", "team": "Tigers", "score": 2500, "active": False},  # Inactivo
    {"name": "Carol", "team": "Tigers", "score": 1800, "active": True},
]

# Salida esperada:
{
    "Tigers": [
        {"name": "Alice", "team": "Tigers", "score": 2000, "active": True},
        {"name": "Carol", "team": "Tigers", "score": 1800, "active": True},
    ]
}
# Bob no aparece porque está inactivo
```

### Ejemplo 3: Múltiples equipos
```python
# Entrada:
players = [
    {"name": "Alice", "team": "Dragons", "score": 1500, "active": True},
    {"name": "Bob", "team": "Tigers", "score": 1800, "active": True},
    {"name": "Carol", "team": "Dragons", "score": 1700, "active": True},
    {"name": "Dave", "team": "Tigers", "score": 1600, "active": True},
]

# Salida esperada:
{
    "Dragons": [
        {"name": "Carol", "team": "Dragons", "score": 1700, "active": True},
        {"name": "Alice", "team": "Dragons", "score": 1500, "active": True},
    ],
    "Tigers": [
        {"name": "Bob", "team": "Tigers", "score": 1800, "active": True},
        {"name": "Dave", "team": "Tigers", "score": 1600, "active": True},
    ]
}
```

### Ejemplo 4: Equipo sin jugadores activos
```python
# Entrada:
players = [
    {"name": "Alice", "team": "Dragons", "score": 1500, "active": False},
    {"name": "Bob", "team": "Tigers", "score": 1800, "active": True},
]

# Salida esperada:
{
    "Tigers": [
        {"name": "Bob", "team": "Tigers", "score": 1800, "active": True},
    ]
}
# Dragons no aparece porque no tiene jugadores activos
```

### Ejemplo 5: Lista vacía
```python
# Entrada:
players = []

# Salida esperada:
{}
```

## Restricciones

- `0 ≤ len(players) ≤ 10,000` jugadores
- `1 ≤ score ≤ 100,000` (entero positivo)
- `team` y `name` son siempre strings no vacíos
- `active` es siempre un booleano
- Tiempo esperado: O(n log n) donde n es el número de jugadores
- No modifiques la lista original de entrada
- No uses librerías externas (solo Python estándar)

## Pistas

💡 **Pista 1**: Divide el problema en pasos: Filtrar → Agrupar → Ordenar → Limitar

💡 **Pista 2**: Primero filtra solo los jugadores activos (como en ejercicio #3)

💡 **Pista 3**: Luego agrúpalos por equipo en un diccionario (como en ejercicio #4)

💡 **Pista 4**: Para cada equipo, ordena sus jugadores por score descendente (como en ejercicio #3)

💡 **Pista 5**: Usa slicing `[:3]` para obtener solo los primeros 3 elementos de una lista

💡 **Pista 6**: Puedes inicializar el diccionario de equipos con listas vacías o usar `.setdefault()`

💡 **Pista 7**: Patrón general:
```python
# 1. Filtrar
activos = [p for p in players if p["active"]]

# 2. Agrupar
equipos = {}
for jugador in activos:
    team = jugador["team"]
    if team not in equipos:
        equipos[team] = []
    equipos[team].append(jugador)

# 3. Ordenar y limitar
for team in equipos:
    equipos[team] = sorted(equipos[team], key=..., reverse=True)[:3]
```

## Objetivos que entrena

✅ **Pipeline de datos**: Encadenar múltiples operaciones (filtrar → agrupar → ordenar → limitar)  
✅ **Pensamiento modular**: Dividir problemas complejos en pasos simples  
✅ **Síntesis de conceptos**: Combinar técnicas de los 4 ejercicios anteriores  
✅ **Top N pattern**: Limitación de resultados (muy común en rankings)  
✅ **Manejo de estructuras anidadas**: Diccionarios con listas de diccionarios  
✅ **Optimización**: Pensar en el orden óptimo de operaciones  
✅ **Preparación para problemas reales**: Este tipo de lógica es omnipresente en apps

---

🗓️ **Creada:** 2025-11-03  
✅ **Resuelta:** YYYY-MM-DD  
⏱️ **Dificultad percibida:** (fácil / medio / difícil)  
🧠 **Observaciones:**
  - (¿Qué paso te resultó más difícil?)
  - (¿Pudiste reutilizar código mental de ejercicios anteriores?)
  - (¿Entendiste por qué filtramos ANTES de agrupar?)
  - (¿Cómo te sentiste resolviendo este ejercicio final?)
  - (¿Qué aprendiste de toda la serie de 5 ejercicios?)