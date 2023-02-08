
'''
Tipos de variáveis, propriedades de cada tipo, operações e operadores. 
Apresenta o conceito de programa no tempo e uma técnica simples de rastreamento. 
Entrada de dados pelo teclado, conversão de tipos de dados e erros comuns.

Nomes de Variáveis
    Devem sempre iniciar com uma letra, mas podem conter números e o simbolo de sublinhar.
    A linguagem de Python 3 permite o uso de acentos na variável. 
    As variáveis tem outra propriedade conhecida como o tipo que define a natureza dos dados, 
    e os mais comuns são: inteiros, strings e pontos flutuantes. 
    Além de poder armazenar números e letras, também pode armazenar valores como VERDADEIRO OU FALSO. 

Variáveis Numéricas
    É quando armazena dados de números inteiros ou ponto flutuante. 
Variáveis do Tipo Lógico
    É quando queremos armazenar valores do tipo lógico: VERDADEIRO OU FALSO. 
    T e F são maiúsculos: True or False

Operadores Relacionais
    Servem para realizar comparações lógicas como: 
    igualdade, maior que, menor que, diferente, maior ou igual e menor e igual. 
'''

nota = 8 
média = 7
aprovado = nota > média
print(aprovado)
print(type(aprovado))

'''
Operadores Lógicos
    São compostos por três operadores básicos: not, and e or
    A tabela verdade demonstra o resultado de um operação com um ou dois valores lógicos ou operandos.
    Quando utiliza apenas um operando, dizemos que é um operador unitário. 
    Quando utiliza dois operandos, é chamado de operador binário.
    O operador not é um operador unitário e o or e and são operadores binários. 

Operador not
    É o mais simples, pois precisa apenas de um operador.
    Também chamado de inversão, pois um valor verdadeiro negado, se torna falso e vice-versa.

Operador and
    Resulta em verdadeiro apenas quando dois operadores forem verdadeiros. 
    V + V = Verdadeiro
    V + F = Falso
    F + V = Falso
    F + F = Falso

Operador or
    Resulta em falso se apenas seus dois operadores forem falsos. 
    V + V = Verdadeiro
    V + F = Verdadeiro
    F + V = Verdadeiro
    F + F = Falso

Expressões Lógicas
    Os operadores lógicos podem ser combinados em expressões lógicas mais complexas. 
    Quando uma expressão tiver mais de um operador lógico, 
    avalia-se primeiro o operador not, seguido do operador and, e 
    finalmente, or. 

True or False and not True
True or False and False
True or False
True

Obs.: Os operadores relacionais também podem ser utilizados em expressões com operadores lógicos. 
    Salário > 1000 and idade > 18
Nesses casos, os operadores relacionais devem ser avaliados primeiramente. 

salario = 100
idade = 20
    salario > 1000 and idade > 18
    100 > 1000 and 20 > 18
    False and True
    False

Variáveis string
    São responsáveis por armazenar cadeias de caracteres como nomes e textos em geral.
    Chamamos de cadeira de caracteres uma sequência de símbolos como letras, números e sinais de pontuação.
    Utilizamos aspas para delimitar o início e o fim da sequência. 
    O tamanho de uma string pode ser obtido utilizando a função len.
    Essa função retorna o número de caracteres na string. 
    Se a string é vazia será representada por "". 

print(len('Samuel Cleyton Macena de Oliveira'))
retornar: 33 caracteres - a função lê a quantidade de caracteres. 

    Sabendo que uma string tem um determinado tamanho, podemos acessar seus caracteres
    utilizando um número inteiro para representar sua posição.
    Esse número é chamado de índice, e começamos a contar de zero.
    Isso quer dizer que o primeiro caractere da string é de posição ou índice 0.
    Para acessar os caracteres de uma string, devemos informar o índice ou posição
    do caractere entre colchetes.
    Logo se a string contiver 9 caracteres, poderemos acessar os caracteres de 0 a 8.
    Se tentarmos acessar um índice maior que a quantidade de caracteres, o interpretador
    emitirá uma mensagem de erro.

Manipulação de strings no interpretador
a = "ABCDEF"
print(a[0])
A

Operações com strings
    As variáveis de tipo string suportam operações como fatiamento, concatenação e composição.
    Por fatiamento, podemos enteder a capacidade de utilizar apenas uma parte da string, ou uma fatia.
    A concatenação nada mais é que poder juntar duas ou mais strings em uma string maior. 
    A composição é muito utilizada em mensagens que enviamos à tela e consiste em utilizar strings
    como modelo onde podemos inserir outras strings. 

Concatenação
    As variáveis strings podem ser somados, ou melhor, concatenados. 
    Para concatenar duas strings, utilizamos o operador de adição +.
    Assim "AB" + "C" é igual a "ABC".
    Um caso especial é a repetição de uma string várias vezes.
    Para isso, utilizamos o operado de multiplicação *:
    "A" * 3 é igual a "AAA".

S = "ABC"
>>> print (s + "C")
ABCC

Composição
    Juntar várias string para construir uma mensagem nem sempre é prático. 
    Por exemplo, exibir que "João tem X anos", onde X é uma variável numérica. 
    "João tem %d anos" % X
    O símbolo de % foi utilizado para indicar a composição da string anterior com
    o conteúdo da variável X.
    O %d dentro da primeira string é o que chamamos de marcador de posição.
    O marcador indica que naquela posição estaremos colocando um valor inteiro, daí o %d.

%d para números inteiros
%s para strings
%f para números decimais

Nesse caso, estamos querendo apresentar um número com três posições, completando com o zeros
à esquerda se o número for menor. Podemos realizar essa operação utilizando "%03d" % X. 
Se você precisar apenas que o número ocupe três posições, mas não desejar zeros à esquerda,
basta retirar o zero e utilizar "%3d" % X.

Exemplos de Composições com marcadores: 

>>> idade = 22
print("[%d]" % idade)
[22]

print("[%03d]" % idade)
[022]

print("[%3d]" % idade)
[ 22]

print("[%-3d]" % idade)
[22 ]

Quando formatamos números decimais, podemos utilizar dois valores entre o símbolo de % e a letra f.
O primeiro indica o tamanho total em caracteres a reservar;
E o segundo, o número de casas decimais. 

Exemplos de composição com números decimais

>>> print("%5f" % 5)
5.000000

print("%5.2f" % 5)
5.00

print("%10.5f" % 5)
5.00000

O poder da composição realmente aparece quando precisamos combinar valores em uma nova string.
Imagine que João tem 22 anos e apenas R$ 51,34 no bolso.
Para exibir essa mensagem, podemos utilizar:

"%s tem %d anos e apenas R$%5.2f no bolso" % ("João", 22, 51.34)

Variáveis e entrada de dados
    Python suporta diversas operações com marcadores. 
    Quando temos mais de um marcador na string, somos obrigados a escrever os valores 
    a substituir em parênteses. 

Exemplo de composição string

>>> nome = "João"
>>> idade = 22
>>> grana = 51.34

>>> print("%s tem %d anos e R$%f no bolso." % (nome, idade, grana))
João tem 22 anos e R$51.340000 no bolso.

>>> print("%12s tem %3d anos e R$%5.2f no bolso." % (nome, idade, grana))
 João tem  22 anos e R$51.34 no bolso.

>>> print("%12s tem %03d anos e R$%5.2f no bolso." % (nome, idade, grana))
 João tem 022 anos e R$51.34 no bolso.

>>> print("%-12s tem %-3d anos e R$%-5.2f no bolso." % (nome, idade, grana))
João     tem 22  anos e R$51.34 no bolso.

Fatiamento
    O fatiamento funciona com a utilização de dois pontos no índice da string.
    O número à esquerda dos dois pontos indica a posição de início da fatia;
    E o à direita, do fim.
    O final da fatia não é incluído na mesma. 
    [0:2] como a fatia de caracteres na posição 0 até a posição 2, sem incluí-la.

>>> s = "ABCDEFGHI"
print(s[0:2])
AB

print(s[1:2])
B

print(s[2:4])
CD

print(s[0:5])
ABCDE

print(s[1:8])
BCDEFGH

Podemos emitir também o número da esquerda ou da direita para representar o início ou o final.
Assim, [:2] indica do início até o segundo caractere e [1:] indica do caractere 1 até o final da string.
Podemos também utilizar valores negativos para indicar posições a partir da direita.
Assim -1 é o último caractere; -2 o penúltimo; e assim por diante.

Sequências e tempo
    Um programa é executado linha por linha pelo computador.
    Quando trabalhamos com variáveis, devemos nos lembrar que o conteúdo da variável pode mudar com o tempo.
    Isso porque cada vez que alteramos o valor de uma variável, o valor anterior é substituído pelo novo.

Rastreamento
    Uma das principais diferenças entre ler um texto e um programa é justamente seguir as mudanças de valores
    de cada variável conforme o programa é executado. 
    Um programa deve ser cuidadosamente analisado linha por linha.
    Para programar corretamente, você deve ser capaz de entender o que cada linha do programa significa
    e os efeitos que produz.
    O rastreamento é feito linha a linha, do início ao fim do programa. 
    Se você encontrar um erro, parar o rastreamento e corrigi-lo, mas lembre-se de recomeçar novamente.
    Dominar o rastreamento de um programa é essencial para programar e 
    ajuda muito a entender como os programas realmente funcionam. 

Entrada de Dados
    Chamamos de entrada de dados o momento em que seu programa recebe dados ou valores por um dispositivo. 
    A função input é utilizada para solicitar dados do usuário. 

x = input('Digite um número: ')
print(x)

Conversão da entrada de dados
    A função input retonar valores do tipo string, não se importa se digitamos apenas números, 
    o resultado sempre é string.
    Para resolver esse problema podemos classificar a função como int ou float. 

anos = int(input('Anos de serviço: '))

Erros Comuns
    A entrada de dados é um ponto frágil em nossos programas.
    Como não temos como prever o que o usuário vai digitar, temos que nos preparar para os erros mais conuns.

Erro de conversão: letras no lugar de números
    > ValueError
Erro de conversão: vírgula no lugar de ponto 
    > ValueError



























































































'''



















































