def Calcular(Multiplicando, Multiplicador, Sumando):
    Resultado = Multiplicando * Multiplicador + Sumando
    return Resultado


def Principal():
    Multiplicando = float(input("Multiplicando: "))
    Multiplicador = float(input("Multiplicador: "))
    Sumando = float(input("Sumando: "))
    Resultado = Calcular(Multiplicando, Multiplicador, Sumando)
    print(f"{Multiplicando} * {Multiplicador} + {Sumando} = {Resultado}")


if __name__ == "__main__":
    Principal()
