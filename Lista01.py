produtos = [
    'tinta acrílica 18 litros 1un', 'porcelanato 73x73 60un', 'argamassa 4kg 10un',
    'tijolos dois furos 2.000un', 'roda pé 2,50 comprimento 15un', 'cal 415 sacos'
]

valores = [68.60, 3959.40, 1200, 3619, 950, 1540]

itens = 0

for produto, valor in zip(produtos, valores):
    itens += 1 

    print(f'{produto.capitalize()}: {valor:.2f} R$')

 
