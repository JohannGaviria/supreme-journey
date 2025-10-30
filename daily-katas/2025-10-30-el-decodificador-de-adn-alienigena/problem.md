# El Decodificador de ADN Alienígena 🧬👽

## Contexto

Has descubierto una antigua civilización alienígena que codificaba mensajes en secuencias de ADN. A diferencia del ADN terrestre (A, T, G, C), el ADN alienígena usa un alfabeto numérico del **1 al 26**, donde cada número representa una letra:

```
1 = A, 2 = B, 3 = C, ..., 26 = Z
```

El problema es que las secuencias no tienen separadores, por lo que una misma cadena puede decodificarse de múltiples maneras:

- `"111"` puede ser: `"AAA"` (1-1-1) o `"KA"` (11-1) o `"AK"` (1-11)
- `"123"` puede ser: `"ABC"` (1-2-3), `"LC"` (12-3), o `"AW"` (1-23)

Tu misión es determinar **cuántas formas diferentes hay de decodificar** una secuencia de ADN alienígena válida.

## Entrada

- `dna_sequence`: String que contiene solo dígitos del 0 al 9
- La secuencia puede contener ceros, pero **un cero nunca puede estar solo** (no hay letra 0)
- Un cero solo puede formar parte de números como 10 o 20

## Salida

- Un entero representando el **número total de decodificaciones posibles**
- Si la secuencia no puede decodificarse (por ejemplo, contiene "00" o comienza con "0"), retorna `0`

## Ejemplos

### Ejemplo 1: Múltiples decodificaciones
```python
dna_sequence = "12"
# Posibles decodificaciones:
# - "AB" (1-2)
# - "L" (12)
Resultado: 2
```

### Ejemplo 2: Con ceros válidos
```python
dna_sequence = "110"
# Posibles decodificaciones:
# - "AJ" (1-10)
# - "KJ" (11-0... no válido, 0 no puede estar solo)
# Solo hay una forma válida: "AJ"
Resultado: 1
```

### Ejemplo 3: Secuencia inválida
```python
dna_sequence = "100"
# El 0 inicial en "00" hace que sea imposible decodificar
Resultado: 0
```

### Ejemplo 4: Secuencia compleja
```python
dna_sequence = "226"
# Posibles decodificaciones:
# - "BBF" (2-2-6)
# - "BZ" (2-26)
# - "VF" (22-6)
Resultado: 3
```

### Ejemplo 5: Una sola forma
```python
dna_sequence = "27"
# Solo puede ser "BG" (2-7)
# No puede ser 27 porque Z = 26
Resultado: 1
```

## Restricciones

- `1 ≤ len(dna_sequence) ≤ 100`
- La secuencia solo contiene dígitos ('0'-'9')
- Tiempo esperado: O(n) donde n es la longitud de la secuencia
- Complejidad espacial esperada: O(n)
- Los números válidos van del 1 al 26

## Reglas de decodificación

✅ **Válido:**
- Números del 1 al 26
- El 0 puede aparecer en números como 10 o 20

❌ **Inválido:**
- El número 0 solo
- Números mayores a 26 (27, 28, ...)
- Secuencias que empiezan con 0
- Doble cero "00"
- Números como 30, 40, ... (el 0 después de 3+ no forma número válido)

## Pistas

💡 **Pista 1**: Este problema tiene subestructura óptima - la respuesta para una posición depende de las respuestas anteriores

💡 **Pista 2**: En cada posición, tienes máximo 2 opciones: tomar 1 dígito o tomar 2 dígitos (si es válido)

💡 **Pista 3**: Piensa en trabajar hacia adelante desde el inicio, o hacia atrás desde el final

💡 **Pista 4**: Memorización (memoization) convertirá una solución exponencial en lineal

💡 **Pista 5**: Los casos con "0" requieren atención especial - un 0 DEBE estar precedido por 1 o 2

## Objetivos que entrena

✅ **Dynamic Programming**: Identificar subestructura óptima y overlapping subproblems  
✅ **Recursión con memorización**: Optimizar soluciones recursivas  
✅ **Validación de estados**: Manejar casos especiales y restricciones  
✅ **Pensamiento inductivo**: Construir la solución a partir de casos más pequeños  
✅ **Manejo de strings**: Slicing y parsing eficiente  
✅ **Edge cases críticos**: Ceros, límites numéricos, secuencias inválidas

---

🗓️ Creada: {{KATA_CREATED}}
✅ Resuelta: YYYY-MM-DD
⏱️ Dificultad percibida: (fácil / medio / difícil)
🧠 Observaciones:
  - (Aquí puedes anotar lo que aprendiste, los errores que cometiste o posibles mejoras)
