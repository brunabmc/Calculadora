# Definindo as funções aritméticas


def soma(n1, n2):
    return n1 + n2


def subtracao(n1, n2):
    return n1 - n2


def divisao(n1, n2):
    if n2 == 0:
        print("Divisão inválida.")
        return "-"
    else:
        return n1 / n2


def multiplicacao(n1, n2):
    return n1 * n2


# Entrada de valores pelo usuário

num1 = float(input("n1: "))
num2 = float(input("n2: "))

print("Escolha a operação aritmética: ")
print("1 - Soma")
print("2 - Subtração")
print("3 - Divisão")
print("4 - Multiplicação")

operacaoArit = int(input())

simbolos = ["+", "-", "/", "*"]

if operacaoArit == 1:
    print(num1, simbolos[0], num2, " = ", soma(num1, num2))

if operacaoArit == 2:
    print(num1, simbolos[1], num2, " = ", subtracao(num1, num2))

if operacaoArit == 3:
    print(num1, simbolos[2], num2, " = ", divisao(num1, num2))

if operacaoArit == 4:
    print(num1, simbolos[3], num2, " = ", multiplicacao(num1, num2))
