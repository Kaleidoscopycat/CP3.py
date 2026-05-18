#Cadastro de tarefas
def cadastrar_nova_tarefa():
  novaTarefa = {}
  accept = False
  while accept == False:
    print("Para cadastrar uma nova tarefa, informe nome, descrição, data de vencimento e status da tarefa")
    novaTarefa["titulo"] = input("Nome: ")
    novaTarefa["descricao"] = input("Descrição: ")
    novaTarefa["data_de_vencimento"] = input("Data de vencimento: ")
    status = input("""Selecione um status:
    1 - Pendente
    2 - Em Andamento
    3 - Concluído
    """)
    match status:
      case 1:
        novaTarefa["status"] = "Pendente"
      case 2:
        novaTarefa["status"] = "Em Andamento"
      case 3:
        novaTarefa["status"] = "Concluído"

    print(novaTarefa)
    confirmacao = input("\npressione y para confirmar ou qualquer outra tecla para cancelar: ")
    if confirmacao == "y":
      accept = True
  return novaTarefa

#Listagem de Tarefas
def listar_tarefas():
  
#Atualização de Tarefas
def atualizar_tarefa():
  print("a")
#Remoção de Tarefas
def remover_tarefa():
  print("a")
