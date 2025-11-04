def analyze_sales_by_category(sales):
    """
    Agrupa ventas por categoría y calcula el total vendido en cada una.
    
    Args:
        sales: Lista de diccionarios con formato:
               {"product": str, "category": str, "amount": number}
    
    Returns:
        Diccionario con categorías como claves y totales como valores
        Formato: {"category_name": total_amount, ...}
        Si no hay ventas, retorna {}
    
    Ejemplos:
        >>> sales = [
        ...     {"product": "Laptop", "category": "Electronics", "amount": 1200},
        ...     {"product": "Mouse", "category": "Electronics", "amount": 25},
        ... ]
        >>> analyze_sales_by_category(sales)
        {'Electronics': 1225}
        
        >>> analyze_sales_by_category([])
        {}
    """
    # TODO: Implementar la solución
    
    # Paso 1: Crear un diccionario vacío para almacenar los totales
    # category_totals = {}
    
    # Paso 2: Iterar sobre cada venta
    # for sale in sales:
    
    # Paso 3: Extraer la categoría y el monto de la venta actual
    # category = sale["category"]
    # amount = sale["amount"]
    
    # Paso 4: Agregar el monto al total de esa categoría
    # Opción A: Verificación manual
    # if category in category_totals:
    #     category_totals[category] += amount
    # else:
    #     category_totals[category] = amount
    
    # Opción B: Usando .get() (más elegante)
    # category_totals[category] = category_totals.get(category, 0) + amount
    
    # Paso 5: Retornar el diccionario de totales
    
    pass


# DESAFÍO OPCIONAL 1: Calcula el promedio en lugar de la suma
def analyze_sales_average(sales):
    """
    Calcula el promedio de ventas por categoría (más desafiante).
    
    Necesitarás llevar registro tanto de la suma como del conteo.
    """
    # TODO: Implementar (requiere dos diccionarios o uno con tuplas)
    pass


# DESAFÍO OPCIONAL 2: Usa collections.defaultdict
def analyze_sales_with_defaultdict(sales):
    """
    Versión usando defaultdict de collections (más avanzado).
    
    defaultdict te permite no preocuparte por verificar si la clave existe.
    """
    # from collections import defaultdict
    # TODO: Implementar
    pass