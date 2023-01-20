from datetime import datetime  # Para registrar data e hora
from os import system  # Para limpar a tela
from time import sleep  # Para fazer um delay
from random import *
import requests
import json
from pyrebase import pyrebase

firebaseConfig = {'apiKey': "AIzaSyBUx7QS7Hvf5iVL5kFaNtVYfTR1e6G9Vyo",
  "authDomain": "protoon-249ed.firebaseapp.com",
  'databaseURL': "https://protoon-249ed-default-rtdb.firebaseio.com",
  'projectId': "protoon-249ed",
  'storageBucket': "protoon-249ed.appspot.com",
  'messagingSenderId': "288750861883",
  'appId': "1:288750861883:web:f68a07119bcb00e1c9261e",
  'measurementId': "G-PQYW79M82Q"}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

logado = []  # Variável para login
azul = '\033[034m'
lilas = '\033[035m'
verde = '\033[032m'
amarelo = '\033[033m'

# Links do Banco de Dados
link_mobile = 'https://protoon-249ed-default-rtdb.firebaseio.com/Python/Mobile/'
link_sistema = 'https://protoon-249ed-default-rtdb.firebaseio.com/Python/Sistema/'

# Formatando data e hora
now = datetime.now()
data = f'{now.day}/{now.month}/{now.year}'
hora = f'{now.hour}:{now.minute}'
for i in data:
    if len(data) > 8:
        mes = data[2:5].strip('/0')
        ano = data[5:].strip('/')
    else:
        mes = data[2:4].strip('/')
        ano = data[4:].strip('/')

# Função para printar linha
def linha():
    print('_' * 80)

# Função para limpar a tela
def limpar():
    print('\n' * 40)

# Função para printar um cabeçalho com mensagem desejada
def cabeçalho(msg):
    linha()
    print(f'\033[033m{msg:^75}\033[m')
    linha()

# Função para mensagem de erro
def erro(msg):
    sleep(0.5)
    print(f'\n\033[031m{msg:^50}\033[m')
    print()
    sleep(1)

# Função para mensagem de erro
def certo(msg):
    print(f'\n\033[032m{msg:^50}\033[m')

# Função para uma animação no inicio
def inicio():
    print('\n' * 3)
    print(f'\033[034m{"BEM VINDO AO PROTO-ON":^100}\033[m')
    sleep(3)
    print('\n')
    limpar()
    usuario()

# Função para tratar erro quando input é interrompido
def interromper():
    print('\n' * 2)
    erro('O Programa foi interrompido')
    #sleep(2)
    print('\n')
    limpar()
    #finalizar()

# Função para finalizar o programa
def finalizar():
    try:
        print(f'\n\033[032m{"Estamos Finalizando...":^50}\033[m')
        sleep(2)
        limpar()
        print(f'\n\033[034m{"Muito obrigado e volte sempre.":^50}\033[m')
        print('\n' * 5)
        sleep(1000)
    except KeyboardInterrupt:
        print()

# Função para escolha do tipo de usúario
def usuario():
    cabeçalho('Escolha Tipo de acesso: ')
    sleep(2)
    opcoes_usuario = ['Funcionário da Prefeitura', 'Cicadão']
    for k, v in enumerate(opcoes_usuario):
        sleep(0.3)
        print(f'\033[034m{k + 1}- {v}')
        if k == len(opcoes_usuario) - 1:
            sleep(0.3)
            print(f'{k + 2}- Sair\033[m')
    try:
        while True:
            try:# Validção do input
                linha()
                sleep(1)
                usuario = input('\033[035mQual será seu acesso: \033[m')
                usuario = int(usuario)
                if usuario < 1 or usuario > len(opcoes_usuario) + 1:
                    print('\n\033[031mNão existe esta opção...\033[m')
                    sleep(1)
                else:
                    break
            except ValueError:
                erro('Valor Inválido')
        # Direcionamento de acordo com a escolha
        if usuario == 1:  # Funcionario
            print('\n')
            print(f'{"Você está sendo direcionado...":^40}')
            sleep(3)
            # system('clear')
            login_funcionario()
        if usuario == 2:  # Municipe
            print('\n')
            print(f'{"Você está sendo direcionado...":^40}')
            sleep(2)
            opcoes_login()
        if usuario == 3:  # Sair
            finalizar()
    except(KeyboardInterrupt):
        interromper()

# Aqui segue 7 funções do funcionário, optei por não por cadastro pra eles
# Função da tela de login do funcionario, ele entra com usuário e senha da aprefeitura está em funcionario.txt
def login_funcionario():
    limpar()
    cabeçalho('Tela de login')
    sleep(2)
    print()
    try:  # Para tratamento de erro, neste caso para quando usuario interromper o programa
        cont = 0
        while True:
            if cont == 3:
                break
            nome = str(input('Nome: ')).title().strip()
            print()
            email = str(input('E-mail: ')).lower().strip()
            print()
            senha = str(input('Senha: ')).upper().strip()
            try:
                login = auth.sign_in_with_email_and_password(email, senha)
                cont = 0
                sleep(1)
                break
            except:
                cont += 1
                erro('E-mail ou senha está inválido')
        if cont == 3:
            erro('Foram muitas tentivas, vamos encerrar o programa...')
            finalizar()
    except KeyboardInterrupt:
        interromper()
    if cont == 0:
        sleep(1)
        certo('Acesso Permitido')
        sleep(1)
        logado.append(nome)
        menu_funcionario()

# Função para retornar ao menu principal do funcionario
# Função de transição de tela para a principal
def menu_funcionario():
    limpar()
    print('\n')
    print(f'\033[032m{"Abrindo o Menu Principal...":^50}\033[m')
    print('\n' * 4)
    sleep(2)
    limpar()
    opcoes_funcionario()

# Função que abre a tela inicial com opções para o funcionario, de registro, consulta ou sair
def opcoes_funcionario():
    cabeçalho('MENU PRINCIPAL')
    # colocando opções em uma lista e printando como opções
    opcoes = ['Registrar uma reclamação', 'Colsultar reclamações em aberto', 'Atualizar Reclamação', 'Excluir Reclamação']
    for k, v in enumerate(opcoes):
        sleep(0.3)
        print(f'\033[034m{k + 1}- {v}')
        if k == len(opcoes) - 1:
            sleep(0.3)
            print(f'{k + 2}- Sair\033[m')
    # Validação das opções da tela inicial
    try:
        while True:
            try:
                linha()
                sleep(1)
                processo = int(input('\033[035mDigite o número da opção que dejesa executar? \033[m'))
                if processo < 1 or processo > len(opcoes) + 1:
                    erro('Não existe esta opção...')
                    sleep(1)
                else:
                    break
            except ValueError:
                erro('Valor Inválido')
        # Direcionamento de acordo com a escolha
        if processo == 1:
            print(f'\n{"Abrindo tela de reclamação...":^40}')
            sleep(3)
            # system('clear')
            cadastro_problema_funcionario()
        if processo == 2:
            print('\n')
            cabeçalho('Carregando Opções de Consulta...')
            sleep(2)
            consultar_funcionario()
        if processo == 3:
            print('\n')
            cabeçalho('Carregando Tela de atualização...')
            sleep(2)
            atualizar()
        if processo == 4:
            print('\n')
            cabeçalho('Carregando Tela de exclusão...')
            sleep(2)
            excluir()
        if processo == 5:
            finalizar()
    except(KeyboardInterrupt):
        interromper()

