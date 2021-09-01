# A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.

# Entrada
# O arquivo de entrada contém um valor inteiro N (0 < N < 46).

# Saída
# Os valores devem ser mostrados na mesma linha, separados por um espaço em branco. Não deve haver espaço após o último valor.

n = int(input())
while n < 0 or n > 46:
    n = int(input('digite um numero inteiro ate 46: '))
fib_list = [0, 1]
if n == 1:
    print(0)
elif n == 2:
    print(0, 1)
else:
    n = n - 2
    for i in range (n) :
        fib_list.append((fib_list[-1] + fib_list [-2]))
    fib_string = ' '.join(map(str,fib_list) )
    print(fib_string)











