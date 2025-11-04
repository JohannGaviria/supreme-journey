import pytest
from solution import analyze_sales_by_category


def test_basic_grouping():
    """Caso básico con dos categorías"""
    sales = [
        {"product": "Laptop", "category": "Electronics", "amount": 1200},
        {"product": "Mouse", "category": "Electronics", "amount": 25},
        {"product": "Desk", "category": "Furniture", "amount": 350},
    ]
    result = analyze_sales_by_category(sales)
    
    assert result == {
        "Electronics": 1225,
        "Furniture": 350
    }


def test_single_category():
    """Todas las ventas de una misma categoría"""
    sales = [
        {"product": "Book A", "category": "Books", "amount": 15},
        {"product": "Book B", "category": "Books", "amount": 20},
        {"product": "Book C", "category": "Books", "amount": 10},
    ]
    result = analyze_sales_by_category(sales)
    
    assert result == {"Books": 45}


def test_empty_list():
    """Lista vacía debe retornar diccionario vacío"""
    result = analyze_sales_by_category([])
    assert result == {}


def test_single_sale():
    """Una sola venta"""
    sales = [{"product": "Phone", "category": "Electronics", "amount": 800}]
    result = analyze_sales_by_category(sales)
    
    assert result == {"Electronics": 800}


def test_multiple_categories():
    """Múltiples categorías con varias ventas cada una"""
    sales = [
        {"product": "Phone", "category": "Electronics", "amount": 800},
        {"product": "Chair", "category": "Furniture", "amount": 150},
        {"product": "Novel", "category": "Books", "amount": 25},
        {"product": "Tablet", "category": "Electronics", "amount": 400},
        {"product": "Table", "category": "Furniture", "amount": 300},
    ]
    result = analyze_sales_by_category(sales)
    
    assert result == {
        "Electronics": 1200,
        "Furniture": 450,
        "Books": 25
    }


def test_decimal_amounts():
    """Montos con decimales"""
    sales = [
        {"product": "Coffee", "category": "Food", "amount": 4.50},
        {"product": "Sandwich", "category": "Food", "amount": 7.99},
        {"product": "Water", "category": "Drinks", "amount": 1.50},
    ]
    result = analyze_sales_by_category(sales)
    
    assert abs(result["Food"] - 12.49) < 0.01  # Comparación con tolerancia
    assert abs(result["Drinks"] - 1.50) < 0.01


def test_large_amounts():
    """Montos grandes"""
    sales = [
        {"product": "Server", "category": "Hardware", "amount": 50000},
        {"product": "Router", "category": "Hardware", "amount": 10000},
    ]
    result = analyze_sales_by_category(sales)
    
    assert result == {"Hardware": 60000}


def test_category_case_sensitive():
    """Las categorías son case-sensitive"""
    sales = [
        {"product": "Item1", "category": "Electronics", "amount": 100},
        {"product": "Item2", "category": "electronics", "amount": 200},
    ]
    result = analyze_sales_by_category(sales)
    
    # Deben ser dos categorías diferentes
    assert result == {
        "Electronics": 100,
        "electronics": 200
    }


def test_return_type():
    """Verificar que retorna un diccionario"""
    sales = [{"product": "Test", "category": "Test", "amount": 10}]
    result = analyze_sales_by_category(sales)
    assert isinstance(result, dict)


def test_all_categories_present():
    """Todas las categorías únicas deben estar en el resultado"""
    sales = [
        {"product": "A", "category": "Cat1", "amount": 10},
        {"product": "B", "category": "Cat2", "amount": 20},
        {"product": "C", "category": "Cat3", "amount": 30},
    ]
    result = analyze_sales_by_category(sales)
    
    assert set(result.keys()) == {"Cat1", "Cat2", "Cat3"}


def test_accumulation_correctness():
    """Verificar que la suma se hace correctamente"""
    sales = [
        {"product": "A", "category": "Test", "amount": 10},
        {"product": "B", "category": "Test", "amount": 20},
        {"product": "C", "category": "Test", "amount": 30},
        {"product": "D", "category": "Test", "amount": 40},
    ]
    result = analyze_sales_by_category(sales)
    
    assert result["Test"] == 100


def test_many_categories():
    """Muchas categorías diferentes"""
    sales = [
        {"product": f"Product{i}", "category": f"Category{i}", "amount": i}
        for i in range(1, 11)
    ]
    result = analyze_sales_by_category(sales)
    
    assert len(result) == 10
    assert result["Category5"] == 5


def test_repeated_products_same_category():
    """El mismo producto vendido múltiples veces"""
    sales = [
        {"product": "Mouse", "category": "Electronics", "amount": 25},
        {"product": "Mouse", "category": "Electronics", "amount": 25},
        {"product": "Mouse", "category": "Electronics", "amount": 25},
    ]
    result = analyze_sales_by_category(sales)
    
    assert result == {"Electronics": 75}


def test_zero_amount():
    """Ventas con monto cero (edge case)"""
    sales = [
        {"product": "Free item", "category": "Promo", "amount": 0},
        {"product": "Paid item", "category": "Promo", "amount": 100},
    ]
    result = analyze_sales_by_category(sales)
    
    assert result == {"Promo": 100}


def test_realistic_scenario():
    """Escenario realista de un e-commerce"""
    sales = [
        {"product": "iPhone 13", "category": "Electronics", "amount": 999},
        {"product": "AirPods", "category": "Electronics", "amount": 199},
        {"product": "Office Chair", "category": "Furniture", "amount": 299},
        {"product": "Standing Desk", "category": "Furniture", "amount": 499},
        {"product": "Python Book", "category": "Books", "amount": 39.99},
        {"product": "LED Monitor", "category": "Electronics", "amount": 349},
        {"product": "Bookshelf", "category": "Furniture", "amount": 89},
    ]
    result = analyze_sales_by_category(sales)
    
    assert result["Electronics"] == 1547
    assert result["Furniture"] == 887
    assert abs(result["Books"] - 39.99) < 0.01


def test_performance_large_dataset():
    """Test de rendimiento con muchas ventas"""
    import time
    
    # Crear 10,000 ventas distribuidas en 50 categorías
    sales = [
        {
            "product": f"Product{i}",
            "category": f"Category{i % 50}",
            "amount": (i % 100) + 1
        }
        for i in range(10000)
    ]
    
    start = time.time()
    result = analyze_sales_by_category(sales)
    elapsed = time.time() - start
    
    # Debe completarse en menos de 0.1 segundos
    assert elapsed < 0.1
    
    # Verificar que se procesaron correctamente
    assert len(result) == 50
    assert isinstance(result, dict)


def test_mixed_int_and_float():
    """Mezcla de enteros y flotantes"""
    sales = [
        {"product": "A", "category": "Mixed", "amount": 10},
        {"product": "B", "category": "Mixed", "amount": 5.5},
        {"product": "C", "category": "Mixed", "amount": 20},
    ]
    result = analyze_sales_by_category(sales)
    
    assert result["Mixed"] == 35.5


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
