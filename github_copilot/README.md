# 🤖 Desafios Python com GitHub Copilot

Este projeto apresenta uma série de desafios Python desenvolvidos com a assistência do **GitHub Copilot**, demonstrando como essa ferramenta de IA pode acelerar e melhorar o processo de desenvolvimento de código.

## 📋 Descrição do Projeto

O projeto consiste em **6 desafios** que exploram conceitos fundamentais de Python, utilizando o GitHub Copilot para:

- Sugerir implementações
- Corrigir erros
- Melhorar a estrutura do código
- Adicionar validações e tratamento de exceções
- Implementar loops e controle de fluxo

## 🎯 Desafios Realizados

### **Desafio 1: Concatenação de Dados** (`desafio_copilot_01.py`)

- **Objetivo**: Receber dois dados diferentes do usuário e concatená-los em uma única string
- **Implementação com Copilot**:
  - Criação da função de concatenação
  - Formatação com espaço entre as palavras usando f-strings
  - Entrada de dados com validação básica

**Como funciona:**

```
Digite o primeiro dado: João
Digite o segundo dado: Silva
Dados concatenados: João Silva
```

---

### **Desafio 2: Repetição de String** (`desafio_copilot_02.py`)

- **Objetivo**: Receber uma string e um número inteiro, repetindo a string o número de vezes informado
- **Implementação com Copilot**:
  - Função de repetição de string
  - Separação das repetições com hífen usando `.join()`
  - Tratamento de entrada do usuário

**Como funciona:**

```
Digite uma string: Hello
Digite um número inteiro: 3
String repetida: Hello-Hello-Hello
```

---

### **Desafio 3: Calculadora Simples** (`desafio_copilot_03.py`)

- **Objetivo**: Realizar operações matemáticas simples entre dois números
- **Implementação com Copilot**:
  - Menu numérico para operações (evitando erros de digitação)
  - Validação de operação inválida com looping
  - Sistema de repetição para múltiplas operações
  - Pergunta para continuar ou sair

**Operações disponíveis:**

- `1` - Soma
- `2` - Subtração
- `3` - Multiplicação
- `4` - Divisão

**Como funciona:**

```
Digite o primeiro número: 10
Digite o segundo número: 5
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
Digite o número da operação (1, 2, 3, 4): 1
Resultado da operação: 15.0

Deseja realizar outra operação? (S/N): N
Programa finalizado!
```

---

### **Desafio 4: Verificar Par ou Ímpar** (`desafio_copilot_04.py`)

- **Objetivo**: Receber um número inteiro e verificar se ele é par ou ímpar
- **Implementação com Copilot**:
  - Uso de operador módulo (%)
  - Estrutura condicional simples
  - Otimização de código com IA

**Como funciona:**

```
Digite um número inteiro: 7
O número 7 é ímpar.
```

---

### **Desafio 5: Cálculo de Média** (`desafio_copilot_05.py`)

- **Objetivo**: Calcular a média de três notas fornecidas pelo usuário
- **Implementação com Copilot**:
  - Função de cálculo de média
  - Operadores aritméticos
  - Formatação de resultado com 2 casas decimais

**Como funciona:**

```
Digite a primeira nota: 7.5
Digite a segunda nota: 8.0
Digite a terceira nota: 9.5
A média das notas é: 8.33
```

---

### **Desafio 6: Verificar Palíndromo** (`desafio_copilot_06.py`)

- **Objetivo**: Verificar se uma palavra é um palíndromo
- **Implementação com Copilot**:
  - Manipulação de strings com slicing (`[::-1]`)
  - Comparação case-insensitive com `.lower()`
  - Explicação clara do conceito de palíndromo

**O que é Palíndromo?**
Uma palavra, número ou frase que se lê da mesma forma nos dois sentidos, ou seja, quando invertida permanece igual.

**Exemplos:** "ama", "radar", "rotor", "arara"

**Como funciona:**

