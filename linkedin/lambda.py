"""
    Funções Lambda
Pequenas funções anônimas
Podem ser passadas como argumento quando você precisar
Tipicamente usadas localmente
Definidas assim:
    lambda(parâmetros):(expressão)
"""


def celsius_para_fahrenheit(temp):
    return (temp * 9/5) + 32


def fahrenheit_para_celsius(temp):
    return (temp - 32) * 5/9


def main():
    temp_em_c = [0, 12, 34, 100]
    temp_em_f = [32, 65, 100, 212]

    print(list(map(fahrenheit_para_celsius, temp_em_f)))
    print(list(map(celsius_para_fahrenheit, temp_em_c)))

    print(list(map(lambda t: (t-32) * 5/9, temp_em_f)))
    print(list(map(lambda t: (t * 9/5) + 32, temp_em_c)))


if __name__ == "__main__":
    main()