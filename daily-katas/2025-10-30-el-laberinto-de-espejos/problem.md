# El Laberinto de Espejos 🪞

## Contexto

Estás explorando un antiguo templo lleno de espejos mágicos. El templo tiene forma de cuadrícula rectangular donde cada celda puede contener:
- Un espacio vacío (`.`)
- Un espejo diagonal derecho (`/`)
- Un espejo diagonal izquierdo (`\`)

Entras al templo por una de las cuatro direcciones (norte, sur, este, oeste) y un rayo de luz te acompaña. Los espejos reflejan el rayo de la siguiente manera:

- Si el rayo va **hacia la derecha** (`→`) y encuentra `/`, se refleja **hacia arriba** (`↑`)
- Si el rayo va **hacia la derecha** (`→`) y encuentra `\`, se refleja **hacia abajo** (`↓`)
- Si el rayo va **hacia arriba** (`↑`) y encuentra `/`, se refleja **hacia la derecha** (`→`)
- Si el rayo va **hacia arriba** (`↑`) y encuentra `\`, se refleja **hacia la izquierda** (`←`)
- Y así sucesivamente para todas las direcciones...

Tu misión es determinar **por qué lado del templo saldrá el rayo de luz** (o si quedará atrapado en un bucle infinito).

## Entrada

- `grid`: Lista de strings representando el laberinto (cada string es una fila)
- `entry_side`: String indicando el lado de entrada: `"north"`, `"south"`, `"east"`, `"west"`
- `entry_position`: Entero indicando la posición de entrada (0-indexed)

### Convenciones de entrada:

- **North**: El rayo entra desde arriba en la columna `entry_position`, moviéndose hacia abajo
- **South**: El rayo entra desde abajo en la columna `entry_position`, moviéndose hacia arriba
- **East**: El rayo entra desde la derecha en la fila `entry_position`, moviéndose hacia la izquierda
- **West**: El rayo entra desde la izquierda en la fila `entry_position`, moviéndose hacia la derecha

## Salida

Un diccionario con:
- `exit_side`: `"north"`, `"south"`, `"east"`, `"west"`, o `"loop"` si queda atrapado
- `exit_position`: Entero con la posición de salida (o `None` si hay loop)

## Ejemplos

### Ejemplo 1: Salida simple
```python
grid = [
    "...",
    "./.",
    "..."
]
entry_side = "west"
entry_position = 1

# El rayo entra por la izquierda en la fila 1
# Encuentra el espejo / en posición [1, 1]
# Se refleja hacia arriba y sale por el norte en columna 1

Resultado: {"exit_side": "north", "exit_position": 1}
```

### Ejemplo 2: Múltiples reflexiones
```python
grid = [
    r"\/",
    r"/\"
]
entry_side = "west"
entry_position = 0

# El rayo rebota entre los espejos varias veces
# Finalmente sale por el sur en columna 1

Resultado: {"exit_side": "south", "exit_position": 1}
```

### Ejemplo 3: Bucle infinito
```python
grid = [
    r"\/",
    r"\/"
]
entry_side = "west"
entry_position = 0

# El rayo queda atrapado rebotando infinitamente

Resultado: {"exit_side": "loop", "exit_position": None}
```

## Restricciones

- `1 ≤ len(grid) ≤ 100` (altura)
- `1 ≤ len(grid[0]) ≤ 100` (ancho)
- Todas las filas tienen la misma longitud
- `entry_position` es siempre válido según las dimensiones
- El grid solo contiene `.`, `/`, y `\`
- Tiempo esperado: O(n × m) donde n y m son las dimensiones

## Pistas

💡 **Pista 1**: Necesitas llevar registro de la posición actual Y la dirección del rayo

💡 **Pista 2**: Para detectar ciclos, piensa en qué significa que el rayo "ya pasó por aquí antes"... no es solo la posición

💡 **Pista 3**: Crea un diccionario que mapee (dirección, tipo_espejo) → nueva_dirección

💡 **Pista 4**: Los bordes del grid son tus condiciones de salida

## Objetivos que entrena

✅ **Simulación de sistemas**: Modelar un proceso paso a paso con reglas claras  
✅ **Detección de ciclos**: Identificar cuándo un estado se repite  
✅ **Trabajo con direcciones**: Manejo de coordenadas 2D y transformaciones  
✅ **Edge cases**: Considerar límites, bucles y casos extremos  
✅ **Estructuras de datos**: Uso eficiente de sets y tuplas como claves

---

🗓️ Creada: {{KATA_CREATED}}
✅ Resuelta: YYYY-MM-DD
⏱️ Dificultad percibida: (fácil / medio / difícil)
🧠 Observaciones:
  - (Aquí puedes anotar lo que aprendiste, los errores que cometiste o posibles mejoras)
