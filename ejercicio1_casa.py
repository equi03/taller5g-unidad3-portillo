from PIL import Image

def dda(pixels, x0, y0, x1, y1, color, ancho, alto):
    """Implementación del algoritmo DDA para trazado de líneas."""
    dx = x1 - x0
    dy = y1 - y0
    pasos = max(abs(dx), abs(dy))
    
    if pasos == 0:
        if 0 <= x0 < ancho and 0 <= y0 < alto:
            pixels[x0, y0] = color
        return

    x_inc = dx / pasos
    y_inc = dy / pasos
    x = x0
    y = y0

    for _ in range(int(pasos) + 1):
        ix, iy = round(x), round(y)
        if 0 <= ix < ancho and 0 <= iy < alto:
            pixels[ix, iy] = color
        x += x_inc
        y += y_inc

def dibujar_rectangulo(pixels, x0, y0, x1, y1, color, ancho, alto):
    """Dibuja un rectángulo usando cuatro llamadas a dda()."""
    dda(pixels, x0, y0, x1, y0, color, ancho, alto)  # Línea superior
    dda(pixels, x1, y0, x1, y1, color, ancho, alto)  # Línea derecha
    dda(pixels, x0, y1, x1, y1, color, ancho, alto)  # Línea inferior
    dda(pixels, x0, y0, x0, y1, color, ancho, alto)  # Línea izquierda

def dibujar_triangulo(pixels, p1, p2, p3, color, ancho, alto):
    """Dibuja un triángulo conectando tres vértices."""
    dda(pixels, p1[0], p1[1], p2[0], p2[1], color, ancho, alto)
    dda(pixels, p2[0], p2[1], p3[0], p3[1], color, ancho, alto)
    dda(pixels, p3[0], p3[1], p1[0], p1[1], color, ancho, alto)

def dibujar_sol(pixels, cx, cy, radio, n_rayos, color, ancho, alto):
    """Dibuja un sol con rayos usando cálculo polar."""
    import math
    # Círculo central aproximado con un punto o pequeño radio (opcional)
    for i in range(n_rayos):
        angulo = 2 * math.pi * i / n_rayos
        x_fin = cx + int(radio * math.cos(angulo))
        y_fin = cy + int(radio * math.sin(angulo))
        dda(pixels, cx, cy, x_fin, y_fin, color, ancho, alto)

# Programa principal
if __name__ == "__main__":
    ancho_lienzo, alto_lienzo = 600, 500
    # Fondo celeste claro para el cielo
    imagen = Image.new("RGB", (ancho_lienzo, alto_lienzo), (200, 230, 255))
    pixels = imagen.load()

    # Colores (RGB)
    COLOR_CASA = (139, 69, 19)      # Marrón para el cuerpo
    COLOR_TECHO = (178, 34, 34)     # Rojo ladrillo para el techo
    COLOR_PUERTA = (85, 26, 139)    # Púrpura oscuro para la puerta
    COLOR_VENTANA = (0, 102, 204)   # Azul para las ventanas
    COLOR_SOL = (255, 215, 0)       # Amarillo dorado para el sol
    COLOR_PISO = (34, 139, 34)      # Verde para el césped/piso

    # 1. Línea de piso horizontal
    for x in range(ancho_lienzo):
        dda(pixels, x, 420, x, 420, COLOR_PISO, ancho_lienzo, alto_lienzo)

    # 2. Cuerpo de la casa (Rectángulo)
    dibujar_rectangulo(pixels, 200, 220, 400, 420, COLOR_CASA, ancho_lienzo, alto_lienzo)

    # 3. Techo de la casa (Triángulo)
    p1 = (300, 120)  # pendicular superior
    p2 = (180, 220)  # Esquina inferior izquierda del techo
    p3 = (420, 220)  # Esquina inferior derecha del techo
    dibujar_triangulo(pixels, (300, 120), (170, 220), (430, 220), COLOR_TECHO, ancho_lienzo, alto_lienzo)

    # 4. Puerta rectangular
    dibujar_rectangulo(pixels, 260, 320, 340, 420, COLOR_PUERTA, ancho_lienzo, alto_lienzo)

    # 5. Dos ventanas cuadradas
    dibujar_rectangulo(pixels, 220, 240, 270, 290, COLOR_VENTANA, ancho_lienzo, alto_lienzo)
    dibujar_rectangulo(pixels, 330, 240, 380, 290, COLOR_VENTANA, ancho_lienzo, alto_lienzo)

    # 6. Sol en la esquina superior
    dibujar_sol(pixels, 520, 80, 40, 12, COLOR_SOL, ancho_lienzo, alto_lienzo)

    # Guardar resultado
    imagen.save("casa.png")
    print("Imagen 'casa.png' generada exitosamente.")