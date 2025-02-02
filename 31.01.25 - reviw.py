
print("Arquivo fibonacci.csv foi criado com sucesso!")import csv

n = int(input('Digite o valor de n: '))

a, b = 1, 1
lstFibonacci = [a := (b := a + b) - b for _ in range(n)]

with open('fibonacci.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(lstFibonacci)
