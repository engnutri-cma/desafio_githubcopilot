#Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

def repetir_string(string, vezes):
    return '-'.join([string] * vezes)
#Solicitando os dados ao usuário
entrada_string = input("Digite uma string: ").strip().capitalize() 
entrada_numero = int(input("Digite um número inteiro: ").strip())
#Repetindo a string
resultado = repetir_string(entrada_string, entrada_numero)
#Exibindo o resultado
print("String repetida:", resultado)
