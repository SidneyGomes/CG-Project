def put_pixel(x1, x2, img):  # Plotar pixel na tela
    try:
        img.put("#ff0000", (round(x1), round(x2)))
    except Exception:
        pass
