# El Analizador de Ventas por Categoría

## Contexto

Trabajas en un e-commerce y necesitas crear un reporte de ventas. Tienes una lista de transacciones y debes agruparlas por categoría de producto, calculando el total de ventas para cada categoría.

Este es un problema clásico de **agregación y agrupamiento**, fundamental en análisis de datos y muy común en entrevistas técnicas.

Tu función debe:
1. Recibir una lista de ventas (cada una con producto, categoría y monto)
2. Agrupar las ventas por categoría
3. Sumar el total vendido en cada categoría
4. Retornar un diccionario con los totales

## Entrada

- `sales`: Lista de diccionarios, donde cada diccionario representa una venta:
  - `"product"`: String con el nombre del producto
  - `"category"`: String con la categoría del producto
  - `"amount"`: Float o int con el monto de la venta

Ejemplo de entrada:
```python
sales = [
    {"product": "Laptop", "category": "Electronics", "amount": 1200},
    {"product": "Mouse", "category": "Electronics", "amount": 25},
    {"product": "Desk", "category": "Furniture", "amount": 350},
]
```

## Salida

- Un diccionario donde:
  - Las **claves** son las categorías (strings)
  - Los **valores** son los totales de ventas (números)
- Si no hay ventas, retorna un diccionario vacío `{}`
- Los montos deben ser numéricos (int o float)

## Ejemplos

### Ejemplo 1: Agrupamiento básico
```python
# Entrada:
sales = [
    {"product": "Laptop", "category": "Electronics", "amount": 1200},
    {"product": "Mouse", "category": "Electronics", "amount": 25},
    {"product": "Desk", "category": "Furniture", "amount": 350},
]

# Salida esperada:
{
    "Electronics": 1225,  # 1200 + 25
    "Furniture": 350
}
```

### Ejemplo 2: Una sola categoría
```python
# Entrada:
sales = [
    {"product": "Book A", "category": "Books", "amount": 15},
    {"product": "Book B", "category": "Books", "amount": 20},
    {"product": "Book C", "category": "Books", "amount": 10},
]

# Salida esperada:
{
    "Books": 45  # 15 + 20 + 10
}
```

### Ejemplo 3: Lista vacía
```python
# Entrada:
sales = []

# Salida esperada:
{}
```

### Ejemplo 4: Múltiples categorías
```python
# Entrada:
sales = [
    {"product": "Phone", "category": "Electronics", "amount": 800},
    {"product": "Chair", "category": "Furniture", "amount": 150},
    {"product": "Novel", "category": "Books", "amount": 25},
    {"product": "Tablet", "category": "Electronics", "amount": 400},
    {"product": "Table", "category": "Furniture", "amount": 300},
]

# Salida esperada:
{
    "Electronics": 1200,  # 800 + 400
    "Furniture": 450,     # 150 + 300
    "Books": 25
}
```

### Ejemplo 5: Montos decimales
```python
# Entrada:
sales = [
    {"product": "Coffee", "category": "Food", "amount": 4.50},
    {"product": "Sandwich", "category": "Food", "amount": 7.99},
    {"product": "Water", "category": "Drinks", "amount": 1.50},
]

# Salida esperada:
{
    "Food": 12.49,   # 4.50 + 7.99
    "Drinks": 1.50
}
```

## Restricciones

- `0 ≤ len(sales) ≤ 10,000` ventas
- `amount` es siempre un número positivo (int o float)
- `category` y `product` son siempre strings no vacíos
- Las categorías son case-sensitive: "Electronics" ≠ "electronics"
- Tiempo esperado: O(n) donde n es el número de ventas
- No uses librerías externas (solo Python estándar)

## Pistas

💡 **Pista 1**: Piensa en el patrón del ejercicio #1 (contador de vocales), pero sumando en lugar de contar

💡 **Pista 2**: Inicializa un diccionario vacío para almacenar los totales por categoría

💡 **Pista 3**: Por cada venta, verifica si la categoría ya existe en el diccionario

💡 **Pista 4**: Si la categoría existe, suma el monto; si no existe, créala con el monto inicial

💡 **Pista 5**: Puedes usar `.get()` para manejar categorías nuevas: `totals[cat] = totals.get(cat, 0) + amount`

💡 **Pista 6**: Este patrón se llama "reduce" o "fold" en programación funcional

💡 **Pista 7**: Alternativa avanzada: Puedes usar `defaultdict` de la librería `collections` (opcional)

## Objetivos que entrena

✅ **Agrupamiento de datos**: Organizar información por categorías  
✅ **Agregación**: Sumar valores dentro de grupos  
✅ **Patrón acumulador**: Construir resultados iterativamente  
✅ **Manejo de diccionarios dinámicos**: Crear claves sobre la marcha  
✅ **Iteración sobre estructuras complejas**: Procesar listas de diccionarios  
✅ **Pensamiento analítico**: Transformar datos crudos en insights  
✅ **Preparación para SQL/Pandas**: Este es el equivalente de GROUP BY + SUM

---

🗓️ **Creada:** 2025-11-03  
✅ **Resuelta:** YYYY-MM-DD  
⏱️ **Dificultad percibida:** (fácil / medio / difícil)  
🧠 **Observaciones:**
  - (¿Te recordó al ejercicio #1? ¿En qué se parecen?)
  - (¿Usaste .get() o if/else? ¿Cuál te pareció más claro?)
  - (¿Entendiste el concepto de agregación?)
  - (¿Podrías modificar esto para calcular promedios en lugar de sumas?)