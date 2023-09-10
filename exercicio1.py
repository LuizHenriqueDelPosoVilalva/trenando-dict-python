'''1. Crie um Dicionário para representar um Animal. Você deve criar os atributos para reino,
espécie, local de origem, nome científico. Desenvolva também um método para imprimir um
animal e crie três exemplos para exemplificar'''

animal1 = {
    'nome': 'elefante',
    'espécie': 'Africana',
    'local': 'Africa',
    'nomeCientífico': ' Loxodonta africana',
}

animal2 = {
    'nome': 'urso',
    'espécie': 'urso Pardo',
    'local': [ 'Rússia', 'Ásia central', 'China', 'Canadá', 'Estados Unidos'],
    'nomeCientífico': 'Ursus arctos',
}

animal3 = {
    'nome': 'cobra',
    'espécie': 'naja',
    'local': [ 'África', 'Sudoeste da Ásia', 'Sul da Ásia e Sudeste Asiático'],
     'nomeCientífico': 'naja',
}

print(f"nome: {animal1['nome']}, espécie: {animal1['espécie']}, local: {animal1['local']}, nome científico: {animal1['nomeCientífico']}")
print(f"nome: {animal2['nome']}, espécie: {animal2['espécie']}, local: {animal2['local']}, nome científico: {animal2['nomeCientífico']}")
print(f"nome: {animal3['nome']}, espécie: {animal3['espécie']}, local: {animal3['local']}, nome científico: {animal3['nomeCientífico']}")