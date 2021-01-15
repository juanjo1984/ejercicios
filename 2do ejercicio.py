from fechaJuanJose import Fecha

def main():
    f = Fecha(29,9,2020)
    print(f.corta())
    print(f.larga())
    print(f.esbisiesto())
    print(f.diasMes())
    print(f.diaSemana())  


if __name__ == "__main__":
    main()