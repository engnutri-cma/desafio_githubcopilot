# Agora vamos calcular a média de três notas fornecidas na entrada do usuário. Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.

def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3
# Solicitando as notas ao usuário
entrada_nota1 = float(input("Digite a primeira nota: ").strip())
entrada_nota2 = float(input("Digite a segunda nota: ").strip())
entrada_nota3 = float(input("Digite a terceira nota: ").strip())
# Calculando a média
resultado = calcular_media(entrada_nota1, entrada_nota2, entrada_nota3)
# Exibindo o resultado
print(f"A média das notas é: {resultado:.2f}")
