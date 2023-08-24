sum = 0                                 # inicia variável sum com valor = 0

for number in range(11, 30, 2):         # laço de repetição, para "number" no intervalo de 11 a 30, pulando de 2 em 2
    sum += number                       # soma recebe o valor de soma + o valor de número
    print("a soma parcial é de:", sum)  # imprime a soma parcial

print("A soma dos números ímpares de 10 a 30 é:", sum)   # imprime o valor da soma
