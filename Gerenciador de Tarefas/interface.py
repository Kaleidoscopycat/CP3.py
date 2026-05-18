import tarefas
#Interface de Usuário
def interface():
  while opcaoescolhida != int and 0<opcaoescolhida<6:
    print("""Menu:
      1 - Cadastrar Tarefa
      2 - Listar Tarefas
      3 - Atualizar Tarefa
      4 - Remover Tarefa
      5 - Sair""")
    opcaoescolhida = input("Selecione uma opção: ")
    if opcaoescolhida != int:
      print("\nOpção Inválida!")
  match int(opcaoescolhida):
    case 1:
      print("\nCadastrando nova tarefa...\n")
      tarefas.cadastrar_nova_tarefa()
    case 2:
      print("\nListando tarefas...\n")
      tarefas.listar_tarefas()
    case 3:
      print("\nAtualizando tarefa...\n")
      tarefas.atualizar_tarefa()
    case 4:
      print("\nRemovendo tarefa...\n")
      tarefas.remover_tarefa()
    case 5:
      print("Encerrando...")
