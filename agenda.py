class Agenda():
  data = None
  hora = None
  duracao = None
  descricao = None


def inserir(e):
  e.data = input('\nData: ')
  e.hora = input('Hora: ')
  e.duracao = input('Duração: ')
  e.descricao = input('Descrição: ')
  return e


def listar(eventos):
  if len(eventos) == 0:
      print('\n\t  Agenda vazia.')
  for i in range(len(eventos)):
      print(
          '\nData: ', eventos[i].data, 
          '\nHora: ', eventos[i].hora, 
          '\nDuração: ', eventos[i].duracao, 
          '\nDescrição: ',eventos[i].descricao 
          )
      print('#'*70) 


def listardata(eventos,data):
  if len(eventos) == 0:
    print('\n\tA agenda está vazia!')
    flag = False
    for i in range(len(eventos)):
      if(eventos[i].data == data):
        print(
            '\nData: ', eventos[i].data, 
            '\nHora: ', eventos[i].hora, 
            '\nDuração: ', eventos[i].duracao, 
            '\nDescrição: ',eventos[i].descricao 
            )
        print('#'*70)
        flag = True
    if flag == False:
      print('\nAgenda Vazia')
  else:
    print('\nA agenda está vazia!')


def listar_hora(eventos,data,hora):
  if len(eventos) != 0:
    flag = False
    for i in range(len(eventos)):
      if(eventos[i].data == data and eventos[i].hora == hora):
        print(
            '\nHora: ', eventos[i].hora, 
            '\nDuração: ', eventos[i].duracao, 
            '\nDescrição: ',eventos[i].descricao 
            )
        print('#'*70) 
        flag = True
    if flag == False:
      print('\nAgenda Vazia')
  else:
    print('\nA agenda está vazia!') 


def editar_evento(eventos,data,hora):
  if len(eventos) != 0:
    flag = False
    for i in range(len(eventos)):
      if(eventos[i].data == data and eventos[i].hora == hora):
        print(
            '\nDuração: ', eventos[i].duracao, 
            '\nDescrição: ',eventos[i].descricao 
            )
        print('#'*70)
        print()
        eventos[i].duracao, = input('Nova duração: ')
        eventos[i].descricao  = input('Nova descrição: ')
        flag = True
    if flag == False:
      print('\nAgenda Vazia')
  else:
    print('\nA agenda está vazia!')


def deletarTudo(eventos):
  if len(eventos) != 0:
    eventos.clear()
    print('\nTodos os contatos foram removidos!')
  else:
    print('\nA agenda está vazia!')


def deletardata(eventos, data):
  if len(eventos) != 0:
    flag = False
    for i in range(len(eventos)):
      if(eventos[i].data==data):
        eventos.pop(i)
        print("\nContato removido!")
        flag = True
    if flag == False:
      print('\nAgenda Vazia Nesta Data')
  else:
    print('\nA agenda está vazia!')


eventos = []

while True:
  print('\n1 - Inserir')
  print('2 - Listar')
  print('3 - Listar evento específico pela data')
  print('4 - Listar um evento específico pela data e pela hora')
  print('5 - Editar')
  print('6 - Deletar evento específico')
  print('7 - Deletar todos os eventos')
  print('8 - Sair.')


  op = int(input('Entre com a opção desejada: '))

  if op == 1:
      e = Agenda()
      eventos.append(inserir(e))
  elif op == 2:
    listar(eventos)
  elif op == 3:
    data = input('Digite a data:')
    listardata(eventos,data)
  elif op == 4:
    data = input('Digite a data: ')
    hora = input('Digite o hora: ')
    listar_hora(eventos,data,hora)
  elif op == 5:
    data = input('Digite a data: ')
    hora = input('Digite o hora: ')
    editar_evento(eventos,data,hora)
  elif op == 6:
    data = input('Digite a data:')
    deletardata(eventos,data)
  elif op == 7:
    deletarTudo(eventos)
  elif op == 8:
    break
  else:
    print('\nDigite um número dentro das opções!')