# Função para o funcionario registrar o problema
def cadastro_problema_funcionario():
    # Informações do problema a ser registrada
    limpar()
    cabeçalho('Tela de Registro de Problema')
    sleep(2)
    try:
        cabeçalho('MENU DE CADASTRO')
        # colocando opções em uma lista e printando como opções
        opcoes = ['Registrar do Mobile para o Sistema', 'Registrar direto no Sistema']
        for k, v in enumerate(opcoes):
            sleep(0.3)
            print(f'\033[034m{k + 1}- {v}')
            if k == len(opcoes) - 1:
                sleep(0.3)
                print(f'{k + 2}- Retornar ao Menu Principal\033[m')
        # Validação das opções da tela inicial
        while True:
            try:
                linha()
                sleep(1)
                processo = int(input('\033[035mDigite o número da opção de Registro: \033[m'))
                if processo < 1 or processo > len(opcoes) + 1:
                    erro('Não existe esta opção...')
                    sleep(1)
                else:
                    break
            except ValueError:
                erro('Valor Inválido')
        # Direcionamento de acordo com a escolha
        if processo == 1:
            print('\n')
            cabeçalho('Registro de Mobile para o Sistema')
            sleep(1)
            print('\n' * 2)
            dados = requests.get(f'{link_mobile}.json')
            dict_dados = dados.json()
            contador = 0
            while True:
                protocolo = input('Digite o número do protocolo: ')
                id = []
                cont = 0
                for i in dict_dados:
                    cont += 1
                    if dict_dados[i]['Protocolo'] == protocolo:
                        contador = 0
                        id1 = i
                        id = dict_dados[i]# Protocolo que vai ser transferido para o sistema
                        id2 = id
                        break
                    else:
                        if cont == len(dict_dados) and len(id) == 0:
                            contador += 1
                            erro('Protocolo não encontrado')
                if len(id) != 0:
                    break
                if len(id) == 0 and contador == 3:
                    erro('Protocolo não encontrado muitas vezes')
                    cabeçalho('Retornando ao Menu Principal...')
                    sleep(1)
                    break
            if len(id) != 0:
                sleep(1)
                certo('Protocolo Encontrado')
                id["Protocolo"] = protocolo
                sleep(1)
                con = 0
                for i in id:
                    cabeçalho('OPÇÕES DE PROBLEMA')
                    # colocando opções em uma lista e printando como opções
                    opcoes_problema = ['Iluminação', 'Buraco', 'Entulho', 'Lixo', 'Boca de lobo', 'Outros']
                    for k, v in enumerate(opcoes_problema):
                        print(f'\033[35m{k + 1}- {v}\033[m')
                        sleep(0.3)
                        if k == len(opcoes_problema) - 1:
                            sleep(0.3)
                            print(f'\033[35m{k + 2}- Retornar ao Menu Principal\033[m')
                        # Validação da escolha de opções de problema
                    while True:
                        try:
                            linha()
                            problema = int(input(f'Digite o número da opção do problema{azul}[{id["Problema"]}]\033[m: '))
                            linha()
                            # colocando opções em uma lista e printando como opções
                            opcoes_problema = ['Iluminacao', 'Buraco', 'Entulho', 'Lixo', 'Boca de lobo', 'Outros']
                            if problema == len(opcoes_problema) + 1:  # Sair
                                con += 1
                                break
                            if problema < 1 or problema >= len(opcoes_problema) + 1:
                                print()
                                erro('Não existe esta opção')
                            # Validação da escolha de opções de problema
                            else:
                                id["Problema"] = opcoes_problema[problema - 1]
                                print(f'Tipo de Problema: \033[033m{id["Problema"]}\033[m')
                                break
                        except ValueError:
                            erro('Valor Inválido')
                    if con == 1:
                        break
                    requerente = input(f'Requerente{azul}[{id["Requerente"]}]\033[m: ').title().strip()
                    if len(requerente) < 3:
                        certo('Requerente não alterado')
                        sleep(1)
                        print()
                        requerente = id["Requerente"]
                    id["Requerente"] = requerente
                    # colocando opções em uma lista e printando como opções
                    cabeçalho('Unidades')
                    opcoes_unidade = ['Meio Ambiente', 'Saude', 'Cultura', 'Educacao']
                    for k, v in enumerate(opcoes_unidade):
                        print(f'\033[35m{k + 1}- {v}\033[m')
                        sleep(0.3)
                        if k == len(opcoes_unidade) - 1:
                            sleep(0.3)
                            print(f'\033[35m{k + 2}- Retornar ao Menu Principal\033[m')
                    while True:
                        try:  # Validação da escolha de opções de problema
                            linha()
                            sleep(1)
                            unidade = int(input(f'Digite o número correspondente a Unidade responsável: '))
                            if unidade < 1 or unidade > len(opcoes_unidade) + 1:
                                erro('Não existe esta opção...')
                                sleep(1)
                            else:
                                break
                        except ValueError:
                            erro('Valor Inválido')
                    linha()
                    if unidade == len(opcoes_unidade) + 1:
                        break  # Opção de sair
                    else:
                        id["Unidade"] = opcoes_unidade[unidade - 1]
                        print(f'Unidade Selecionada: {amarelo}Secretaria de {id["Unidade"]}\033[m')
                        sleep(1)
                    cabeçalho('Etapas')
                    linha()
                    # colocando opções em uma lista e printando como opções
                    opcoes_andamento = ['Em Analise', 'Em Execucao', 'Finalizado', 'Rejeitado']
                    for k, v in enumerate(opcoes_andamento):
                        print(f'\033[35m{k + 1}- {v}\033[m')
                        sleep(0.3)
                        if k == len(opcoes_andamento) - 1:
                            sleep(0.3)
                            print(f'\033[35m{k + 2}- Retornar ao Menu Principal\033[m')
                    while True:
                        try:  # Validação da escolha da etapa
                            linha()
                            sleep(1)
                            andamento = int(input(f'Digite o número correspondente a etapa atual{azul}[{id["Etapa"]}]\033[m: '))
                            if andamento < 1 or andamento > len(opcoes_andamento) + 1:
                                print('\n\033[031mNão existe esta opção...\033[m')
                                sleep(1)
                                print()
                            else:
                                break
                        except ValueError:
                            erro('Valor Inválido')
                    linha()
                    if andamento == len(opcoes_andamento) + 1:
                        break  # Opção de sair
                    else:
                        id["Etapa"] = opcoes_andamento[andamento - 1]
                        print(f'Andamento: {amarelo}{id["Etapa"]}\033[m')
                    sleep(1)
                    descricao = input(f'\nDescrição{azul}[{id["Descricao"]}]\033[m: ').capitalize().strip()
                    if len(descricao) < 5:
                        certo('Descrição não alterada')
                        sleep(1)
                        descricao = id["Descricao"]
                    id["Descricao"] = descricao
                    registro = {'Protocolo': id["Protocolo"], 'Funcionario': logado[0], 'Requerente': id["Requerente"], 'Problema': id["Problema"], 'Bairro': id["Bairro"],
                                'Rua': id["Rua"], 'Numero': id["Numero"], 'Data': data, 'Hora': hora, 'Etapa': id["Etapa"], 'Descricao': id["Descricao"], 'Unidade': id["Unidade"]}
                    transferindo = requests.post(f'{link_sistema}.json', data=json.dumps(id2))
                    gravando = requests.post(f'{link_sistema}.json', data=json.dumps(registro))
                    deletando = requests.delete(f'{link_mobile}{id1}.json')
                    sleep(1)
                    cabeçalho('REGISTRO CONCLUÍDO')
                    input('\n\033[032mAperte Enter para retornar ao Menu Principal \033[m')
                    print('\n')
                    break
                menu_funcionario()
            if contador == 3:
                menu_funcionario()
        if processo == 3:
            print('\n')
            cabeçalho('Retornando ao Menu Principal')
            sleep(2)
            menu_funcionario()
        if processo == 2:
            print('\n' * 2)
            cabeçalho('Registro Direto no Sistema')
            sleep(1)
            dados = requests.get(f'{link_sistema}.json')
            dict_dados = dados.json()
            terminal = len(dict_dados) + 1
            terminal = str(terminal)
            if len(terminal) == 1:  # Ajustando terminal pra quando ele ficar com 1 digito
                protocolo = '1900' + str(terminal) + '/' + ano
            if len(terminal) == 2:  # Ajustando terminal pra quando ele ficar com 2 digitos
                protocolo = '190' + str(terminal) + '/' + ano
            if len(terminal) == 3:  # Ajustando terminal pra quando ele ficar com 3 digitos
                protocolo = '19' + str(terminal) + '/' + ano
            registro = {}
            registro["Protocolo"] = protocolo
            registro["Funcionario"] = logado[0]
            print('\n')
            cabeçalho('OPÇÕES DE ASSUNTO')
            # colocando opções em uma lista e printando como opções
            opcoes_problema = ['Iluminação', 'Buraco', 'Entulho', 'Lixo', 'Boca de lobo', 'Outros']
            for k, v in enumerate(opcoes_problema):
                print(f'\033[35m{k + 1}- {v}\033[m')
                sleep(0.3)
                if k == len(opcoes_problema) - 1:
                    sleep(0.3)
                    print(f'\033[35m{k + 2}- Retornar ao Menu Principal\033[m')
                # Validação da escolha de opções de problema
            while True:
                try:
                    linha()
                    problema = int(input('Digite o número da opção do problema? '))
                    linha()
                    # colocando opções em uma lista e printando como opções
                    opcoes_problema = ['Iluminacao', 'Buraco', 'Entulho', 'Lixo', 'Boca de lobo', 'Outros']
                    if problema < 1 or problema > len(opcoes_problema) + 1:
                        print()
                        erro('Não existe esta opção')
                    # Validação da escolha de opções de problema
                    else:
                        break
                except ValueError:
                    erro('Valor Inválido')
            if problema == len(opcoes_problema) + 1:
                cabeçalho('Retornando...')
                sleep(2)
                menu_funcionario()
            else:
                registro["Problema"] = opcoes_problema[problema - 1]
                print(f'{azul}Assunto selecionado foi {registro["Problema"]}\033[m')
                sleep(1)
                registro["Requerente"] = input('Requerente: ').strip().title()
                cabeçalho('Unidades de Origem')
                # colocando opções em uma lista e printando como opções
                opcoes_unidade = ['Meio Ambiente', 'Saúde', 'Cultura', 'Educação']
                for k, v in enumerate(opcoes_unidade):
                    print(f'\033[35m{k + 1}- {v}\033[m')
                    sleep(0.3)
                    if k == len(opcoes_unidade) - 1:
                        sleep(0.3)
                        print(f'\033[35m{k + 2}- Retornar ao Menu Principal\033[m')
                while True:
                    try:# Validação da escolha de opções de unidade
                        linha()
                        sleep(1)
                        unidade = int(input('Digite o número correspondente a Unidade responsável: '))
                        if unidade < 1 or unidade > len(opcoes_unidade) + 1:
                            erro('Não existe esta opção...')
                            sleep(1)
                        else:
                            break
                    except ValueError:
                        erro('Valor Inválido')
                linha()
                if unidade == len(opcoes_unidade) + 1:# Opção de sair
                    cabeçalho('Retornando...')
                    sleep(2)
                    menu_funcionario()
                else:
                    opcoes_unidade = ['Meio Ambiente', 'Saude', 'Cultura', 'Educacao']
                    registro["Unidade"] = opcoes_unidade[unidade - 1]
                    print(f'{azul}Unidade Selecionada foi Secretaria de {registro["Unidade"]}\033[m')
                    registro["Bairro"] = input('Bairro: ').strip().upper()
                    registro["Rua"] = input('Rua: ').strip().capitalize()
                    registro["Numero"] = input('Número: ').strip().capitalize()
                    registro["Data"] = data
                    registro["Hora"] = hora
                    cabeçalho('Etapas')
                    # colocando opções em uma lista e printando como opções
                    opcoes_andamento = ['Em Análise', 'Em Execução', 'Concluído', 'Rejeitado']
                    for k, v in enumerate(opcoes_andamento):
                        print(f'\033[35m{k + 1}- {v}\033[m')
                        sleep(0.3)
                        if k == len(opcoes_andamento) - 1:
                            sleep(0.3)
                            print(f'\033[35m{k + 2}- Retornar ao Menu Principal\033[m')
                    while True:
                        try:# Validação da escolha da etapa
                            linha()
                            sleep(1)
                            andamento = int(input('Digite o número correspondente a etapa atual: '))
                            if andamento < 1 or andamento > len(opcoes_andamento) + 1:
                                print('\n\033[031mNão existe esta opção...\033[m')
                                sleep(1)
                            else:
                                break
                        except ValueError:
                            erro('Valor Inválido')
                    linha()
                    if andamento == len(opcoes_andamento) + 1: # Opção de sair
                        cabeçalho('Retornando...')
                        sleep(2)
                        menu_funcionario()
                    else:
                        opcoes_andamento = ['Em Analise', 'Em Execucao', 'Concluido', 'Rejeitado']
                        registro["Etapa"] = opcoes_andamento[andamento - 1]
                        print(f'\033[036mAndamento está {registro["Etapa"]}\033[m')
                        registro["Descricao"] = input('\nDescrição: ').strip().capitalize()
                        registrando = requests.post(f'{link_sistema}.json', data=json.dumps(registro))
                        linha()
                        print('\n')
                        cabeçalho('REGISTRO BEM SUCEDIDO')
                        sleep(1)
                        print('\n')
                        cabeçalho(f"Número de Protocolo gerado: {protocolo}")
                        input('\nAperte enter para Continuar ')
                        menu_funcionario()
    except KeyboardInterrupt:
        interromper()

