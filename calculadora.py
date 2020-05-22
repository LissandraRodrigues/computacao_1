#Trabalho: Calculadora

# FUNCAO QUE MOSTRA NA TELA O MENU DA CALCULADORA

def menu():

    # Para organizar e enfeitar
    
    print()
    print('-'*50)

    print('MENU')
    print('1. Multiplicacao\n2. Divisao\n3. MMC\n4. MDC\n5. Numero Primos\n6. Sair') 
    
    print('-'*50)
    

# FUNCAO QUE REALIZA A OPERACAO - MULTIPLICACAO

def multiplicacao(numero1, numero2):

    resultado = 0

    # O for ira do numero2 ate 0, em passos -1, assim resultado vai receber numero1, ate o contador ser 0 
    
    for contador in range(numero2, 0, -1):
        resultado += numero1

    # Apos a execucao do for, eh retornado o resultado
        
    return resultado


# FUNCAO QUE REALIZA A OPERACAO - DIVISAO (COM RECURSIVIDADE)

def divisao(numerador, denominador):

    # O if acontece quando o numerador passar a ser menor que o denominador   

    if (numerador < denominador):

        # Resultado recebe 0 e o numerador, em que o numerador ja eh o resto

        resultado = 0, numerador
      
    # O else acontece enquanto o numerador for maior ou igual que o denominador
    
    else:

        # (quociente, resto) recebem o resultado da funcao divisao
        
        (quociente, resto) = divisao(numerador - denominador, denominador)

        resultado = (quociente+1, resto)

    return resultado 


# FUNCAO QUE REALIZA O MMC (MINIMO MULTIPLO COMUM) ENTRE OS NUMEROS INSERIDOS PELO USUARIO

def mmc(numero1, numero2):

    """ Utilizo o algoritmo de Euclides para calcular o MMC
    mmc * mdc = a * b
    Entao:
    mmc = a * b / mdc """
    
    # Clono os valores inseridos nos parametros para duas variaveis 

    auxNumero1 = numero1
    auxNumero2 = numero2

    # Atribuo 'None' a uma variavel, assim o computador nao ira alocar espaco para essa variavel

    resto = None
    
    while(resto != 0):
        resto = auxNumero1 % auxNumero2
        auxNumero1 = auxNumero2
        auxNumero2 = resto
    
    # 'auxNumero1' assume o papel de MDC e o resultado do return sera o MMC

    return ((numero1 * numero2) / auxNumero1)


# FUNCAO QUE IRA REALIZAR O MDC (MAXIMO DIVISOR COMUM) ENTRE OS NUMEROS INSERIDOS PELO USUARIO

def mdc(numero1, numero2):
    
    # Utilizo a  mesma logica do algoritmo de Euclides para calcular o MDC 

    resto = None

    # Como no MDC nao irei precisar dos numeros iniciais do usuario depois, utilizo os proprios no while

    while(resto != 0):
        resto = numero1 % numero2
        numero1 = numero2
        numero2 = resto

    # Apos a conclusao do while, 'numero1' se torna o MDC, assim como o 'auxNumero1' na funcao do MMC
    
    return numero1


# FUNCAO PARA EXIBIR OS NUMEROS PRIMOS EXISTENTES ATE O LIMITE INDICADO PELO USUARIO

def numerosPrimos(numeroLimite):

    # Inicializacao de listas vazias

    numerosPrimos, divisores = [], []

    # Em cada repeticao, contador_2 ira verificar todos os valores de 1 ate contador_1 +1 

    ''' Se o contador_1 for maior ou igual a contador_2, ira acontecer o modulo, de contador_1 com contador_2,
    verificando se o resultado eh zero, se for, a lista divisores recebe contador_2 '''

    for contador_1 in range(2, numeroLimite+1):
        for contador_2 in range(1, contador_1+1): 
        
            if(contador_1 >= contador_2):
                if(contador_1 % contador_2 == 0):
                    divisores += [contador_2]

        ''' Os numeros que ao final dessa repeticao contiverem apenas 2 elementos na lista divisores
        sao adicionados a lista numerosPrimos '''

        if(len(divisores) == 2):
            numerosPrimos += [contador_1]

        # A lista divisores eh esvaziada para comecar outra repeticao

        divisores = []

    # Retorna a lista de numeros primos contidos no intervalo inserido pelo usuario 

    return numerosPrimos


########## PROGRAMA PRINCIPAL ###########

# FUNCAO PRINCIPAL DO PROGRAMA, EH ELA QUE CHAMA TODAS AS OUTRAS FUNCOES

