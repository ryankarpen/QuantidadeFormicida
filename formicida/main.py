# Nome: Ryan Lucas Karpen
# Data: 21/09/2022
# Curso: Ciência Da Computação 2°fase
from formicida import formigas

area_sauva = []
area_quenquen = []

formigas_total = int(input('Informe a quantidade total de formigueiros:'))
for c in range(formigas_total):
    tipo = str(input('Informe o tipo de formigueiro [saúva/quenquén]:'))
    if tipo == 'sauva':
        s = formigas.Sauva(float(input('Informe a largura do formigueiro em cm:')),
                           float(input('Informe a comprimento do formigueiro em cm:')))
        area_sauva.append(s.area_formigueiro())

    if tipo == 'quenquen':
        q = formigas.Quenquen(float(input('Informe a largura do formigueiro em cm:')),
                              float(input('Informe a comprimento do formigueiro em cm:')))
        area_quenquen.append(q.area_formigueiro())

soma_sauva = 0
soma_quenquen = 0
for c in area_sauva:
    soma_sauva += c

for i in area_quenquen:
    soma_quenquen += i


# 8 g - 1 m2 (quenquen)
#   x - soma_quenquen

# 10 g - 1 m2 (sauva)
#    x - soma_sauva

# 1 pacote = 10 g

formicida_sauva = (10 * soma_sauva)/1000
formicida_quenquen = (8 * soma_quenquen)/1000
pacotes_sauva = formicida_sauva/10
pacotes_quenquen = formicida_quenquen/10

print('-'*30)
print('A area total de Saúva é {:.2f} m²'.format(soma_sauva))
print('Quantidade de formicida para Saúva: {:.2f} g. Equivalente a {:.2f} pacotes'.format(formicida_sauva, pacotes_sauva))
print('A area total de Quenquén é: {:.2f} m²'.format(soma_quenquen))
print('Quantidade de formicida para Quenquén: {:.2f} g. Equivalente a {:.2f} pacotes'.format(formicida_quenquen, pacotes_quenquen))