# Função para consultar registros filtrados na visão do municipe
def consultar_funcionario():
    try:
        limpar()
        print()
        cabeçalho('OPÇÕES DE CONSULTA')
        linha()
        # Alimentando o dicionário para filtragem
        dados = requests.get(f'{link_sistema}.json')
        dict_dados = dados.json()
        for i in dict_dados:
            date = dict_dados[i]["Data"]
            if len(date) == 8:
                dict_dados[i]['Mes'] = date[2:4].strip('/')
                dict_dados[i]['Ano'] = date[4:].strip('/')
            else:
                dict_dados[i]['Mes'] = date[3:5].strip('/')
                dict_dados[i]['Ano'] = date[5:].strip('/')
        # colocando opções em uma lista e printando como opções
        opcoes_consulta = ['Consultar por N° de Protocolo', 'Consultar por Problema', 'Consultar por Bairro', 'Etapa',
                           'Consultar por Mês', 'Consultar por Ano']
        for k, v in enumerate(opcoes_consulta):
            sleep(0.3)
            print(f'\033[35m{k + 1}- {v}\033[m')
            if k == len(opcoes_consulta) - 1:
                sleep(0.3)
                print(f'\033[35m{k + 2}- Voltar ao Menu Principal\033[m')
        # Validação da opção de filtro
        # Variavel dado filtrado para buscar por dados iguais no input filtro
        dado_filtrado = ''
        while True:
            try:
                linha()
                sleep(1)
                opcao_filtro = input('Digite o número da opção que dejesa executar? ')  # Tipo de Consulta
                opcao_filtro = int(opcao_filtro)
                if opcao_filtro < 1 or opcao_filtro > 7:
                    print('\n\033[031mNão existe esta opção...\033[m')
                    sleep(1)
                else:
                    break
            except ValueError:
                erro('Valor Inválido')
        if opcao_filtro == 7:  # Opção de Sair
            menu_funcionario()
        if opcao_filtro > 0 and opcao_filtro <= 6:
            consulta = opcoes_consulta[opcao_filtro - 1]  # Variável que recebe o índice do valor da consulta
            if opcao_filtro == 1:
                linha()
                dado_filtrado = input('Número do protocolo: ').title().strip()
            if opcao_filtro == 2:
                linha()
                sleep(2)
                limpar()
                cabeçalho('Lista de Problemas')
                linha()
                # colocando opções em uma lista e printando como opções
                opcoes_problema = ['Iluminacao', 'Buraco', 'Entulho', 'Lixo', 'Boca de lobo', 'Outros']
                for k, v in enumerate(opcoes_problema):
                    sleep(0.3)
                    print(f'\033[35m{k + 1}- {v}\033[m')
                    if k == len(opcoes_problema) - 1:
                        sleep(0.3)
                        print(f'\033[35m{k + 2}- Retornar ao Menu Principal\033[m')
                while True:  # Validação do input filtro
                    try:
                        linha()
                        filtro = int(input('Qual tipo de problema: '))
                        sleep(0.5)
                        if filtro < 1 or filtro > 7:
                            print('\n\033[031mNão existe esta opção...\033[m')
                            sleep(1)
                        if filtro == 7:  # Opção Sair
                            break
                        if filtro > 0 and filtro < 7:
                            dado_filtrado = opcoes_problema[filtro - 1]
                            break
                    except ValueError:
                        erro('Valor Inválido')
                if filtro == 7:  # Opção Sair
                    menu_funcionario()
            if opcao_filtro == 3:
                linha()
                dado_filtrado = input('Qual bairro: ').upper().strip()
            if opcao_filtro == 4:
                linha()
                limpar()
                cabeçalho('Opções de Etapa')
                linha()
                # colocando opções em uma lista e printando como opções
                opcoes_etapa = ['Em Analise', 'Em Execucao', 'Finalizado']
                for k, v in enumerate(opcoes_etapa):
                    print(f'\033[35m{k + 1}- {v}\033[m')
                    sleep(0.3)
                    if k == len(opcoes_etapa) - 1:
                        sleep(0.3)
                        print(f'\033[35m{k + 2}- Retorna ao Menu Principal\033[m')
                while True:  # Validação da escolha de opções de problema
                    try:
                        linha()
                        sleep(1)
                        etapa = input('Digite o número correspondente a Etapa: ')
                        etapa = int(etapa)
                        if etapa < 1 or etapa > len(opcoes_etapa) + 1:
                            print('\n\033[031mNão existe esta opção...\033[m')
                            sleep(1)
                        else:
                            break
                    except ValueError:
                        erro('Valor Inválido')
                linha()
                if etapa == len(opcoes_etapa) + 1:
                    menu_funcionario()  # Opção de sair
                else:
                    etapa_selecionada = opcoes_etapa[etapa - 1]
                linha()
                dado_filtrado = etapa_selecionada
            if opcao_filtro == 5:
                linha()
                dado_filtrado = input('Qual número do mês[ex: 12]: ').strip()
            if opcao_filtro == 6:
                linha()
                dado_filtrado = input('Qual ano[ex: 2021]: ').strip()
            # Busca pelo item selecionado na opção_filtro
            print(f'\nPalavra Chave de Busca foi \033[036m{dado_filtrado.upper()}\033[m')
            sleep(2)
            print('\n')
            list_filtrada = []  # Lista que vai receber somente os dicionários com valores iguais ao escolhido
            for i in dict_dados:  # list filtro contém os dicionários (i = dicionário)
                for d in dict_dados[i]:
                    if dict_dados[i][d] == dado_filtrado:
                        list_filtrada.append(dict_dados[i])
            if len(list_filtrada) == 0:
                sleep(0.5)
                print(f'{lilas}Não foi encontrado nada em {consulta} {dado_filtrado}\033[m')
                sleep(2)
                consultar_funcionario()  # Se nada for encontrado retorna as opções de consulta
            else:
                limpar()
                linha()
                cabeçalho('IMPRIMINDO DADOS')
                linha()
                sleep(2)
                # colocando opções em uma lista e printando como opções
                indices = ["Protocolo", "Requerente", "Problema", "Bairro", "Rua"]  # Primeira parte do cabeçalho
                for i in range(len(indices)):
                    print(f'{indices[i]:<18}', end='')
                print()
                linha()
                valores = []
                contador = 0  # Contador para formatar os print
                for i in list_filtrada:
                    for d in indices:
                        if contador == 5:
                            contador = 0
                            print()
                        if contador % 2 == 0:
                            contador += 1
                            print(f'{azul}{i[f"{d}"]:<18}\033[m', end='')
                        else:
                            contador += 1
                            print(f'{lilas}{i[f"{d}"]:<18}\033[m', end='')
                print()
                sleep(2)
                input('\n\033[035mAperte enter para continuar\033[m  ')
                print('_' * 100)
                indices = ["Numero", "Data", "Hora", "Etapa", "Descricao"]  # Segunda parte do cabeçalho
                for i in range(len(indices)):
                    print(f'{indices[i]:<18}', end='')
                print()
                print('_' * 100)
                contador = 0
                for i in list_filtrada:
                    for d in indices:
                        if contador == 5:
                            contador = 0
                            print()
                        if contador % 2 == 0:
                            contador += 1
                            print(f'{azul}{i[f"{d}"]:<18}\033[m', end='')
                        else:
                            contador += 1
                            print(f'{lilas}{i[f"{d}"]:<18}\033[m', end='')
                print()
                dados.close()
                sleep(2)
                input('\n\033[035mAperte enter para continuar\033[m  ')
                menu_funcionario()
    except(KeyboardInterrupt):
        interromper()

