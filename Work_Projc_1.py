from os import system
from colorama import init, Fore, Back, Style
from getpass import getpass
import getpass
from time import sleep
import stdiomask


init(autoreset=True)

def exibirMenu():
    print(Fore.GREEN + '''
        Bem Vindo 

        Sistema de Login    

        Escolha a Opção 
        [1]Cadastro de Usuario
        [2]Fazer Login
        [3]Sair
    ''')
    opcao = int(input("Digite sua opção"))
    return(opcao)

def fazerLogin():
    login = input('Nome :')
    senha = input('Senha :')
    return(login, senha)

def buscarUsuario(Login,senha):
    usuarios = []
    try:
        with open('usuarios.txt','r+', encoding='Utf-8', newline='' ) as arquivo:
            for linha in arquivo:
                linha = linha.strip(",")
                usuarios.append(linha.split())
            for usuario in usuarios:
                nome = usuario[0]
                password = usuario[1]
                if Login == nome and senha == password:
                    return True
    except FileExistsError:
        return False    

while True:
    system('cls')  # Limpa o terminal

    opcao = exibirMenu()

    system('cls') 

    if opcao == 1:
        login, senha = fazerLogin()
        if login == senha:
            print('Sua senha deve ser diferente do seu login.')
            senha = input("senha :")
        user = buscarUsuario(login, senha)
        if user == True :
            print(Fore.RED + 'Usuario Já existente')
            sleep(2)
        else:
            with open('usuarios.txt', 'a+', encoding='Utf-8',newline='') as arquivo:
                arquivo.writelines(f'{login} {senha}\n')
            print( 'Cadastro Aprovado!')
            exit() 

    elif opcao == 2:
        login , senha = fazerLogin()
        user = buscarUsuario(login, senha)
        if user == True:
            print("Login realizado com sucesso!")
            sleep(1)
            exit()
        else:
            print("Seu login é invalido!")
            sleep(2)    
    else:
        system("cls")
        print("GoodBay")
        break        