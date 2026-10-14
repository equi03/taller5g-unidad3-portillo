# ejercicio2_roseta.py
from PIL import Image
import math

def bresenham(pixels, x0, y0, x1, y1, color, ancho, alto):
    """Implementación del algoritmo de Bresenham para trazado de líneas."""
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    x, y = x0, y0
    while True:
        if 0 <= x < ancho and 0 <= y < alto:
            pixels[x, y] = color
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy

def generar_puntos_circulo(cx, cy, radio, n):
    """Genera una lista de n puntos equiespaciados sobre una circunferencia."""
    puntos = []
    for i in range(n):
        angulo = 2 * math.pi * i / n
        x = cx + int(radio * math.cos(angulo))
        y = cy + int(radio * math.sin(angulo))
        puntos.append((x, y))
    return puntos

def dibujar_roseta(pixels, puntos, ancho, alto):
    """Conecta cada par de puntos de la circunferencia aplicando un gradiente de color."""
    n = len(puntos)
    for i in range(n):
        for j in range(i + 1, n):
            # Gradiente basado en la distancia de separación de los índices o posición
            factor = (i + j) / (2 * n)
            r = int(255 * (1 - factor))
            g = int(100 + 155 * factor)
            b = int(255 * factor)
            color = (r, g, b)
            
            bresenham(pixels, puntos[i][0], puntos[i][1],
                              puntos[j][0], puntos[j][1], color, ancho, alto)

# Generar las tres variantes solicitadas
if __name__ == "__main__":
    ancho_lienzo, alto_lienzo = 700, 700
    
    for n_val in [12, 24, 36]:
        # Fondo negro para Resaltar el efecto luminoso de la roseta
        img = Image.new("RGB", (ancho_lienzo, alto_lienzo), (10, 10, 10))
        pixels = img.load()
        
        # Generar puntos sobre circunferencia centrada en (350, 350) con radio 300
        puntos = generar_puntos_circulo(350, 350, 300, n_val)
        
        # Dibujar roseta
        dibujar_roseta(pixels, puntos, ancho_lienzo, alto_lienzo)
        
        # Guardar variante
        nombre_archivo = f"roseta_{n_val}.png"
        img.save(nombre_archivo)
        print(f"Imagen '{nombre_archivo}' generada correctamente.")