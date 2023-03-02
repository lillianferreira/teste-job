#Questão 2
# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

#IMPORTANTE:
#	Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

num = int(input("Informe um número: "))

fib = [0, 1]

while fib[-1] < num:
    fib.append(fib[-1] + fib[-2])

if num in fib:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")

#Explicando o código: primeiro, é solicitado que o usuário informe um número através da função input() e esse valor é armazenado na variável num.
#Em seguida, é criada uma lista fib com os dois primeiros valores da sequência de Fibonacci (0 e 1). Então, é criado um laço while que adiciona novos valores à lista fib até que o último valor da lista seja maior ou igual a num. Isso é feito através da expressão fib[-1] < num, que verifica se o último valor da lista fib é menor que num.
#Por fim, é verificado se o número num pertence à lista fib através do comando if num in fib. Se o número estiver presente na lista, é exibida uma mensagem indicando que ele pertence à sequência de Fibonacci. Caso contrário, é exibida uma mensagem informando que ele não pertence à sequência.



#Questão 3
#Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#	• O menor valor de faturamento ocorrido em um dia do mês;
#	• O maior valor de faturamento ocorrido em um dia do mês;
#	• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#	a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#	b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

# Lê o arquivo JSON
with open("faturamento.json", "r") as file:
    data = json.load(file)

# Obtém o valor de faturamento diário a partir dos dados lidos do arquivo
faturamento_diario = data["faturamento_diario"]

# Calcula o menor e o maior valor de faturamento diário
menor_valor = min(faturamento_diario)
maior_valor = max(faturamento_diario)

# Calcula a média mensal de faturamento, ignorando os dias sem faturamento
faturamento_sem_zeros = [f for f in faturamento_diario if f != 0]
media_mensal = sum(faturamento_sem_zeros) / len(faturamento_sem_zeros)

# Calcula o número de dias em que o valor de faturamento diário foi superior à média mensal
dias_acima_da_media = sum(1 for f in faturamento_sem_zeros if f > media_mensal)

# Imprime os resultados
print(f"Menor valor de faturamento diário: R$ {menor_valor:.2f}")
print(f"Maior valor de faturamento diário: R$ {maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")

#Explicando o código: primeiro, o arquivo JSON é lido e seus dados são armazenados na variável data. Em seguida, o valor de faturamento diário é obtido a partir dos dados lidos do arquivo e armazenado na variável faturamento_diario.
#O menor e o maior valor de faturamento diário são calculados utilizando as funções min() e max(), respectivamente. Já a média mensal de faturamento é calculada utilizando uma lista de compreensão para ignorar os dias sem faturamento (valores iguais a zero) e a função sum() para somar os valores de faturamento. O resultado é dividido pelo número de dias com faturamento (ou seja, o comprimento da lista faturamento_sem_zeros).
#Por fim, o número de dias em que o valor de faturamento diário foi superior à média mensal é calculado utilizando outra lista de compreensão e a função sum().
#Os resultados são impressos na tela utilizando a função print(). É importante lembrar que o arquivo JSON deve estar no mesmo diretório que o arquivo Python. Caso contrário, é necessário fornecer o caminho completo para o arquivo na função open().



#Questão 4
#Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

#	SP – R$67.836,43
#	RJ – R$36.678,66
#	MG – R$29.229,88
#	ES – R$27.165,48
#	Outros – R$19.849,53

#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

# Define o valor de faturamento mensal de cada estado

faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcula o valor total mensal
valor_total = sum(faturamento.values())

# Calcula o percentual de representação de cada estado
percentuais = {estado: (valor / valor_total) * 100 for estado, valor in faturamento.items()}

# Imprime os resultados
for estado, percentual in percentuais.items():
    print(f"{estado} – {percentual:.2f}%")

#Explicando o código: primeiro, o valor de faturamento mensal de cada estado é definido em um dicionário chamado faturamento.
#Em seguida, o valor total mensal é calculado utilizando a função sum() aplicada aos valores do dicionário faturamento.
#Para calcular o percentual de representação de cada estado, é utilizado outro dicionário chamado percentuais. Um laço for percorre os itens do dicionário faturamento, calcula o percentual correspondente a cada valor e armazena no dicionário percentuais utilizando a chave correspondente ao estado.
#Por fim, um novo laço for é utilizado para imprimir os resultados na tela, utilizando a função print(). Os percentuais são formatados para exibir duas casas decimais utilizando a sintaxe :.2f.



#Questão 5
#Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#	a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#	b) Evite usar funções prontas, como, por exemplo, reverse;
# Define a string a ser invertida
texto = "exemplo de string a ser invertida"

# Inicializa uma nova string vazia
texto_invertido = ""

# Percorre a string original de trás para frente
for i in range(len(texto)-1, -1, -1):
    # Adiciona cada caractere na nova string
    texto_invertido += texto[i]

# Imprime a nova string invertida
print(texto_invertido)

#Explicando o código: primeiro, a string a ser invertida é definida na variável texto.
#Em seguida, uma nova string vazia é inicializada na variável texto_invertido.
#O laço for percorre a string original de trás para frente, utilizando a função range() com os parâmetros len(texto)-1 (para começar no último caractere da string), -1 (para chegar até o primeiro caractere) e -1 (para percorrer a string de trás para frente). Em cada iteração do laço, o caractere correspondente é adicionado na nova string utilizando o operador +=.
#Por fim, a nova string invertida é impressa na tela utilizando a função print().