# Função para tela de atualização, mas ainda não está pronta esta tela
def atualizar():
    try:
        print('\n' * 4)
        cabeçalho('TELA DE ATUALIZAÇÃO')
        sleep(1)
        print('\n' * 2)
        dados = requests.get(f'{link_sistema}.json')
        dict_dados = dados.json()
        contador = 0
        id = ''
        while True:
            protocolo = input('Digite o número do protocolo para atualização: ')
            cont = 0
            for i in dict_dados:
                cont += 1
                if protocolo == dict_dados[i]["Protocolo"]:
                    id = dict_dados[i]
                else:
                    if cont == len(dict_dados) and len(id) == 0:
                        contador += 1
                        erro('Protocolo não encontrado')
            if len(id) != 0:
                break
            if len(id) == 0 and contador == 3:
                erro('Protocolo não encontrado muitas vezes')
                cabeçalho('Retornando ao Menu Principal...')
                sleep(1)
                break
        if len(id) != 0:
            sleep(1)
            certo('Protocolo Encontrado')
            sleep(1)
            con = 0
            id["Protocolo"] = protocolo
            id["Funcionario"] = logado[0]
            cabeçalho('OPÇÕES DE PROBLEMA')
            # colocando opções em uma lista e printando como opções
            opcoes_problema = ['Iluminação', 'Buraco', 'Entulho', 'Lixo', 'Boca de lobo', 'Outros']
            for k, v in enumerate(opcoes_problema):
                print(f'\033[35m{k + 1}- {v}\033[m')
                sleep(0.3)
                if k == len(opcoes_problema) - 1:
                    sleep(0.3)
                    print(f'\033[35m{k + 2}- Retornar ao Menu Principal\033[m')
                # Validação da escolha de opções de problema
            while True:
                try:
                    linha()
                    problema = int(input(f'Digite o número da opção do problema{azul}[{id["Problema"]}]\033[m? '))
                    linha()
                    # colocando opções em uma lista e printando como opções
                    opcoes_problema = ['Iluminacao', 'Buraco', 'Entulho', 'Lixo', 'Boca de lobo', 'Outros']
                    if problema == len(opcoes_problema) + 1:  # Sair
                        con += 1
                        break
                    if problema < 1 or problema >= len(opcoes_problema) + 1:
                        print()
                        erro('Não existe esta opção')
                    # Validação da escolha de opções de problema
                    else:
                        id["Problema"] = opcoes_problema[problema - 1]
                        print(f'Tipo de Problema: \033[033m{id["Problema"]}\033[m')
                        break
                except ValueError:
                    erro('Valor Inválido')
            if con == 1:
                menu_funcionario()
            requerente = input(f'Requerente{azul}[{id["Requerente"]}]\033[m: ').title().strip()
            if len(requerente) < 3:
                certo('Requerente não alterado')
                sleep(1)
                print()
            else:
                id["Requerente"] = requerente
            # colocando opções em uma lista e printando como opções
            cabeçalho('Unidades')
            opcoes_unidade = ['Meio Ambiente', 'Saude', 'Cultura', 'Educacao']
            for k, v in enumerate(opcoes_unidade):
                print(f'\033[35m{k + 1}- {v}\033[m')
                sleep(0.3)
                if k == len(opcoes_unidade) - 1:
                    sleep(0.3)
                    print(f'\033[35m{k + 2}- Retornar ao Menu Principal\033[m')
            while True:
                try:  # Validação da escolha de opções de problema
                    linha()
                    sleep(1)
                    unidade = int(input(f'Digite o número correspondente a Unidade responsável{azul}[{id["Unidade"]}]\033[m: '))
                    if unidade < 1 or unidade > len(opcoes_unidade) + 1:
                        erro('Não existe esta opção...')
                        sleep(1)
                    else:
                        break
                except ValueError:
                    erro('Valor Inválido')
            linha()
            if unidade == len(opcoes_unidade) + 1:
                menu_funcionario()  # Opção de sair
            else:
                id["Unidade"] = opcoes_unidade[unidade - 1]
                print(f'Unidade Selecionada foi Secretaria de\033[033m {id["Unidade"]}\033[m')
                sleep(1)
            print()
            bairro = input(f'Bairro{azul}[{id["Bairro"]}]\033[m: ').strip().upper()
            if len(bairro) < 3:
                certo('Bairro não alterado')
                sleep(1)
                print()
                bairro = id["Bairro"]
            else:
                id["Bairro"] = bairro
            rua = input(f'Rua{azul}[{id["Rua"]}]\033[m: ').strip().capitalize()
            if len(rua) < 3:
                certo('Rua não alterada')
                sleep(1)
                print()
                rua = id["Rua"]
            else:
                id["Rua"] = rua
            numero = input(f'Número{azul}[{id["Numero"]}]\033[m: ').strip().capitalize()
            if len(numero) < 3:
                certo('Número não alterado')
                sleep(1)
                print()
                numero = id["Numero"]
            else:
                id["Numero"] = numero
            id["Data"] = data
            id["Hora"] = hora
            cabeçalho('Etapas')
            linha()
            # colocando opções em uma lista e printando como opções
            opcoes_andamento = ['Em Analise', 'Em Execucao', 'Finalizado', 'Rejeitado']
            for k, v in enumerate(opcoes_andamento):
                print(f'\033[35m{k + 1}- {v}\033[m')
                sleep(0.3)
                if k == len(opcoes_andamento) - 1:
                    sleep(0.3)
                    print(f'\033[35m{k + 2}- Retorna ao Menu Principal\033[m')
            while True:
                try:  # Validação da escolha da etapa
                    linha()
                    sleep(1)
                    andamento = int(input(f'Digite o número correspondente a etapa atual{azul}[{id["Etapa"]}]\033[m: '))
                    if andamento < 1 or andamento > len(opcoes_andamento) + 1:
                        print('\n\033[031mNão existe esta opção...\033[m')
                        sleep(1)
                        print()
                    else:
                        break
                except ValueError:
                    erro('Valor Inválido')
            linha()
            if andamento == len(opcoes_andamento) + 1:
                menu_funcionario() # Opção de sair
            else:
                id["Etapa"] = opcoes_andamento[andamento - 1]
                print(f'Andamento está\033[036m {id["Etapa"]}\033[m')
            descricao = input(f'\nDescrição{azul}[{id["Descricao"]}]\033[m: ').capitalize().strip()
            if len(descricao) < 5:
                certo('Descrição não alterada')
                sleep(1)
                descricao = id["Descricao"]
            id["Descricao"] = descricao
            atualizacao = requests.post(f'{link_sistema}.json', data=json.dumps(id))
            sleep(1)
            cabeçalho('Atualização Concluida')
            input('\n\033[032mAperte Enter para retornar ao Menu Principal \033[m')
            print('\n')
        menu_funcionario()
    except KeyboardInterrupt:
        interromper()

