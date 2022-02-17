"""
Date: 03/02/2022
Author: Flaviane S. Nascimento
Desc.: Calculadora Python. Realiza as funções de soma, subtração, multiplicação, divisão, resto da divisão, potência e raiz. Armazena o histórico de operações em um arquivo txt que pode ser manipulado.
"""

from os import system
from time import sleep


class Calculadora:
    def __init__(self):
        print("""
1- Soma
2- Subtração
3- Multiplicação
4- Divisão
5- Resto da divisão
6- Potência
7- Raiz
8- Histórico
9- Sair
        """)


class Soma:
    """ Soma entre dois números """

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.soma = self.num1 + self.num2
        self.arquivo = open("historico.txt", "a")
        self.historico = f'{self.soma}\n'
        self.arquivo.write(self.historico)
        self.arquivo.close()
        print("{} + {} = {}".format(self.num1, self.num2, str(self.soma)))


class Subtracao:
    """ Subtração entre dois números """

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.subtracao = self.num1 - self.num2
        self.arquivo = open("historico.txt", "a")
        self.historico = f'{self.subtracao}\n'
        self.arquivo.write(self.historico)
        self.arquivo.close()
        print("{} - {} = {}".format(self.num1, self.num2, str(self.subtracao)))


class Multiplicacao:
    """ Multiplicação entre dois números """

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.multiplicacao = self.num1 * self.num2
        self.arquivo = open("historico.txt", "a")
        self.historico = f'{self.multiplicacao}\n'
        self.arquivo.write(self.historico)
        self.arquivo.close()
        print("{} * {} = {}".format(self.num1, self.num2, str(self.multiplicacao)))


class Divisao:
    """ Divisão entre dois números """

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.divisao = self.num1 / self.num2
        self.arquivo = open("historico.txt", "a")
        self.historico = f'{self.divisao}\n'
        self.arquivo.write(self.historico)
        self.arquivo.close()
        print("{} / {} = {}".format(self.num1, self.num2, str(self.divisao)))


class RestoDaDivisao:
    """ Resto da divisão entre dois números """

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.restodivisao = self.num1 % self.num2
        self.arquivo = open("historico.txt", "a")
        self.historico = f'{self.restodivisao}\n'
        self.arquivo.write(self.historico)
        self.arquivo.close()
        print("O resto da divisão entre {} e {} = {}".format
              (self.num1, self.num2, str(self.restodivisao)))


class Potencia:
    """ Solicita base e expoente e retorna a potência """

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.potencia = self.num1 ** self.num2
        self.arquivo = open("historico.txt", "a")
        self.historico = f'{self.potencia}\n'
        self.arquivo.write(self.historico)
        self.arquivo.close()
        print("{} elevado a {} = {}".format(self.num1, self.num2, str(self.potencia)))


class Raiz:
    """ A raiz quadrada de um número """

    def __init__(self, num1):
        self.num1 = num1
        self.raiz = self.num1 ** (1 / 2)
        self.arquivo = open("historico.txt", "a")
        self.historico = f'{self.raiz}\n'
        self.arquivo.write(self.historico)
        self.arquivo.close()
        print('Raiz: %.2f' % self.raiz)


class ImprimirHistorico:
    """ Exibe o histórico de cálculos """

    def __init__(self):
        self.historico = open("historico.txt", "r")
        for listar in self.historico:
            print(listar)
        self.historico.close()


class DeletarHistorico:
    """ Deleta o histórico de cálculos """

    def __init__(self):
        self.deletar = open("historico.txt", "w")
        self.deletar.close()
        print("Histórico deletado")


system('clear')
print(10 * "=", "CALCULADORA", 10 * "=")
print(33 * "=")


