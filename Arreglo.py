licenciaturas = ["EFN", "AGR", "TU", "GHT", "CP"]

def imprimir_licenciaturas():
    print("<ul>")
    for licenciatura in licenciaturas:
        print(f"  <li>{licenciatura}</li>")
    print("</ul>")

if __name__ == "__main__":
    imprimir_licenciaturas()