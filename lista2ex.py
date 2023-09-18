def menu(lista, cont):
    print('-- SISTEMAS DE GERENCIAMENTOS DE ALUNOS --')
    while True:
        print("Menu de opções")
        print('---------------')
        print("1 -- Digitar nome do aluno --")
        print("2 -- Apresentar alunos --")
        print("3 -- Buscar aluno pelo nome --")
        print("4 -- Atulizar nota aluno --")
        print("5 -- Excluir aluno --")
        print("6 -- Calcular média de todos os alunos --")
        print("0 --  Para sair --")

        opcao = int(input(">> "))

        match opcao:
            case 1:
                print("--Cadastrar--")
                cont = cadastrar_aluno(lista, cont)
            case 2:
                print("--Listar alunos--")
                listar_alunos(lista)
            case 3:
                print("--Buscar aluno--")
                buscar = input("Digite o nome: ")
                posicao = buscar_aluno_pelo_nome(lista, buscar)
                if posicao >= 0:
                    print("aluno encontrado")
                    print(lista[posicao])
                else:
                    print("aluno não encontrado")
            case 4:
                print("--Atualizar nota aluno --")
                atualizar_nota(lista)
            case 5:
                print("-- Excluir aluno --")
                buscar = input("Digite o nome do aluno a ser excluido: ")
                posicao = buscar_aluno_pelo_nome(lista, buscar)
                if posicao >= 0:
                    print("Aluno encontrado")
                    aluno_removido = excluir_aluno(lista, posicao)
                    print("Aluno removido")
                else:
                    print("Aluno não encontrado")
            case 6:
                print("-- Media das notas de todos os alunos cadastrados --")
                resultadoMedias = apresentar_medias_alunos(lista)
                print(resultadoMedias)
                
            case 0:
                break
            case _:
                print("Não existe essa opção")


def cadastrar_aluno (lista, cont):
    id = cont
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    nota3 = float(input("Digite a terceira nota do aluno: "))
    nota4 = float(input("Digite a quarta nota do aluno: "))
    
    aluno = dict(
        id = id, 
        nome = nome, 
        nota1_aluno = nota1, 
        nota2_aluno = nota2, 
        nota3_aluno = nota3, 
        nota4_aluno = nota4)
    lista.append(aluno)
    cont += 1
    print("--Cadastro Efetuado com sucesso--")
    return cont

def listar_alunos(lista):
    for item in lista:
        imprimir_alunos(item)

def imprimir_alunos(aluno):
   print('id: ', aluno['id'])
   print('Aluno:', aluno['nome'])
   print('Nota 1: ', aluno['nota1_aluno'])
   print('Nota 2: ', aluno['nota2_aluno'])
   print('Nota 3: ', aluno['nota3_aluno'])
   print('Nota 4: ', aluno['nota4_aluno'])

def buscar_aluno_pelo_nome(lista, buscar):
    tamanho = len(lista)
    if tamanho > 0:
        for i in range(tamanho):
            if lista[i]['nome'] == buscar:
                return i
        else:
            return -1
    else:
        return -1

def atualizar_nota(lista):
    nome = input("Digite o nome do aluno: ")
    tamanho = len(lista)
    if tamanho > 0:
        for i in range(tamanho):
            if lista[i]['nome'] == nome:
                nova_nota1 = input("Digite a primeira nova nota do aluno: ")
                nova_nota2 = input("Digite a primeira nova nota do aluno: ")
                nova_nota3 = input("Digite a primeira nova nota do aluno: ")
                nova_nota4 = input("Digite a primeira nova nota do aluno: ")

                lista[i]['nota1_aluno'] = nova_nota1
                lista[i]['nota2_aluno'] = nova_nota2
                lista[i]['nota3_aluno'] = nova_nota3
                lista[i]['nota4_aluno'] = nova_nota4
                print("Notas atualizadas com sucesso")
                print("------------------------------")
                print(lista[i])
            else:
                print("Nome do aluno não encontrado")
    else:
        print("Nome não encontrado")
    
def excluir_aluno(lista, posicao):
    remover = lista.pop(posicao)
    return remover

def media_alunos(aluno):
    nota1 = aluno['nota1_aluno']
    nota2 = aluno['nota2_aluno']
    nota3 = aluno['nota3_aluno']
    nota4 = aluno['nota4_aluno']
    media = (nota1 + nota2 + nota3 + nota4) /4
    return media
    
def apresentar_medias_alunos(lista):
    if not lista:
        return "A lista de alunos está vazia."

    apresentacao = "Médias dos alunos:\n"
    for aluno in lista:
        nome_aluno = aluno['nome']
        media_aluno = media_alunos(aluno)
        apresentacao += f"{nome_aluno}: {media_aluno:.2f}\n"

    return apresentacao



contador = 0
lista_alunos = []
menu(lista_alunos, contador)
