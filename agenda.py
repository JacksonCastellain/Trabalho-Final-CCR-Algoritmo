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
  for i in range(len(eventos)):
    print(
        '\nData: ', eventos[i].data, 
        '\nHora: ', eventos[i].hora, 
        '\nDuração: ', eventos[i].duracao, 
        '\nDescrição: ',eventos[i].descricao 
        )
    print('#'*70) 

def listardata(eventos,data):
  for i in range(len(eventos)):
    if(eventos[i].data == data):
      print(
          'Data: ', eventos[i].data, 
          'Hora: ', eventos[i].hora, 
          'Duração: ', eventos[i].duracao, 
          'Descrição: ',eventos[i].descricao 
          )
    else:
      print('\nDatas com agendamentos: ',eventos[i].data
            )

def deletarTudo(eventos):
  if len(eventos) != 0:
    eventos.clear()
    print('\nTodos os contatos foram removidos!')
  else:
    print('\nA agenda está vazia!')

def deletardata(eventos, data):
  if len(eventos) != 0:
    for i in range(len(eventos)):
      if(eventos[i].data==data):
        eventos.pop(i)
        print("\nContato removido!")
        break

eventos = []

while True:
  print('\n1 - Inserir')
  print('2 - Listar')
  print('3 - Listar contato específico')
  print('4 - Deletar contato específico')
  print('5 - Deletar todos os contatos')
  print('6 - Sair.')

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
    data = input('Digite a data:')
    deletardata(eventos,data)
  elif op == 5:
    deletarTudo(eventos)
  elif op == 6:
    break
  else:
    print('Op Inválida!')