# Função para tela de atualização, mas ainda não está pronta esta tela
def excluir():
    try:
        print('\n' * 4)
        cabeçalho('TELA DE EXCLUSÃO')
        print('\n')
        sleep(1)
        cabeçalho('Opções de Exclusão')
        opcoes = ['Protocolo de Mobile', 'Protocolo do Sistema']  # Lista de opções do municipe
        for k, v in enumerate(opcoes):
            sleep(0.3)
            print(f'\033[034m{k + 1}- {v}')
            if k == len(opcoes) - 1:
                sleep(0.3)
                print(f'{k + 2}- Retornar ao Menu Principal\033[m')
                sleep(0.3)
        while True:  # Validação do input
            try:
                linha()
                conta = int(input('Qual sua opção: '))
                if conta < 1 or conta > 3:
                    print('\n\033[031mNão existe esta opção...\033[m')
                    sleep(1)
                else:
                    break
            except ValueError:
                erro('Valor Inválido')
        if conta == 2:  # Exclusão do arquivo sistema.txt
            cabeçalho('Exclusão de Protocolo do Sistema')
            sleep(1)
            print()
            dados = requests.get(f'{link_sistema}.json')
            dict_dados = dados.json()
            cont = 0
            id = []
            while True:
                sleep(1)
                print()
                protocolo = input(f'Digite o Protocolo a ser excluido{azul} [ex: 19000/2022]: \033[m').strip()
                protolo_excluido = []
                for i in dict_dados:
                    if protocolo == dict_dados[i]["Protocolo"]:
                        id.append(str(i))
                    else:
                        protolo_excluido.append(i)
                    if len(dict_dados) == len(protolo_excluido):
                        erro('Protocolo não encontrado')
                        cont += 1
                if cont == 3:
                    erro('Protocolo não encontrado muitas vezes')
                    cabeçalho('Retornando ao Menu Principal...')
                    sleep(1)
                    break
                if len(id) != 0:
                    sleep(1)
                    print('\n')
                    resp = input(f'Tem certeza que deseja excluir o Protocolo {amarelo}{protocolo}[S/N] ? \033[m').upper().strip()
                    if resp in "S":
                        break
            if cont == 3:
                menu_funcionario()
            else:
                for i in id:
                    requisicao = requests.delete(f'{link_sistema}{i}.json')
                sleep(1)
                cabeçalho('Exclusão Completa')
                sleep(1)
                input('\n\033[032mAperte Enter para retornar ao Menu Principal...\033[m')
                print('\n')
                menu_funcionario()
        if conta == 3:  # Retorna ao Menu Principal
            menu_funcionario()
        if conta == 1:
            sleep(1)  # Exclusão do arquivo mobile.txt
            cabeçalho('Exclusão de Protocolo do Mobile')
            sleep(1)
            print()
            dados = requests.get(f'{link_mobile}.json')
            dict_dados = dados.json()
            cont = 3
            id = []
            while True:
                protocolo = input(f'Digite o Protocolo a ser excluido{azul} [ex: 19000/2022]: \033[m').strip()
                protolo_excluido = []
                for i in dict_dados:
                    if protocolo == dict_dados[i]["Protocolo"] or dict_dados[i]["Etapa"] == 'Rejeitado':
                        id.append(str(i))
                    else:
                        protolo_excluido.append(i)
                if len(dict_dados) == len(protolo_excluido):
                    erro('Protocolo não encontrado')
                    cont += 1
                    if cont == 6:
                        erro('Protocolo não encontrado muitas vezes')
                        cabeçalho('Retornando ao Menu Principal...')
                        sleep(1)
                        break
                else:
                    sleep(1)
                    print('\n')
                    resp = input(f'Tem certeza que deseja excluir o Protocolo {amarelo}{protocolo}? \033[m').upper().strip()
                    if resp in "S":
                        break
            if cont > 5:
                menu_funcionario()
            else:
                for i in id:
                    exclusao = requests.delete(f'{link_mobile}{i}.json')
                sleep(1)
                cabeçalho('Exclusão Completa')
                sleep(1)
                input('\n\033[032mAperte Enter para retornar ao Menu Principal...\033[m')
                print('\n')
                menu_funcionario()
    except KeyboardInterrupt:
        interromper()

