# Búsqueda en la tabla con polinomios de Lagrange

Aplicación Flask que busca el intervalo donde cae un valor x dentro de una tabla
y lo interpola con Lagrange:

- Intervalos intermedios: polinomio cúbico (4 puntos).
- Primer y último intervalo: polinomio cuadrático (3 puntos).
- Si x está fuera del rango de la tabla muestra un mensaje de error.

Por defecto carga la tabla de prueba f(x) = ln x con x = 1, 2, ..., 10.

## Ejecutar (Windows)

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Abrir http://127.0.0.1:5000 en el navegador.

## Archivos

- `app.py`: rutas de Flask y lectura del formulario.
- `interpolacion.py`: funciones `lagrange` y `buscar_en_tabla`.
- `templates/`: páginas HTML con Jinja2.
- `static/estilos.css`: estilos básicos.
