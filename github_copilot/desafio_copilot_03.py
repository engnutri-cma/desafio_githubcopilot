#Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

def operar_numeros(num1, num2, operacao):
    if operacao == '1':
        return num1 + num2
    elif operacao == '2':
        return num1 - num2
    elif operacao == '3':
        return num1 * num2
    elif operacao == '4':
        return num1 / num2
    else:
        return None

continuar = 'S'
while continuar.upper() == 'S':
    #Solicitando os dados ao usuário
    entrada_num1 = float(input("Digite o primeiro número: ").strip())
    entrada_num2 = float(input("Digite o segundo número: ").strip())
    
    operacao_valida = False
    while not operacao_valida:
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        entrada_operacao = input("Digite o número da operação (1, 2, 3, 4): ").strip()
        
        #Realizando a operação
        resultado = operar_numeros(entrada_num1, entrada_num2, entrada_operacao)
        
        if resultado is None:
            print("❌ Operação inválida! Tente novamente.\n")
        else:
            operacao_valida = True
            #Exibindo o resultado
            print(f"Resultado da operação: {resultado}\n")
    
    continuar = input("Deseja realizar outra operação? (S/N): ").strip()

print("Programa finalizado!")