# Aqui segue 7 funções para o municipe
# Função para registrar o usuário no municipe.txt
def cadastro():
    limpar()
    cabeçalho('Tela de Cadastro')
    try:
        cont = 0
        while True:  # Validação do input nome
            if cont == 3:
                break
            else:
                print()
                nome = str(input('Nome: ')).title()
                if len(nome) < 4:
                    print()
                    erro('Necessário no mínimo 4 letras')
                    print()
                    sleep(1)
                    cont += 1
                else:
                    if nome.isalpha():
                        cont = 0
                        break
                    else:
                        cont += 1
                        erro('Só aceita letras')
        if cont < 3:
            while True:  # Validação do input senha
                if cont > 4:
                    break
                print()
                senha = str(input('Senha: ')).upper().strip()
                if len(senha) < 6:
                    cont += 1
                    erro('6 digitos no minimo')
                    sleep(1)
                if senha.isalnum() and len(senha) > 5:
                    cont = 0
                    break
                if not senha.isalnum():
                    cont += 1
                    erro('A senha só aceita letras e números')
                    sleep(1)
        else:
            cont += 2
        if cont < 4:
            while True:  # Validação da confirmação de senha
                if cont == 3:
                    break
                print()
                confsenha = str(input('Confirmar a Senha: ')).upper().strip()
                if confsenha == senha:
                    cont = 0
                    print()
                    break
                else:
                    cont += 1
                    print()
                    erro('Senha não corresponde')
                    print()
                    sleep(1)
        if cont < 3:
            while True:  # Validação do input e-mail
                try:
                    if cont == 3:
                        break
                    email = str(input('E-mail: ')).lower().strip()
                    email = f'municipe{email}'
                    user = auth.create_user_with_email_and_password(email, senha)
                    certo('Cadastro feito com sucesso')
                    sleep(1)
                    cont = 0
                    break
                except:
                    cont += 1
                    erro('E-mail está incorreto ou já existe')
        if cont < 3:
            opcoes_login()
        else:
            erro('Foram muitas tentativas, vamos encerrar o programa...')
            sleep(1)
            finalizar()
    except KeyboardInterrupt:
        interromper()

