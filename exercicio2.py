'''2. Implemente uma lista de contatos, para tal, você pode se basear na lista de contatos de seu
smartphone. Adicione alguns contatos à lista e faça um método de impressão.'''

contatos = [
    {
        'nome':'Joana',
        'numero': 679989-8992,
        'Email':'aaaa@aaa.com',
        'endereço':'sasasasasasa'
    },
    {
        'nome':'Rodrigo',
        'numero': 679989-8994,
        'Email':'bbbbb@bbbbb.com',
        'endereço':'Rua B'
    },
    {
        'nome':'Lara',
        'numero': 679988-9929,
        'Email':'cccccc@ccccc.com',
        'endereço':'Rua C'
    },
    {
        'nome':'JoaoBobão',
        'numero': 679988992,
        'Email':'ddddd@ddddd.com',
        'endereço':'Rua F'
    },
]

nome = input('Insira o nome do contato: ')
numero = int(input('Insira o numero de telefone: '))
email = input('Insira um Email: ')
endereco = input('Insira o endereço')

novoContato = dict( nome = nome, numero = numero, Email = email, endereço = endereco)
contatos.append(novoContato)



for c in contatos:
    print(c)