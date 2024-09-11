from classe import *

if __name__ == '__main__':
    # entrada de dados
    nome = input('Informe o nome: ')
    idade = int(input('Informe a idade: '))
    email = input('Informe o e-mail: ')

    # instancia da classe
    usuario = Pessoa(nome, idade, email)

    # saída de dados
    print(f'\nNome: {usuario.nome}.')
    print(f'Idade: {usuario.idade}.')
    print(f'E-mail: {usuario.email}.')