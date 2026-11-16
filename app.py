import math
from flask import Flask, render_template, request

from interpolacion import buscar_en_tabla

app = Flask(__name__)

# Tabla de prueba del enunciado: f(x) = ln x con x = 1, 2, ..., 10
TABLA_X_DEFECTO = ", ".join(str(i) for i in range(1, 11))
TABLA_Y_DEFECTO = ", ".join(f"{math.log(i):.6f}" for i in range(1, 11))


def leer_lista(texto):
    """Convierte '1, 2, 3' en [1.0, 2.0, 3.0]."""
    return [float(v) for v in texto.replace(";", ",").split(",") if v.strip()]


@app.route("/", methods=["GET", "POST"])
def index():
    datos = {
        "tabla_x": TABLA_X_DEFECTO,
        "tabla_y": TABLA_Y_DEFECTO,
        "x": "",
        "comparar_ln": True,
    }
    resultado = None
    error = None

    if request.method == "POST":
        datos["tabla_x"] = request.form.get("tabla_x", "")
        datos["tabla_y"] = request.form.get("tabla_y", "")
        datos["x"] = request.form.get("x", "")
        datos["comparar_ln"] = request.form.get("comparar_ln") == "on"

        try:
            tabla_x = leer_lista(datos["tabla_x"])
            tabla_y = leer_lista(datos["tabla_y"])
            x = float(datos["x"])

            if len(tabla_x) != len(tabla_y):
                raise ValueError("Las listas de x y f(x) deben tener la misma cantidad de valores.")
            if tabla_x != sorted(tabla_x):
                raise ValueError("Los valores de x deben estar en orden creciente.")

            resultado = buscar_en_tabla(tabla_x, tabla_y, x)

            # Comparacion con el valor real de ln(x) (solo para la prueba del enunciado)
            if datos["comparar_ln"] and x > 0:
                real = math.log(x)
                resultado["real"] = real
                resultado["error_abs"] = abs(real - resultado["valor"])
                if real != 0:
                    resultado["error_rel"] = abs(real - resultado["valor"]) / abs(real) * 100

        except ValueError as e:
            mensaje = str(e)
            if "could not convert" in mensaje:
                mensaje = "Revisa los datos: solo se permiten numeros separados por comas."
            error = mensaje

    return render_template("index.html", datos=datos, resultado=resultado, error=error)


if __name__ == "__main__":
    app.run(debug=True)
