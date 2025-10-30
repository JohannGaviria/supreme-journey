# Supreme Journey: Colección de Katas Diarias en Python

Bienvenido/a a **Supreme Journey**, una colección abierta de retos tipo ***kata*** en Python.
Aquí encontrarás ejercicios diseñados para **practicar programación, algoritmia y resolución de problemas**, ideales para entrevistas técnicas o entrenamiento competitivo.

---

## 🚀 ¿Qué encontrarás aquí?

* 🧩 **Retos originales** de distintos niveles: fácil, medio y difícil
* 💡 **Problemas enfocados** en lógica, estructuras de datos, entrevistas y programación competitiva
* 🧠 Cada reto incluye:

  * Enunciado completo y ejemplos
  * Código base (función vacía)
  * Pruebas automáticas listas para `pytest`
  * Pistas opcionales y objetivos de aprendizaje

---

## 📁 Estructura del repositorio

```
daily-katas/
├── YYYY-MM-DD-nombre-del-reto/
│   ├── problem.md         # Enunciado y contexto del problema
│   ├── solution.py        # Código base (sin solución)
│   └── test_solution.py   # Pruebas automáticas (pytest)
└── ...
```

---

## 🧑‍💻 Cómo usar esta colección

### 🔹 Resolver una kata existente

1. Navega a `daily-katas/` y elige un reto según el tema o dificultad.

2. Lee el enunciado en `problem.md`.

3. Implementa tu solución en `solution.py`.

4. Ejecuta las pruebas con:

  ```bash
  pytest test_solution.py
  ```

5. Si te atoras, consulta la sección **Pistas** (pero intenta resolverlo primero 😉).

---

### 🔹 Crear una nueva kata (opcional)

Si quieres crear tu propio reto, puedes hacerlo fácilmente con el **Makefile**:

```bash
# Crea una nueva kata (te pedirá el nombre por consola)
make new
```

Esto generará automáticamente la estructura base en `daily-katas/`.

Cada nuevo reto debe incluir:

* `problem.md` → descripción y ejemplos
* `solution.py` → función vacía con comentarios
* `test_solution.py` → tests en `pytest`
* Pistas y objetivos de aprendizaje al final del `problem.md`

---

## 🌱 Propósito

Este repositorio busca fomentar la práctica constante y la mejora progresiva en programación.
Además, sirve como un registro personal de aprendizaje, demostrando disciplina y crecimiento técnico.