def opcoes_login():
    limpar()
    cabeçalho('Login do Cidadão')
    opcoes = ['Logar', 'Cadastrar-se']  # Lista de opções do municipe
    for k, v in enumerate(opcoes):
        sleep(0.3)
        print(f'\033[034m{k + 1}- {v}')
        if k == len(opcoes) - 1:
            sleep(0.3)
            print(f'{k + 2}- Sair\033[m')
            sleep(0.3)
    while True:  # Validação do input
        try:
            linha()
            conta = int(input('Qual sua opção: '))
            if conta < 1 or conta > 3:
                print('\n\033[031mNão existe esta opção...\033[m')
                sleep(1)
            else:
                break
        except ValueError:
            erro('Valor Inválido')
    if conta == 2:  # Cadastro
        linha()
        cabeçalho('Abrindo Tela de Cadastro')
        linha()
        sleep(2)
        cadastro()
    if conta == 3:  # Sair
        finalizar()
    else:
        sleep(1)  # Login
        print('\n')
        cabeçalho('Você está sendo direcionado...')
        login_municipe()

# Função da tela de login do municipe
def login_municipe():
    sleep(2)
    print()
    try:
        linha()
        cabeçalho('Tela de Login')
        sleep(0.5)
        cont = 0
        while True:
            try:
                if cont == 3:
                    break
                nome = input('nome: ').title().strip()
                print()
                email = input('E-mail: ').lower().strip()
                email = f'municipe{email}'
                print()
                senha = input('Senha: ').upper().strip()
                login = auth.sign_in_with_email_and_password(email, senha)
                print()
                cabeçalho('Acesso Permitido')
                sleep(1)
                break
            except:
                cont += 1
                erro('E-mail ou senha  inválido')
        if cont == 3:
            erro('Foram muitas tentativas, estamos retornando...')
            sleep(1)
            opcoes_login()
        else:
            logado.append(nome)
            menu_municipe()
    except(KeyboardInterrupt):
        interromper()

# Função para retornar ao menu principal do usuario
def menu_municipe():
    linha()
    limpar()
    print('\n')
    print(f'\033[032m{"Abrindo o Menu Principal...":^50}\033[m')
    print('\n' * 5)
    sleep(2)
    limpar()
    opcoes_municipe()

# Função que abre a tela inicial com opções para o municipe, de registro, consulta ou sair
def opcoes_municipe():
    cabeçalho('MENU PRINCIPAL')
    # colocando opções em uma lista e printando como opções
    opcoes = ['Abrir uma reclamação', 'Consultar reclamações em aberto']
    for k, v in enumerate(opcoes):
        sleep(0.3)
        print(f'\033[034m{k + 1}- {v}')
        if k == len(opcoes) - 1:
            sleep(0.3)
            print(f'{k + 2}- Sair\033[m')
    # Validação das opções da tela inicial
    try:
        while True:
            try:
                linha()
                sleep(1)
                processo = input('\033[035mDigite o número da opção que dejesa executar? \033[m')
                processo = int(processo)
                if processo < 1 or processo > len(opcoes) + 1:
                    print('\n\033[031mNão existe esta opção...\033[m')
                    sleep(1)
                else:
                    break
            except ValueError:
                erro('Valor Inválido')
        # Direcionamento de acordo com a escolha
        if processo == 1:  # Abrir uma Reclamação
            print(f'\n{"Abrindo opções de reclamação...":^40}')
            sleep(3)
            # system('clear')
            reclamar()
        if processo == 2:  # Consultar
            print('\n')
            cabeçalho('Carregando Opções de Consulta...')
            sleep(2)
            consultar_municipe()
        if processo == 3:  # Sair
            finalizar()
    except KeyboardInterrupt:
        interromper()

