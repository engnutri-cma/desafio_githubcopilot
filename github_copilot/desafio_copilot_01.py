#Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!

def concatenar_dados(dado1, dado2):
    return f"{dado1} {dado2}"
#Solicitando os dados ao usuário
entrada1 = input("Digite o primeiro dado: ").strip().capitalize()
entrada2 = input("Digite o segundo dado: ").strip().capitalize()
#Concatenando os dados
resultado = concatenar_dados(entrada1, entrada2)
#Exibindo o resultado
print("Dados concatenados:", resultado)