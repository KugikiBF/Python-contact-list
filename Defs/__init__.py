arq="pessoas_cadastradas.txt"


def menu():
    from time import sleep
    if not arq_existe():
        criar_arq()
    while True:
        sleep(1)
        cabeçalho("MENU PRINCIPAL")
        mostrar_opcoes()
        print(linha())
        opc=leiaint("Sua opção: ")
        if opc==1:
            sleep(0.5)
            ler_arquivo()
        elif opc==2:
            cadastro()
        elif opc==3:
            sleep(0.5)
            cabeçalho("Saindo do sistema... até logo")
            break
        else:
            erro("Erro: Opção inválida!")

def erro(txt):
    print(f"\033[35m{txt}\033[m")

def linha(tam=30):
    return "-"*tam

def cabeçalho(txt):
    print('\033[32m')
    print(linha())
    print(txt.center(30))
    print(linha())
    print('\033[m')

def leiaint(txt):
    while True:
        try:
            leiaint=int(input(f"{txt}"))
            return leiaint
        except KeyboardInterrupt:
            erro("usuario preferiu não informar um valor")
            leiaint=0
            return leiaint
        except:
            erro("Erro: Digite um número inteiro válido")

def cadastro():
    cabeçalho("Cadastrando Pessoa")
    nome=input("Nome: ").strip()
    idade=leiaint("Idade: ")
    try:
        with open(arq,"at") as a:
            a.write(f'{nome};{idade}\n')
        erro(f"Novo registro de {nome} adicionado")
    except Exception as e:
        erro(f"Houve um erro ao escrever os dados: {e}")

def mostrar_opcoes():
    print("Opção 1: Mostrar cadastros")
    print("Opção 2: Cadastrar nova pessoa")
    print("Opção 3: Sair do sistema")

def arq_encontrado():
    if arq_existe==True:
        cabeçalho("Arquivo encontrado")
    else:
        cabeçalho(erro("Arquivo não encontrado"))

def criar_arq():
    try:
        a=open(arq,"wt+")
        a.close()
    except:
        erro("Houve um erro na criação do arquivo")
    else:
        print("Arquivo criado com sucesso")

def arq_existe():
    try:
        a=open(arq,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:return True

def ler_arquivo():
    try:
        a=open(arq,'rt')
    except:
        erro("Erro ao ler o arquivo")
    else:
        cabeçalho("Pessoa Cadastradas")
        print(f"\033[36m{"Nome":<15}{"Idade":>15}\033[m\n")
        for linha in a:
            dado=linha.split(';')
            dado[1]=dado[1].replace("\n","")
            print(f"{dado[0]:<15}{dado[1]:>15}")
    finally:
        a.close()