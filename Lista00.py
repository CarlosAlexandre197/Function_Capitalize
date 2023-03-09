lista1 = ['Cristiano', 'vancris', 'Crisvano', 'alexandre', 'WESLEY']
lista2 = [37, 28, 25, 36, 35]

quantidade = 0
for nome, idade in zip(lista1, lista2):
    quantidade += 1
    print(f'{nome.title()} tem {idade} anos!')

print(f'Existem {quantidade} nomes e idades na lista!')

