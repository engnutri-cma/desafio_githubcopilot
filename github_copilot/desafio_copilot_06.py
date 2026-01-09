#Vamos testar se uma palavra é um palíndromo?!
# 
# PALÍNDROMO: Uma palavra, número ou frase que se lê da mesma forma nos dois sentidos,
# ou seja, quando invertida permanece igual. Exemplos: "ama", "radar", "rotor", "arara"
# Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

def verificar_palindromo(palavra):
    palavra_invertida = palavra[::-1]
    return palavra.lower() == palavra_invertida.lower()
#Solicitando a palavra ao usuário
entrada_palavra = input("Digite uma palavra: ").strip()
#Verificando se é palíndromo
if verificar_palindromo(entrada_palavra):
    print(f"A palavra '{entrada_palavra}' é um palíndromo.")
else:
    print(f"A palavra '{entrada_palavra}' não é um palíndromo.")