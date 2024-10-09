try:
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite a sua altura em metros: "))

    imc = peso / (altura ** 2)

    print(f"\nSeu IMC é: {imc:.2f}")

    if imc < 18.5:
        print("Diagnóstico: Abaixo do peso")
    elif 18.5 <= imc < 24.9:
        print("Diagnóstico: Peso normal")
    elif 25 <= imc < 29.9:
        print("Diagnóstico: Sobrepeso")
    elif 30 <= imc < 34.9:
        print("Diagnóstico: Obesidade Grau I")
    elif 35 <= imc < 39.9:
        print("Diagnóstico: Obesidade Grau II")
    else:
        print("Diagnóstico: Obesidade Grau III")

except ValueError:
    print("Por favor, insira valores numéricos válidos.")