```
Digite uma palavra: radar
A palavra 'radar' é um palíndromo.
```

---

## 🚀 Como Usar o GitHub Copilot

### **Recursos Utilizados:**

1. **Autocompletar de Código**: Sugestões inteligentes enquanto digitava
2. **Geração de Funções**: Criação automática de funções baseada em comentários
3. **Refatoração**: Melhorias na estrutura e legibilidade do código
4. **Tratamento de Erros**: Adição de validações e loops de repetição
5. **Formatação de Strings**: Sugestões de uso de f-strings e `.join()`

### **Boas Práticas Aplicadas:**

- Uso de comentários descritivos para guiar o Copilot
- Nomes de variáveis e funções claros e em português
- Formatação consistente do código
- Validação de entrada do usuário
- Loops para controle de fluxo

---

## 📁 Estrutura do Projeto

```
github_copilot/
├── desafio_copilot_01.py    # Concatenação de dados
├── desafio_copilot_02.py    # Repetição de string
├── desafio_copilot_03.py    # Calculadora simples
├── desafio_copilot_04.py    # Verificar par ou ímpar
├── desafio_copilot_05.py    # Cálculo de média
├── desafio_copilot_06.py    # Verificar palíndromo
└── README.md                # Este arquivo
```

---

## 🔧 Requisitos

- **Python 3.6+**
- **GitHub Copilot** instalado no VS Code (opcional para execução, necessário para desenvolvimento)

---

## ▶️ Como Executar

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/github_copilot.git
cd github_copilot
```

2. **Execute os scripts:**

```bash
# Desafio 1
python desafio_copilot_01.py

# Desafio 2
python desafio_copilot_02.py

# Desafio 3
python desafio_copilot_03.py

# Desafio 4
python desafio_copilot_04.py

# Desafio 5
python desafio_copilot_05.py

# Desafio 6
python desafio_copilot_06.py
```

---

## 💡 Aprendizados com GitHub Copilot

### ✅ Vantagens Observadas:

- **Produtividade**: Redução significativa no tempo de codificação
- **Sugestões Precisas**: O Copilot forneceu soluções relevantes e idiomáticas
- **Aprendizado**: Vendo diferentes formas de resolver o mesmo problema
- **Menos Erros**: Validações e tratamento de exceções foram sugeridos automaticamente
- **Código Limpo**: Formatação e estrutura melhoradas automaticamente

### ⚠️ Limitações Encontradas:

- Necessidade de validação manual do código gerado
- Contexto limitado em projetos muito grandes
- Requer comentários bem descritos para melhores resultados

---

## 🎓 Conceitos Python Explorados

- ✅ Variáveis e tipos de dados
- ✅ Funções e return
- ✅ Entrada de dados com `input()`
- ✅ Concatenação e formatação de strings
- ✅ Operações matemáticas (soma, subtração, multiplicação, divisão)
- ✅ Estruturas de controle (`if`, `elif`, `else`)
- ✅ Loops (`while`)
- ✅ Validação de entrada
- ✅ F-strings para formatação
- ✅ Método `.join()` para strings
- ✅ Operador módulo (%)
- ✅ Slicing de strings (`[::-1]`)
- ✅ Método `.lower()` para normalização
- ✅ Formatação de números com casas decimais (`.2f`)

---

## 📚 Recursos Úteis

- [Documentação do GitHub Copilot](https://docs.github.com/en/copilot)
- [Python Official Documentation](https://docs.python.org/3/)
- [VS Code Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

---

## 👨‍💻 Autor

Desenvolvido com o auxílio do **GitHub Copilot** durante o Bootcamp Backend Python.

---

## 📄 Licença

Este projeto é fornecido como material educacional. Sinta-se livre para usar, modificar e distribuir conforme necessário.

---

## 🤝 Contribuições

Sugestões de melhorias são bem-vindas! Abra uma issue ou faça um pull request.

---

**⭐ Se este projeto foi útil, considere dar uma estrela!**
