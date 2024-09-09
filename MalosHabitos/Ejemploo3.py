# Función para calcular el área de un rectángulo
def AreaRectangulo(AlturaRectangulo, BaseRectangulo):
    Resultado = AlturaRectangulo * BaseRectangulo
    return Resultado


# Función para calcular el área de un triángulo
def AreaTriangulo(BaseTriangulo, AlturaTriangulo):
    Resultado = 0.5 * BaseTriangulo * AlturaTriangulo
    return Resultado


# Función principal
def Principal():
    BaseRectangulo = float(input("Base del rectangulo: "))
    AlturaRectangulo = float(input("Altura del rectangulo: "))
    RectanguloArea = AreaRectangulo(BaseRectangulo, AlturaRectangulo)
    print(f"{BaseRectangulo} * {AlturaRectangulo} = {RectanguloArea}")

    BaseTriangulo = float(input("Base del triangulo: "))
    AlturaTriangulo = float(input("Base del triangulo: "))
    TrianguloArea = AreaTriangulo(BaseTriangulo, AlturaTriangulo)
    print(f"({BaseTriangulo} * {AlturaTriangulo})/2 = {TrianguloArea}")


if __name__ == "__main__":
    Principal()
