# El Detector de Palabras Repetidas

## Contexto

Estás construyendo un moderador de comentarios para una red social. Una de las funciones que necesitas es detectar cuando alguien repite palabras innecesariamente en su mensaje (como "esto esto esto es genial genial").

Tu tarea es crear una función que identifique **qué palabras aparecen más de una vez** en un texto y **cuántas veces aparece cada una**.

A diferencia del ejercicio anterior donde contábamos caracteres, ahora contaremos **palabras completas**.

## Entrada

- `text`: String que contiene palabras separadas por espacios
- Las palabras pueden estar en mayúsculas o minúsculas
- Puede contener signos de puntuación pegados a las palabras
- Puede ser una cadena vacía

## Salida

- Un diccionario con **solo las palabras que aparecen más de una vez**
- Las claves son las palabras en minúsculas (normalizadas)
- Los valores son enteros indicando cuántas veces aparecen
- Si ninguna palabra se repite, retorna un diccionario vacío `{}`

## Ejemplos

### Ejemplo 1: Palabras repetidas simples
```python
# Entrada:
text = "hola mundo hola"

# Salida esperada:
{'hola': 2}
```

### Ejemplo 2: Múltiples repeticiones
```python
# Entrada:
text = "esto esto esto es genial genial"

# Salida esperada:
{'esto': 3, 'genial': 2}
```

### Ejemplo 3: Sin repeticiones
```python
# Entrada:
text = "cada palabra es unica"

# Salida esperada:
{}
```

### Ejemplo 4: Con mayúsculas mezcladas
```python
# Entrada:
text = "Python python PYTHON es genial"

# Salida esperada:
{'python': 3}
```

### Ejemplo 5: Con puntuación
```python
# Entrada:
text = "hola, hola! mundo."

# Salida esperada:
# Nota: 'hola,' y 'hola!' son palabras diferentes por la puntuación
{'hola,': 1, 'hola!': 1}
# O si limpias la puntuación:
{'hola': 2}
```

## Restricciones

- `0 ≤ len(text) ≤ 10,000` caracteres
- Las palabras están separadas por espacios simples o múltiples
- Tiempo esperado: O(n) donde n es el número de palabras
- No uses librerías externas (solo Python estándar)
- **Decisión de diseño**: Puedes elegir si limpiar o no la puntuación
  - Versión simple: No limpies (más fácil)
  - Versión avanzada: Limpia signos de puntuación (más realista)

## Pistas

💡 **Pista 1**: El método `.split()` divide un string en una lista de palabras

💡 **Pista 2**: Reutiliza el patrón del ejercicio anterior: inicializar diccionario → iterar → acumular

💡 **Pista 3**: Cuenta TODAS las palabras primero, luego filtra las que aparecen > 1 vez

💡 **Pista 4**: Puedes usar `.lower()` para normalizar mayúsculas/minúsculas

💡 **Pista 5**: Para crear el diccionario final, puedes usar comprensión de diccionarios o un loop con condición

💡 **Pista 6** (avanzada): Para limpiar puntuación, puedes usar `.strip('.,!?;:')` o el módulo `string`

## Objetivos que entrena

✅ **Procesamiento de palabras**: Trabajar con tokens en lugar de caracteres  
✅ **Uso de .split()**: Dividir strings en listas  
✅ **Filtrado de resultados**: Seleccionar solo datos relevantes  
✅ **Normalización avanzada**: Manejar mayúsculas y opcionalmente puntuación  
✅ **Comprensión de diccionarios**: Crear diccionarios con condiciones (opcional)  
✅ **Reutilización de patrones**: Aplicar lo aprendido en ejercicio #1  
✅ **Decisiones de diseño**: Pensar en cómo manejar edge cases

---

🗓️ **Creada:** 2025-11-03  
✅ **Resuelta:** YYYY-MM-DD  
⏱️ **Dificultad percibida:** (fácil / medio / difícil)  
🧠 **Observaciones:**
  - (¿Decidiste limpiar la puntuación o no? ¿Por qué?)
  - (¿Qué fue lo más difícil: el conteo o el filtrado?)
  - (¿Usaste comprensión de diccionarios o loops tradicionales?)