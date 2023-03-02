class Agenda():
  data = None
  hora = None
  duracao = None
  descricao = None


#Função que retorna se a lista de eventos está vazia
def listaVazia(eventos):
  if len(eventos) == 0:
    print('\n\t A agenda está vazia!')
    return True
  return False


#Função que insere eventos com verificação de mesma data e horário
def inserir(eventos,data,hora,duracao,descricao,e):
  e.data = data
  e.hora = hora
  e.duracao = duracao
  e.descricao = descricao
  for i in range(len(eventos)):
    if(eventos[i].data == data and eventos[i].hora == hora):
      print('\nJá existe um compromisso agendado para a mesma data e horário.')
      del e.data
      del e.hora
      del e.duracao
      del e.descricao
  return e


#Função que ordena por data e hora em ordem crescente
def ordenarEventos(eventos,e):
  e.data = Data(data)
  e.hora = hora.replace(':','')
  for i in range(len(eventos)):
    for j in range(0, len(eventos) - i - 1):
      if eventos[j].data > eventos[j + 1].data:
        temp = eventos[j]
        eventos[j] = eventos[j+1]
        eventos[j+1] = temp
      elif eventos[j].data == eventos[j].data:
        for i in range(len(eventos)):
          for j in range(0, len(eventos) - i - 1):
            if eventos[j].hora > eventos[j + 1].hora:
              temp = eventos[j]
              eventos[j] = eventos[j+1]
              eventos[j+1] = temp 


#Função que lista todos os eventos
def listar(eventos):
  if len(eventos) == 0:
      print('\n\t  A agenda está vazia!')
  for i in range(len(eventos)):
    if eventos[i].data == None:
      del eventos[i]
    else:
      ordenarEventos(eventos,e)
      #e.data = dataCorreta()
      print(
          '\nData: ', eventos[i].data,
          '\nHora: ', eventos[i].hora, 
          '\nDuração: ', eventos[i].duracao, 
          '\nDescrição: ',eventos[i].descricao 
          )
      print('#'*70)


#Função que lista um evento por data
def listarData(eventos,data):
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
 

#Função que lista um evento por data e hora
def listarHora(eventos,data,hora):
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


#Função que edita a duração e a descrição de um evento
def editarEvento(eventos,data,hora):
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
    print('\nCompromisso não encontrado')


#Função que deleta um evento específico
def deletarData(eventos, data,hora):
  flag = False
  for i in range(len(eventos)):
    if(eventos[i].data == data and eventos[i].hora == hora):
      eventos.pop(i)
      print("\n Evento removido!")
      flag = True
  if flag == False:
    print('\n Compromisso não encontrado')


#Função que deleta todos os eventos da agenda
def deletarTudo(eventos):
  if len(eventos) != 0:
    eventos.clear()
    print('\nTodos os eventos foram removidos!')
  else:
    print('\n\t A agenda está vazia!')


# 20/10/2023 => 20231020
def Data(data):
  new_data = data.split('/')[::-1]
  nova_data = ''
  nova_data = nova_data.join(new_data)
  return nova_data

#20231020 => 20/10/2023
def dataCorreta():
  f_data = Data(data)[:4]
  f_data1 = Data(data)[4:6]
  f_data2 = Data(data)[6:]
  f_n_data = f_data2 +'/' + f_data1 +'/'+ f_data
  return f_n_data


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

  try:
    op = int(input('Entre com a opção desejada: '))
  except:
    print('\n\tDigite somente números inteiros.')
    continue

  if op == 1:
      print('\tExemplo: dd/mm/aaaa')
      data = input('Digite a data: ')
      print('\tExemplo: hh:mm')
      hora = input('Digite o hora: ')
      duracao = input('Duração: ')
      descricao = input('Descrição: ')
      e = Agenda()
      eventos.append(inserir(eventos,data,hora,duracao,descricao,e))
  elif op == 2:
    listar(eventos)
  elif op == 3:
    if listaVazia(eventos) == True:
      continue
    else:
      data = input('Digite a data: ')
      listarData(eventos,data)
  elif op == 4:
    if listaVazia(eventos) == True:
      continue
    else:
      print('\t\tExemplo: dd/mm/aaaa')
      data = input('Digite a data: ')
      print('\t\tExemplo: hh:mm')
      hora = input('Digite o hora: ')
      listarHora(eventos,data,hora)
  elif op == 5:
    if listaVazia(eventos) == True:
      continue
    else:
      print('\t\tExemplo: dd/mm/aaaa')
      data = input('Digite a data: ')
      print('\t\tExemplo: hh:mm')
      hora = input('Digite o hora: ')
      editarEvento(eventos,data,hora)
  elif op == 6:
    if listaVazia(eventos) == True:
      continue
    else:
      print('\t\tExemplo: dd/mm/aaaa')
      data = input('Digite a data: ')
      print('\t\tExemplo: hh:mm')
      hora = input('Digite o hora: ')
      deletarData(eventos,data,hora)
  elif op == 7:
    deletarTudo(eventos)
  elif op == 8:
    break
  else:
    print('\nDigite um número dentro das opções!')


     
