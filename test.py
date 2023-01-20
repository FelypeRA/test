import os

# fazer aparecer o menu na tela  
def menu():
  global opção
  print('-'*60)
  print(f'{"ferramenta para cadastro de funcionarios":^60}')
  print('-'*60)
  print('         [ 1 ] Para cadastrar um funcionário. ')
  print('         [ 2 ] Para ver lista de funcionários.')
  print('         [ 3 ] Para excluir um funcionario.   ')
  print('         [ 4 ] Sair do programa.              ')
  print('-' * 60)

  

# Função para cadastrar um funcionario na lista 
def cadastro():
  os.system('clear')
  while True:
    print('-'*30)
    print(f'{"CADASTRO":^30}')
    print('-'*30)
    funcionario = dict()
    funcionario['nome'] = (str(input('Nome do funcionário: ')))
    funcionario['idade'] = (int(input('Qual a idade: ')))
    funcionario['função'] = (str(input('Qual a função: ')))
    funcionario['CPF'] = (str(input('CPF: ')))
    funcionario['Endereço'] = (str(input('Endereço: ')))
      
    funcionarios.append(funcionario.copy())
    funcionario.clear()
    print(f'{"Funcionario cadastrado com sucesso!":^60}')
    print('---'*20)
    
    continuar = str(input('Fazer novo cadastro? '))
    if continuar in 'Nn':
      os.system('clear')
      break


# Função que lista os funcionarios 




def listarfuncinarios():
  os.system('clear')
  global funcionarios
  print('-'* 71)
  print('|ID                 NOME                          FUNÇÃO               |')
  for index,lin in enumerate(funcionarios):
    print(f'|{index:0>2}', end = '        ')
    print(f"{lin['nome']:<30}", end = '')
    print(f"{lin['função']:<30}|", end = '')
    print('') 
  print('-'* 71)

  
# Excluir funcionario da lista
def excluifuncionario(): 
  listarfuncinarios()
  id = int(input('Digite o ID de quem deseja excluir: '))
  del funcionarios[id]

funcionarios = [
  {'nome': 'Felype Ramirez Alves', 'idade': 21, 'função': 'Desenvolvedor Python', 'CPF': '1234567', 'endereço': 'Foz do Iguaçu'},
  {'nome': 'Jorje', 'idade': 21, 'função': 'mecanico', 'CPF': '08545646546', 'endereço': 'Foz do Iguaçu'},
  {'nome': 'everton', 'idade': 21, 'função': 'Desenvolvedor Python', 'CPF': '1234567', 'endereço': 'Foz do Iguaçu'},
  {'nome': 'Felype Ramirez Alves', 'idade': 21, 'função': 'Desenvolvedor Python', 'CPF': '1234567', 'endereço': 'Foz do Iguaçu'},
]
cont = 0 
opção = 0
continuar = ''

while True: 
  menu()
  opção = int(input('Sua opção: '))
  os.system('clear')
  if opção == 1:
    cadastro()
  elif opção == 2:
    listarfuncinarios()
    id = int(input('Digite o ID do funcionário para mais informaçoes[-1 para voltar ao menu principal]: '))
    if id != -1:
      for key,item in funcionarios[id].items():
        print(f'{key}: {item}')
      print('')
    input('Precione qualquer tecla para voltar ao menu principal: ')
    os.system('clear')

  elif opção == 3:
    excluifuncionario()
  elif opção == 4:
    break
for index,item in enumerate(funcionarios):
  print(item)