def calculadora():
    Calculadora()
    opcao = input("Digite o número correspondente a operação que deseja realizar: ")

    def soma():

        try:
            system('clear')
            num1 = float(input("Número para soma: "))
            num2 = float(input("Segundo número para soma: "))
            Soma(num1=num1, num2=num2)
            nova_operacao()

        except (Exception,):
            erro()
            sleep(1)
            soma()

    def subtracao():

        try:
            system('clear')
            num1 = float(input("Número para subtração: "))
            num2 = float(input("Segundo número para subtração: "))
            Subtracao(num1=num1, num2=num2)
            nova_operacao()

        except (Exception,):
            erro()
            sleep(1)
            subtracao()

    def multiplicacao():

        try:
            system('clear')
            num1 = float(input("Número para multiplicação: "))
            num2 = float(input("Segundo número para multiplicação: "))
            Multiplicacao(num1=num1, num2=num2)
            nova_operacao()

        except (Exception,):
            erro()
            sleep(1)
            multiplicacao()

    def divisao():

        try:
            system('clear')
            num1 = float(input("Número para divisão: "))
            num2 = float(input("Segundo número para divisão: "))
            Divisao(num1=num1, num2=num2)
            nova_operacao()

        except (Exception,):
            erro()
            sleep(1)
            divisao()

    def resto_divisao():

        try:
            system('clear')
            num1 = float(input("Número para divisão: "))
            num2 = float(input("Segundo número para divisão: "))

            if num1 < num2:
                print(num1, "não divisível por", num2)
                print("O primeiro número deve ser maior que o segundo")
                sleep(7)
                resto_divisao()

            RestoDaDivisao(num1=num1, num2=num2)
            nova_operacao()

        except (Exception,):
            erro()
            sleep(1)
            resto_divisao()

    def potencia():

        try:
            system('clear')
            num1 = float(input("Número base: "))
            num2 = float(input("Número expoente: "))
            Potencia(num1=num1, num2=num2)
            nova_operacao()

        except (Exception,):
            erro()
            sleep(1)
            potencia()

    def raiz():

        try:
            system('clear')
            num1 = float(input("Digite o número: "))
            Raiz(num1)
            nova_operacao()

        except (Exception,):
            erro()
            sleep(1)
            raiz()

    def historico():
        escolha = input("""
1- Histórico
2- Deletar histórico
3- Voltar 
""")
        if escolha == '1':
            system('clear')
            ImprimirHistorico()
            historico()

        elif escolha == '2':
            system('clear')
            confirmar = input("Deseja realmente deletar o histórico? S/N ")

            if confirmar.upper() == 'S':
                system('clear')
                DeletarHistorico()
                sleep(2)
                system('clear')
                historico()

            elif confirmar.upper() == 'N':
                system('clear')
                historico()

            else:

                if confirmar.upper() != ['S', 'N']:
                    print("Inválido")
                    sleep(2)
                    system('clear')
                    historico()

        elif escolha == '3':
            system('clear')
            calculadora()

        else:

            if escolha != ['1', '2', '3']:
                print("Inválido")
                sleep(2)
                system('clear')
                historico()

    def nova_operacao():
        novaoperacao = input("\nNova operação? S/N ")

        if novaoperacao.upper() == 'S':
            system('clear')
            calculadora()

        elif novaoperacao.upper() == 'N':
            print("Até logo!")
            quit()

        else:

            if novaoperacao.upper() != ['S', 'N']:
                print("Inválido")
                nova_operacao()

    def erro():
        print("\nDigite apenas números")

    if opcao == "1":
        soma()
    elif opcao == '2':
        subtracao()
    elif opcao == '3':
        multiplicacao()
    elif opcao == '4':
        divisao()
    elif opcao == '5':
        resto_divisao()
    elif opcao == '6':
        potencia()
    elif opcao == '7':
        raiz()
    elif opcao == '8':
        system('clear')
        historico()
    elif opcao == '9':
        print("Até logo!")
        quit()
    else:
        if opcao.isdigit() != ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Inválido")
            sleep(2)
            system('clear')
            calculadora()


calculadora()
