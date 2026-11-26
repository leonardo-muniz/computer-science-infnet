def mult(x, y, nivel=0):
    
    print("  " * nivel + f"mult({x}, {y})")

    if y == 0:  # caso base
        print("  " * nivel + "retorna 0")
        return 0

    resultado = x + mult(x, y - 1, nivel + 1)

    print("  " * nivel + f"retorna {resultado}")
    return resultado


print(mult(4, 3))