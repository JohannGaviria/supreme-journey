# 🧠 Prompt Kata diaria

Crea un reto tipo *kata* en **Python** siguiendo estas reglas:

### General

- Nivel: **(fácil / medio / difícil)**  
- Orientación: **(entrevistas técnicas / programación competitiva / lógica y estructuras de datos)**  
- Tema o tipo de problema: **(por ejemplo: recursion, arrays, grafos, dynamic programming, backtracking, etc.)**

### Enunciado

- Incluye un **enunciado completo y detallado** con:
  - Contexto breve o historia (opcional, para hacerlo más entretenido)  
  - Entradas y salidas esperadas  
  - Ejemplos de entrada/salida  
  - Restricciones (tamaño máximo de entrada, tiempo esperado, complejidad si aplica)

### Código base

- Proporciona solo la **función vacía o incompleta**, sin solución implementada.  
- Usa **nombres de funciones y variables claros**, tipo *snake_case*.  
- No incluyas librerías externas, solo las estándar de Python.

### Tests automáticos

- Crea un archivo de pruebas con **tests listos para ejecutar con `pytest`**.  
- Incluye al menos **3–5 casos**, con nombres descriptivos (`test_case_name`).  
- Cubre casos normales, límites y edge cases.  
- Si el problema lo permite, agrega un test de rendimiento pequeño (por ejemplo, verificar que corra en < 1s con inputs grandes).

### Extras

- Agrega una sección **"Pistas"** con sugerencias para resolver el problema (sin spoilers directos).  
- Incluye una sección **"Objetivos que entrena"**, indicando los conceptos o patrones de pensamiento que desarrolla.  
- Devuelve el resultado formateado en **tres bloques de código**:
  1. `problem.md` → Enunciado y contexto  
  2. `solution.py` → Código base con función vacía y comentarios  
  3. `test_solution.py` → Tests automáticos en pytest

### Estructura final esperada

```
daily-katas/
├── YYYY-MM-DD-problem-name/
│   ├── problem.md
│   ├── solution.py
│   ├── test_solution.py
```

### Template para `problem.md`

Usa exactamente esta estructura para el contenido del archivo:

````markdown
# {{KATA_TITLE}}

## Contexto

Describe el contexto o historia del problema aquí.

## Entrada

- Explica los parámetros de entrada.

## Salida

- Explica el formato de la salida esperada.

## Ejemplos

### Ejemplo 1
```python
# Entrada:
# ...
# Salida esperada:
# ...
```

## Restricciones

- Lista las restricciones del problema.

## Pistas

- Agrega pistas opcionales para ayudar a resolver la kata.

## Objetivos que entrena

- Enumera los conceptos o habilidades que se practican con esta kata.

---

🗓️ Creada: {{KATA_CREATED}}
✅ Resuelta: YYYY-MM-DD
⏱️ Dificultad percibida: (fácil / medio / difícil)
🧠 Observaciones:
  - (Aquí puedes anotar lo que aprendiste, los errores que cometiste o posibles mejoras)
````

### Consideraciones finales

* El problema debe tener **una solución única o verificable**.
* Debe ser lo suficientemente interesante para **subirse a GitHub** como parte de tu colección personal.
* No copies enunciados de plataformas existentes (puedes inspirarte, pero redacta todo desde cero).
