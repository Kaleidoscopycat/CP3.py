# Projeto de Sistema de Gerenciamento de Tarefas
Este projeto consiste na criação de um sistema de gerenciamento de tarefas, que permitirá aos
usuários cadastrar, listar, atualizar e remover tarefas. O sistema deve ter as seguintes
funcionalidades:
1. Cadastro de Tarefas: Os usuários poderão cadastrar novas tarefas, informando uma descrição,
uma data de vencimento e o status da tarefa (pendente, em andamento, concluída).
2. Listagem de Tarefas: Os usuários poderão listar todas as tarefas cadastradas, podendo filtrar por
status (pendente, em andamento, concluída) ou por data de vencimento.
3. Atualização de Tarefas: Os usuários poderão atualizar o status das tarefas (marcar como
concluída, por exemplo) ou editar informações como descrição e data de vencimento.
4. Remoção de Tarefas: Os usuários poderão remover tarefas cadastradas.
5. Persistência de Dados: As tarefas cadastradas devem ser armazenadas de forma persistente,
salvando em arquivos.
6. Interface de Usuário: O sistema deve ter uma interface simples para interação com o usuário,
podendo ser uma interface de linha de comando ou uma interface gráfica.
Além das funcionalidades básicas mencionadas acima, o sistema pode ser expandido para incluir
outras funcionalidades, como a capacidade de lidar com tarefas recorrentes, prioridades,
categorias, etc.

A estrutura do projeto poderia ser dividida em módulos separados para cada funcionalidade, com
funções específicas para cada parte do sistema. Por exemplo:
• tarefas.py: Contém as funções para cadastrar, listar, atualizar e remover tarefas.
• persistencia.py: Contém as funções para salvar e carregar tarefas de um arquivo ou banco de
dados.
• interface.py: Contém a interface de usuário para interagir com o sistema.
