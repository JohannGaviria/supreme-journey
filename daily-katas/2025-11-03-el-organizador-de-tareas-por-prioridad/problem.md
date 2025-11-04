# El Organizador de Tareas por Prioridad

## Contexto

Estás desarrollando un gestor de tareas para un equipo de desarrollo. El equipo añade tareas con diferentes prioridades, pero la lista se va desordenando con el tiempo. 

Tu misión es crear una función que:
1. Reciba una lista de tareas (cada una con título, prioridad y estado)
2. Filtre solo las tareas pendientes
3. Las ordene por prioridad (de mayor a menor)
4. Retorne la lista organizada

Este tipo de problema es **muy común en aplicaciones reales** y en entrevistas técnicas.

## Entrada

- `tasks`: Lista de diccionarios, donde cada diccionario representa una tarea con:
  - `"title"`: String con el nombre de la tarea
  - `"priority"`: Entero del 1 al 5 (1 = baja, 5 = crítica)
  - `"completed"`: Boolean (True = completada, False = pendiente)

Ejemplo de entrada:
```python
tasks = [
    {"title": "Fix bug", "priority": 5, "completed": False},
    {"title": "Write tests", "priority": 3, "completed": False},
    {"title": "Deploy", "priority": 4, "completed": True},
]
```

## Salida

- Una lista de diccionarios con **solo las tareas pendientes** (`completed = False`)
- Ordenadas por `priority` de **mayor a menor** (5 → 4 → 3 → 2 → 1)
- Si hay tareas con la misma prioridad, mantener el orden original
- Si no hay tareas pendientes, retornar lista vacía `[]`

## Ejemplos

### Ejemplo 1: Ordenamiento básico
```python
# Entrada:
tasks = [
    {"title": "Tarea A", "priority": 2, "completed": False},
    {"title": "Tarea B", "priority": 5, "completed": False},
    {"title": "Tarea C", "priority": 3, "completed": False},
]

# Salida esperada:
[
    {"title": "Tarea B", "priority": 5, "completed": False},
    {"title": "Tarea C", "priority": 3, "completed": False},
    {"title": "Tarea A", "priority": 2, "completed": False},
]
```

### Ejemplo 2: Filtrar completadas
```python
# Entrada:
tasks = [
    {"title": "Tarea A", "priority": 5, "completed": True},  # Completada
    {"title": "Tarea B", "priority": 3, "completed": False},
    {"title": "Tarea C", "priority": 4, "completed": False},
]

# Salida esperada:
[
    {"title": "Tarea C", "priority": 4, "completed": False},
    {"title": "Tarea B", "priority": 3, "completed": False},
]
# La Tarea A no aparece porque está completada
```

### Ejemplo 3: Lista vacía
```python
# Entrada:
tasks = []

# Salida esperada:
[]
```

### Ejemplo 4: Todas completadas
```python
# Entrada:
tasks = [
    {"title": "Tarea A", "priority": 5, "completed": True},
    {"title": "Tarea B", "priority": 3, "completed": True},
]

# Salida esperada:
[]
```

### Ejemplo 5: Misma prioridad
```python
# Entrada:
tasks = [
    {"title": "Tarea A", "priority": 3, "completed": False},
    {"title": "Tarea B", "priority": 3, "completed": False},
    {"title": "Tarea C", "priority": 3, "completed": False},
]

# Salida esperada (mantiene orden original):
[
    {"title": "Tarea A", "priority": 3, "completed": False},
    {"title": "Tarea B", "priority": 3, "completed": False},
    {"title": "Tarea C", "priority": 3, "completed": False},
]
```

## Restricciones

- `0 ≤ len(tasks) ≤ 1000` tareas
- `1 ≤ priority ≤ 5` (entero)
- `completed` es siempre un booleano
- `title` es siempre un string no vacío
- Tiempo esperado: O(n log n) por el ordenamiento
- No modifiques la lista original de entrada

## Pistas

💡 **Pista 1**: Primero filtra, luego ordena (es más eficiente)

💡 **Pista 2**: Usa list comprehension para filtrar: `[task for task in tasks if condicion]`

💡 **Pista 3**: El método `.sort()` modifica la lista, pero `sorted()` crea una nueva

💡 **Pista 4**: Para ordenar por prioridad descendente: `sorted(lista, key=lambda x: x["priority"], reverse=True)`

💡 **Pista 5**: Lambda es una función anónima: `lambda x: x["priority"]` significa "dame el valor de priority de x"

💡 **Pista 6**: El ordenamiento en Python es "estable" (mantiene orden relativo de elementos iguales)

## Objetivos que entrena

✅ **Trabajo con listas de diccionarios**: Estructuras de datos anidadas muy comunes  
✅ **Filtrado de listas**: List comprehensions o filter()  
✅ **Ordenamiento con criterios**: sorted() + lambda functions  
✅ **Acceso a claves de diccionarios**: Navegación en estructuras complejas  
✅ **Inmutabilidad**: No modificar datos originales  
✅ **Transformación de datos**: De una estructura a otra  
✅ **Problema real**: Este ejercicio modela aplicaciones del mundo real

---

🗓️ **Creada:** 2025-11-03  
✅ **Resuelta:** YYYY-MM-DD  
⏱️ **Dificultad percibida:** (fácil / medio / difícil)  
🧠 **Observaciones:**
  - (¿Entendiste cómo funcionan las lambda functions?)
  - (¿Usaste sorted() o .sort()? ¿Por qué?)
  - (¿Te resultó difícil trabajar con diccionarios dentro de listas?)
  - (¿Probaste el código con tus propios ejemplos?)