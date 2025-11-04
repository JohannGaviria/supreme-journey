# El Contador de Vocales Especial

## Contexto

Estás desarrollando un analizador de texto para un proyecto de procesamiento de lenguaje natural. La primera funcionalidad que necesitas implementar es un contador de vocales que no solo cuente cuántas vocales hay, sino que te diga **cuántas veces aparece cada vocal específica** en un texto.

A diferencia de un contador simple, tu función debe:
- Distinguir entre mayúsculas y minúsculas (tratarlas como iguales)
- Contar solo las vocales en español: a, e, i, o, u
- Ignorar vocales con tildes (á, é, í, ó, ú) para esta versión básica
- Retornar un diccionario con el conteo de cada vocal

## Entrada

- `text`: String que puede contener letras, números, espacios y símbolos
- Puede ser una cadena vacía
- Puede contener mayúsculas y minúsculas mezcladas

## Salida

- Un diccionario con las vocales como claves ('a', 'e', 'i', 'o', 'u')
- Los valores son enteros representando cuántas veces aparece cada vocal
- **Importante**: Todas las vocales deben aparecer en el diccionario, incluso si su conteo es 0

## Ejemplos

### Ejemplo 1: Texto simple
```python
# Entrada:
text = "Hola Mundo"

# Salida esperada:
{'a': 1, 'e': 0, 'i': 0, 'o': 2, 'u': 1}
```

### Ejemplo 2: Sin vocales
```python
# Entrada:
text = "xyz"

# Salida esperada:
{'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
```

### Ejemplo 3: Solo vocales
```python
# Entrada:
text = "AeIoU"

# Salida esperada:
{'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
```

### Ejemplo 4: Con números y símbolos
```python
# Entrada:
text = "Python3.11 es genial!"

# Salida esperada:
{'a': 1, 'e': 2, 'i': 1, 'o': 1, 'u': 0}
```

## Restricciones

- `0 ≤ len(text) ≤ 10,000` caracteres
- El texto puede contener cualquier carácter ASCII
- Tiempo esperado: O(n) donde n es la longitud del texto
- No uses librerías externas (solo Python estándar)

## Pistas

💡 **Pista 1**: Puedes inicializar un diccionario con todas las vocales en 0 desde el principio

💡 **Pista 2**: El método `.lower()` te ayudará a manejar mayúsculas y minúsculas

💡 **Pista 3**: Recorre el texto carácter por carácter con un `for` simple

💡 **Pista 4**: Verifica si cada carácter está en tu conjunto de vocales antes de contarlo

💡 **Pista 5**: Puedes usar el operador `in` para verificar pertenencia: `if char in 'aeiou':`

## Objetivos que entrena

✅ **Iteración sobre strings**: Recorrer caracteres uno por uno  
✅ **Uso de diccionarios**: Crear, inicializar y actualizar diccionarios  
✅ **Normalización de datos**: Convertir a minúsculas para comparación  
✅ **Conteo y acumulación**: Patrón fundamental en programación  
✅ **Manejo de casos edge**: Strings vacíos, sin vocales, etc.  
✅ **Complejidad O(n)**: Entender soluciones lineales eficientes

---

🗓️ **Creada:** 2025-11-03  
✅ **Resuelta:** YYYY-MM-DD
⏱️ **Dificultad percibida:** (fácil / medio / difícil)  
🧠 **Observaciones:**