# Função para abrir uma reclamação
def reclamar():
    cabeçalho('TELA DE RECLAMAÇÃO')
    sleep(1)
    print('\n' * 2)
    cabeçalho('Opções de Reclamação')
    # colocando opções em uma lista e printando como opções
    opcoes_problema = ['Iluminação', 'Buraco', 'Entulho', 'Lixo', 'Boca de lobo', 'Outros']
    for k, v in enumerate(opcoes_problema):
        print(f'\033[35m{k + 1}- {v}\033[m')
        sleep(0.3)
        if k == len(opcoes_problema) - 1:
            sleep(0.3)
            print(f'\033[35m{k + 2}- Retornar ao Menu Principal\033[m')
        # Validação da escolha de opções de problema
    try:
        while True:
            try:
                linha()
                problema = int(input('Digite o número da opção do problema? '))
                linha()
                # colocando opções em uma lista e printando como opções
                opcoes_problema = ['Iluminacao', 'Buraco', 'Entulho', 'Lixo', 'Boca de lobo', 'Outros']
                if problema == len(opcoes_problema) + 1:  # Sair
                    break
                if problema < 1 or problema >= len(opcoes_problema) + 1:
                    print()
                    erro('Não existe esta opção')
                # Validação da escolha de opções de problema
                else:
                    print(f'Tipo de Problema: \033[033m{opcoes_problema[problema - 1]}\033[m')
                    problema = opcoes_problema[problema - 1]  # Problema que será usado para registro
                    break
            except ValueError:
                erro('Valor Incorreto')
        if problema == len(opcoes_problema) + 1:
            cabeçalho('Retornando ao Menu Principal...')
            sleep(2)
            opcoes_municipe()
        else:
            tamanho = requests.get(f'{link_sistema}.json')
            dict_tamanho = tamanho.json()
            terminal = len(dict_tamanho) + 1
            terminal = str(terminal)
            if len(terminal) == 1:  # Ajustando terminal para quando ele ficar com 1 digito
                protocolo = '1900' + str(terminal) + '/' + ano
            if len(terminal) == 2:  # Ajustando terminal para quando ele ficar com 2 digitos
                protocolo = '190' + str(terminal) + '/' + ano
            if len(terminal) == 3:  # Ajustando terminal para quando ele ficar com 3 digitos
                protocolo = '19' + str(terminal) + '/' + ano
            print()
            bairro = input('Bairro: ').strip().upper()
            print()
            rua = input('Rua: ').strip().capitalize()
            print()
            numero = input('Número: ').strip().capitalize()
            print()
            descricao = input('Descrição do problema: ').strip().capitalize()
            # Guardando informações no banco de dados firebase
            dados_registro = {'Protocolo': protocolo, 'Funcionario': 'Municipe', 'Requerente': logado[0], 'Problema': problema, 'Bairro': bairro,
                              'Rua': rua, 'Numero': numero, 'Data': data, 'Hora': hora, 'Etapa': 'Em analise', 'Descricao': descricao,'Unidade': 'Atendimento'}
            requisicao_mobile = requests.post(f'{link_mobile}.json', data=json.dumps(dados_registro))
            linha()
            print('\n')
            cabeçalho('REGISTRO BEM SUCEDIDO')
            sleep(1)
            print('\n')
            cabeçalho(f"Número de Protocolo gerado: {protocolo}")
            input('\nAperte enter para Continuar ')
            menu_municipe()
    except(KeyboardInterrupt):
        interromper()

# Função para consultar registros filtrados na visão do funcionario
def consultar_municipe():
    try:
        dados = requests.get(f'{link_sistema}.json')
        dict_dados = dados.json()
        # Alimentando o dicionário para filtragem
        for i in dict_dados:
            date = dict_dados[i]["Data"]
            dict_dados[i]['Mes'] = str(date[2:5]).strip('/')
            dict_dados[i]['Ano'] = str(date[5:]).strip('/')
        lista = []# Variável para pega registros em nome do usúario
        for i in dict_dados:
            if logado[0] == dict_dados[i]['Requerente']:
                lista.append(dict_dados[i])
        if len(lista) == 0:
            sleep(0.5)
            print(f'{lilas}Não foi encontrado nada no nome de {logado[0]} \033[m')
            print(f'{lilas}Pode ser que o seu processo ainda não caiu no sistema\033[m')
            input('\nAperte enter para continuar...')
            consultar_municipe()
        else:
            limpar()
            cabeçalho('IMPRIMINDO DADOS')
            print('\n' * 4)
            sleep(2)
            limpar()
            # colocando opções em uma lista para cabeçalho do print
            linha()
            print(f'Protocolos aberto por\033[035m {logado[0]}\033[m')
            print()
            linha()
            prot = []
            for i in lista:
                for v in i.items():
                    if v[0] == 'Protocolo':
                        prot.append(v[1])
            prot.sort()
            n = ''
            for i in prot:
                if n != i:
                    print(f'{azul}{i}\033[m')
                n = i
            print()
            linha()
            sleep(0.5)
            input('\n\033[032mAperte enter para continuar...\033[m  ')
            valores = []
            protocolo = input('\nDigite o número do protocolo que você deseja consultar[ex: 19000/2020]: ').strip()
            for valor in lista:
                if protocolo == valor["Protocolo"]:
                    valores.append(valor)
            if len(valores) == 0:
                sleep(0.5)
                print(f'{lilas}Não foi encontrado nada no Protocolo {protocolo} \033[m')
                print(f'{lilas}Pode ser que o seu processo ainda não caiu no sistema\033[m')
                input(f'\n{verde}Aperte enter para continuar...\033[m')
                opcoes_municipe()
            else:
                variaveis = {}
                for i in valores:
                    variaveis = i
                sleep(1)
                limpar()
                cabeçalho('DADOS')
                print(f'{"Protocolo Nº "}{verde}{variaveis["Protocolo"]:<35}\033[m {"Data da Consulta: "}{verde}{data}\033[m')
                sleep(0.5)
                linha()
                print(f'{"Unidade de origem: "}{verde}Secretaria de {variaveis["Unidade"]:<15}\033[m {"Ultima Atualização: "}{verde}{variaveis["Data"]}\033[m')
                sleep(0.5)
                linha()
                print(f'Assunto: {verde}{variaveis["Problema"]}\033[m')
                sleep(0.5)
                linha()
                print(f'Funcionário responsável: {verde}{variaveis["Funcionario"]}\033[m')
                sleep(0.5)
                linha()
                print(f'Requerente: {verde}{variaveis["Requerente"]}\033[m')
                sleep(0.5)
                linha()
                print(f'Descrição do problema: {verde}{variaveis["Descricao"]}\033[m')
                sleep(0.5)
                linha()
                print(f'Status do processo: {verde}{variaveis["Etapa"]}\033[m')
                linha()
                while True:
                    atualizacao = input(f"\nDeseja ver os detalhes do andamento{verde}[S/N]? \033[m").strip().upper()
                    if atualizacao == 'S':
                        lista_atualizada = []
                        for i in valores:
                            lista_atualizacao = []
                            lista_atualizacao = [i['Data'], i["Funcionario"], i["Unidade"], i["Descricao"]]
                            lista_atualizada.append(lista_atualizacao[:])
                        lista_atualizada.reverse()
                        linha()
                        print(f'\033[036m{"Data":<20}{"Funcionario":<20}{"Secretária":<20}{"Ato":<20}\033[m')
                        linha()
                        contador = 0
                        for l in range(len(lista_atualizada)):
                            for c in range(len(lista_atualizacao)):
                                if contador % 2 == 0:
                                    contador += 1
                                    print(f'{azul}{lista_atualizada[l][c]:<20}\033[m', end='')
                                else:
                                    contador += 1
                                    print(f'{lilas}{lista_atualizada[l][c]:<20}\033[m', end='')
                            print()
                        print()
                        linha()
                        break
                    else:
                        break
                sleep(0.5)
                input('\n\033[035mAperte enter para voltar ao Menu Principal\033[m  ')
                menu_municipe()
    except KeyboardInterrupt:
        interromper()

# Função que starta o programa, chamando no fim para ele reconhecer todas as funções e variáveis
inicio()
