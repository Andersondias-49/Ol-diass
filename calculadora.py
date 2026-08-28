from time import sleep
def divisor():
    print('-'*30)


def divisao(a,b):
    print(f'{verde}{a:g} / {b:g} = {a / b:g}{reset}')


def multiplicacao(a,b):
    print(f'{verde}{a:g} x {b:g} = {a * b:g}{reset}')


def adicao(a,b):
    print(f'{verde}{a:g} + {b:g} = {a + b:g}{reset}')



def subtracao(a,b):
    print(f'{verde}{a:g} - {b:g} = {a - b:g}{reset}')


divisor()
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[36m'
reset = '\033[m'
vermelho = '\033[31m'
print(f'CALCULADORA DIASS'.center(30))
divisor()
sleep(1)
while True:
    print(f'{azul}1 - Multiplicação\n'
          '2 - Divisão\n'
          '3 - Adição\n'
          '4 - Subtração\n'
          f'5 - Sair do programa{reset}')
    divisor()
    escolha = int(input('Qual sua escolha? '))
    if escolha == 5:
        break
    elif escolha not in range(1,6):
        sleep(1)
        print('\033[31mERRO! DIGITE UM NÚMERO DE 1 A 5\033[m')
        continue
    while True:
        try:
            n1 = float(input(f'{amarelo}Digite um número:{reset} '))
            break
        except ValueError:
            print(f'{vermelho}ERRO! DIGITE APENAS NÚMEROS{reset}')
    while True:
        try:
            n2 = float(input(f'digite outro número:{reset} '))
            break
        except ValueError:
            print(f'{vermelho}ERRO! DIGITE APENAS NÚMEROS{reset}')
    print(f'{azul}Calculando...{reset}')
    sleep(2)
    if escolha == 1:
        sleep(1)
        multiplicacao(n1,n2)
        sleep(3)
    elif escolha == 2:
        sleep(1)
        divisao(n1,n2)
        sleep(3)
    elif escolha == 3:
        sleep(1)
        adicao(n1,n2)
        sleep(3)
    elif escolha == 4:
        sleep(1)
        subtracao(n1,n2)
        sleep(3)
sleep(1)
divisor()
print('VOLTE SEMPRE!'.center(30))
divisor()
print(f'{vermelho}FIM DO PROGRAMA CALCULADORA{reset}'.center(30))
divisor()