def main():

    # Para enfeitar e organizar o programa
    
    print()
    print('#'*50) 
    print(' '*19, 'Calculadora')  
    print('#'*50)

    print('\nBem vindo ao programa: Calculadora em Python!')

    escolhaUsuario = 0

    ''' Este while determina que o programa sera executado enquanto o usuario nao inserir o numero 6,
    que, no caso, eh a condicao de parada, o Sair '''
        
    while (escolhaUsuario != 6):

        # Mostra o MENU na tela

        menu()

        # Permite o usuario inserir o numero correspondente da operacao matematica desejada
        
        print('\nInsira o numero correspondente a operacao desejada: ', end = '')
        escolhaUsuario = int(input()) 

        # Estrutura condicional que sera executada a partir da escolha do Usuario

        # Condicao executada caso o usuario escolha: 1. Multiplicacao
        
        if (escolhaUsuario == 1):

            # Recebe do usuario os numeros que serao utilizados na multiplicacao
            
            print('\nMultiplicacao!')
            print('Digite o primeiro numero: ', end = '')
            numero1 = int(input())

            print('Digite o segundo numero: ', end = '')
            numero2 = int(input())

            # 'Chamamento' da funcao multiplicacao

            resultado = multiplicacao(numero1, numero2)

            # Mostra na tela o resultado da multiplicacao
            
            print('\n{} x {} = {}'.format(numero1, numero2, resultado))

        # Condicao executada caso o usuario escolha: 2. Divisao

        elif(escolhaUsuario == 2):

            # Recebe do usuario os numeros que serao utilizados na divisao
            
            print('\nDivisao!')
            print('Digite o primeiro numero: ', end = '')
            numero1 = int(input())

            print('Digite o segundo numero: ', end = '')
            numero2 = int(input())

            ''' Verificacao para saber se a conta podera ser executada,
            ja que nao existe divisao quando o denominador eh igual a zero'''
            
            if(numero2 != 0):

                # 'Chamamento' da funcao divisao
                
                resultado = divisao(numero1, numero2)
                quociente, resto = resultado

                # Mostra na tela o resultado da divisao
                
                print('\n{} / {}\nQuociente = {}\nResto = {}'.format(numero1, numero2, quociente, resto))

            else:
                
                print('\nNao existe divisao com zero no denominador!')

        # Condicao executada caso o usuario escolha: 3. MMC
                
        elif(escolhaUsuario == 3):

            # Recebe do usuario os numeros que serao utilizados no MMC
            
            print('\nMinimo Multiplo Comum!')
            print('Digite o primeiro numero: ', end = '')
            numero1 = int(input())

            print('Digite o segundo numero: ', end = '')
            numero2 = int(input())

            # 'Chamamento' da funcao mmc
                
            resultado = mmc(numero1, numero2)

            # Mostra na tela o resultado do MMC
            
            print('\nMMC entre {} e {}: {}'.format(numero1, numero2, resultado))

        # Condicao executada caso o usuario escolha: 4. MDC
            
        elif(escolhaUsuario == 4):

            # Recebe do usuario os numeros que serao utilizados no MDC
            
            print('\nMaximo Divisor Comum!')
            print('Digite o primeiro numero: ', end = '')
            numero1 = int(input())

            print('Digite o segundo numero: ', end = '')
            numero2 = int(input())

            # 'Chamamento' da funcao mdc

            resultado = mdc(numero1, numero2)

            # Mostra na tela o resultado do MDC
            
            print('\nMDC entre {} e {}: {}'.format(numero1, numero2, resultado))

        # Condicao executada caso o usuario escolha: 5. Numeros Primos 

        elif(escolhaUsuario == 5):

            # Recebe do usuario o numero que sera utilizado como limite
            
            print('\nNumeros Primos!')
            print('Insira o limite do intervalo de numeros primos que voce deseja ver: ', end='')
            resposta = int(input())

            # 'Chamamento' da funcao numerosPrimos

            resultado = numerosPrimos(resposta)

            # Mostra na tela os numeros primos 
            
            print('\nNumeros Primos:', resultado)

        # Condicao executada caso o usuario escolha: 6. Sair, que no caso, eh a condicao que encerra o programa
            
        elif(escolhaUsuario == 6):

            # Mostra na tela uma mensagem indicando o encerramento do programa
            
            print('\nObrigada por utilizar a Calculadora Python, volte sempre!')

        # Condicao executada caso o usuario insira algum numero diferente do que foi indicado

        else:

            # Mostra na tela que o usuario digitou um numero invalido
            
            print('\nResposta Invalida')

# Faz o programa principal ser executado

main()
