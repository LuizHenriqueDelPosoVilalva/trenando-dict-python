def menu(lista, cont):
    while True:
        print('---Sistemas de gerenciamento de atividades')
        print('1- Cadastrar Atividade')
        print('2- Listar Atividades')
        print('3- Atualizar Atividade')
        print('4- Remover Atividades')
        print('5- Buscar atividade pro nome')
        print('6- Buscar atividades por atividades de carga horaria')
        print('0- para sair')

        opcao = int(input('Digite a opção: '))
        
        match opcao:
            case 1:
                print('--Cadastro--')
                cadastrar_atividade(lista, cont)
                listar_atividades(lista)
            case 2:
                print('--Listagem--')
                listar_atividades(lista)
            case 3:
                print('--Atualizar--')
                nome = input('Digite o nome da atividade: ')
                posicao = buscar_atividade_por_nome(lista, nome)
                if posicao >= 0:
                    print('atividade encontrada')
                    atualizar_atividade(lista, posicao)
                    print('atividade atualizada com sucesso')
                else:
                    print('atividade não encontrada')
            case 4:
                print('--Remover--')
                nome = input('Digite o nome da atividade')
                posicao = buscar_atividade_por_nome(lista, nome)
                if posicao >= 0:
                    print('Atividade encontrada')
                    atv = remover_atividade(lista, posicao)
                    print('Atividade removida')
                    imprimir_atividade(atv)
                else:
                    print('Atividade não encontrada')
            case 5:
                print('--Buscar atividade--')
                nome = input('Digitar atividade a ser buscada: ')
                posicao = buscar_atividade_por_nome(lista, nome)
                if posicao >= 0:
                    print('Atividade encontrada!')
                    imprimir_atividades(lista[posicao])
                else:
                    print('Atividade não encontrada')
            case 6:
                print('-Busca carga horaria por')
                qtd_carga_horaria = int(input('Digte a quantidade de horas para encontrar atividades com carga horaria maior: '))
                lista_ch_maior = buscar_atividades_com_ch_maior_que(lista, qtd_carga_horaria)
                if len(lista_ch_maior) > 0:
                    listar_atividades(lista_ch_maior)
                else:
                    print('Não existem atividades com carga horária maior que ', qtd_carga_horaria)
            case 0:
                break
            case _:
                print('não existe essa opção')

def cadastrar_atividade(list, cont):
    id = cont
    titulo = input("Digite o titulo da atividade: ")
    descricao = input("informe a descrição da atividade: ")
    cargaHoraria = input("Carga Horaria: ")
    data = input('data [d/m/Y]: ')  
    atividade = dict(id = id, titulo = titulo, descricao = descricao, cargaHoraria = cargaHoraria, data = data)
    list.append(atividade)
    cont +=1
    print("Cadastro efetuado com sucesso")
    return cont

def listar_atividades(list):
    for item in list:
        imprimir_atividades(item)

def imprimir_atividades(atv):
    print('id: ', atv['id'])
    print('titulo: ', atv['titulo'])
    print('descrição: ', atv['descricao'])
    print('carga horaria: ', atv['cargaHoraria'])
    print('data: ', atv['data'])

def buscar_atividade_por_nome(lista, atividade_nome):
    tamanho = len(lista)
    if tamanho > 0:
        for i in range(tamanho):
            if lista[i]["titulo"] == atividade_nome:
                return i
            return -1
        else:
            return -1

def remover_atividade(lista,  posicao):
   atividade = lista.pop(posicao)
   return atividade

def atualizar_atividade(lista, posicao):
    imprimir_atividades(lista[posicao])
    lista[posicao]['titulo'] = input('digite a novo título: ')
    lista[posicao]['descrição'] = input('digite a nova descrição: ')
    lista[posicao]['carga horaria'] = input('digite a nova carga horaria: ')
    lista[posicao]['data'] = input('digite a nova data: ')

def buscar_atividades_com_ch_maior_que(lista, valor):
    tamanho = len(lista)
    if tamanho > 0:
        lista_ch_maior = []
        for i in lista:
           if i['carga horaria'] > valor:
                lista_ch_maior.append(i)
        return lista_ch_maior
    else:
        return []


cont = 0
lista_atv = []
menu(lista_atv, cont)
