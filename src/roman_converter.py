### Enzo Agustín Aguirre Polenta (@EnzoAguirre04).
### Computacion I - Trabajo práctico N°1.
### Inicio del código.


def decimal_to_roman(n):
    if not (1 <= n <= 3999):
        raise ValueError("El número debe estar entre 1 y 3999")

    val = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    result = ""
    for (arabic, roman) in val:
        while n >= arabic:
            result += roman
            n -= arabic

    return result


if __name__ == "__main__":
    print("Conversor de Números Decimales a Números Romanos entre 1 y 3999. Ingresá 'fin' para finalizar el programa.")

    while True:
        entrada = input("Ingresá un número decimal: ").strip().lower()

        if entrada in ["fin", "'fin'", "fin'", "'fin"]:
            print("Fin del programa.")
            break

        if entrada == "":
            print("No ingresaste ningún valor. Intentá nuevamente.")
            continue

        if not entrada.isdigit():
            print("Entrada inválida. Por favor, ingresá solo números enteros positivos entre 1 y 3999.")
            continue

        numero = int(entrada)

        try:
            romano = decimal_to_roman(numero)
            print(f"{numero} en números romanos equivale a: {romano}")
        except ValueError as e:
            print(f"Error: {e}")


### Fin del código.