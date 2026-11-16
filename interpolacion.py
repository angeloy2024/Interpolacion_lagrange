"""
Funciones de interpolacion de Lagrange para "busqueda en la tabla".

Reglas del enunciado:
- Intervalos intermedios: polinomio CUBICO (4 puntos, la incognita queda en el intervalo central).
- Primer y ultimo intervalo: polinomio CUADRATICO (3 puntos).
- Si x esta fuera del rango de la tabla: mensaje de error.
"""


def lagrange(puntos_x, puntos_y, x):
    """
    Evalua el polinomio de Lagrange en x usando los puntos dados.
    Devuelve el valor interpolado y la lista de coeficientes L_i(x).
    Con 3 puntos el polinomio es de grado 2, con 4 puntos es de grado 3.
    """
    n = len(puntos_x)
    coeficientes = []
    resultado = 0.0

    for i in range(n):
        li = 1.0
        for j in range(n):
            if j != i:
                li = li * (x - puntos_x[j]) / (puntos_x[i] - puntos_x[j])
        coeficientes.append(li)
        resultado = resultado + puntos_y[i] * li

    return resultado, coeficientes


def buscar_en_tabla(tabla_x, tabla_y, x):
    """
    1) Busca el intervalo [x_i, x_i+1] donde se encuentra x.
    2) Elige los puntos segun el intervalo:
       - primero o ultimo -> 3 puntos (cuadratico)
       - intermedio       -> 4 puntos (cubico)
    3) Aplica Lagrange.

    Devuelve un diccionario con todos los pasos para mostrarlos en la pagina.
    Lanza ValueError si x esta fuera del rango.
    """
    n = len(tabla_x)

    if n < 3:
        raise ValueError("La tabla debe tener al menos 3 puntos.")

    if x < tabla_x[0] or x > tabla_x[-1]:
        raise ValueError(
            f"El valor x = {x} esta fuera del rango de la tabla "
            f"[{tabla_x[0]}, {tabla_x[-1]}]."
        )

    # Paso 1: ciclo hacia abajo de la tabla hasta encontrar el intervalo
    i = 0
    while i < n - 2 and x > tabla_x[i + 1]:
        i = i + 1
    # ahora x esta en [tabla_x[i], tabla_x[i+1]]

    # Paso 2: elegir los puntos
    if i == 0:
        inicio, fin = 0, 3                # primer intervalo -> cuadratico
        metodo = "Cuadratico (grado 2)"
    elif i == n - 2:
        inicio, fin = n - 3, n            # ultimo intervalo -> cuadratico
        metodo = "Cuadratico (grado 2)"
    else:
        inicio, fin = i - 1, i + 3        # intermedio -> cubico
        metodo = "Cubico (grado 3)"

    puntos_x = tabla_x[inicio:fin]
    puntos_y = tabla_y[inicio:fin]

    # Paso 3: interpolar
    valor, coeficientes = lagrange(puntos_x, puntos_y, x)

    return {
        "x": x,
        "intervalo": (tabla_x[i], tabla_x[i + 1]),
        "metodo": metodo,
        "puntos": list(zip(puntos_x, puntos_y, coeficientes)),
        "valor": valor,
    }
