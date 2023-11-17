def calcular_media(notas):
    return sum(notas) / len(notas)

def calcular_conceito(media):
    if 9 <= media <= 10:
        return 'A'
    elif 7.5 <= media < 9:
        return 'B'
    elif 6 <= media < 7.5:
        return 'C'
    elif 4 <= media < 6:
        return 'D'
    else:
        return 'F'

def main():
    try:
        num_notas = int(input("Quantas notas você deseja calcular? "))
        notas = []

        for i in range(num_notas):
            nota = float(input(f"Digite a nota {i + 1}: "))
            notas.append(nota)

        media = calcular_media(notas)
        conceito = calcular_conceito(media)

        print("\nResultado:")
        print(f"Média: {media:.2f}")
        print(f"Conceito: {conceito}")

    except ValueError:
        print("Por favor, insira notas válidas.")

if __name__ == "__main__":
    main()
