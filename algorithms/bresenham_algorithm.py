def bresenham_algorithm(
    x_inicial: int, y_inicial: int, x_final: int, y_final: int
) -> list:
    """
    Bresenham's line algorithm implementation.
    """

    points = []

    dx = abs(x_final - x_inicial)
    dy = abs(y_final - y_inicial)
    x_atual, y_atual = x_inicial, y_inicial

    d_inicial = 2 * dy - dx

    incremento_east = 2 * dy
    incremento_northeast = 2 * (dy - dx)

    points.append((x_atual, y_atual))

    while x_atual < x_final:
        if d_inicial <= 0:
            d_inicial += incremento_east
            x_atual += 1
        else:
            d_inicial += incremento_northeast
            x_atual += 1
            y_atual += 1

        points.append((x_atual, y_atual))

    return points


if __name__ == "__main__":
    # Use the Bresenham algorithm to get the points for a line
    initial_point = (1, 1)
    final_point = (8, 5)

    points = bresenham_algorithm(*initial_point, *final_point)
    print(points)
