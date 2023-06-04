lista01 = ['Cristian', 'vancris', 'Crisvano', 'alexandre', 'WESLEY']
lista02 = [37, 28, 25, 36, 35]

quantidade = 0
for nome, idade in zip(lista01, lista02):
    quantidade += 1
    print(f'{nome.title()} tem {idade} anos!')

print(f'Existem {quantidade} nomes e idades na lista!')

