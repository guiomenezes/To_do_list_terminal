from base_de_dados import criar_banco_de_dados, criar_tarefa, editar_tarefa, mostrar_tarefas, apagar_tarefa, mostrar_unica_tarefa, alterar_status
from time import sleep
from rich.console import Console

criar_banco_de_dados()

console = Console()

console.print("""
░▀█▀░█▀█░█▀▄░█▀▀░█▀▀░█▀█░█▀▀
░░█░░█▀█░█▀▄░█▀▀░█▀▀░█▀█░▀▀█
░░▀░░▀░▀░▀░▀░▀▀▀░▀░░░▀░▀░▀▀▀
""", style='green on yellow')

console.print('[bold purple]BEM VINDO![/]')
print('')
console.print('[bold purple]Escolha o número da opção que deseja.[/]')

while True:

    console.print(30 * '[bold white]-=[/]')
    console.print('[bold yellow]MENU[/]')
    console.print('[1] [green]Criar uma tarefa[/].\n[2] [green]Editar tarefa.[/]\n[3] [green]Excluir tarefa.[/]\n[4] [green]Exibir todas tarefas.[/]\n[5] [green]Concluir tarefa.[/]\n[6] [green]Sair[/]')
    console.print(30 * '[bold white]-=[/]')
    opcao = str(console.input('[bold green]OPÇÃO: [/]'))
    if opcao not in '123456':
        console.print('[bold red]OPÇÃO INVÁLIDA.[/]')
    if opcao in '123456':
        pass
    print('')

    if opcao == '1':
        descricao = str(input('Descreva a tarefa: '))
        criar_tarefa(descricao)
        print('')
        console.print('[bold green]Tarefa criada com sucesso![/]')
        print('')
        sleep(2)

    if opcao == '2':
        while True:
            try:
                while True:
                    id = int(input('Digite o ID da tarefa que deseja alterar: '))
                    mostrar_unica_tarefa(id)
                    tarefa = mostrar_unica_tarefa(id)
                    if tarefa is None:
                        console.print('[bold red]ID da tarefa não encontrado.[/]')
                    else:
                        print('')
                        console.print(f'[bold]ID:[/] [bold blue]{id}[/]\n[bold]Descrição:[/] [bold blue]{tarefa[0]}[/]\n[bold]Data e hora:[/] [bold blue]{tarefa[1]}[/]')
                        console.print('[bold]Status:[/] [bold blue]Concluída[/]' if tarefa[2] == 1 else '[bold]Status:[/] [bold blue]Pendente[/]')
                        print('')
                        break
                nova_descricao = str(input('Edite a descrição da tarefa: '))
                while True:
                    tarefa_concluida = str(input('Essa tarefa foi concluida? [1]Sim | [2]Não: '))
                    if tarefa_concluida not in '12':
                        console.print('[bold red]OPÇÃO INVÁLIDA.[/]')
                    else:
                        break
                if tarefa_concluida == '1':
                    concluida = 1
                else:
                    concluida = 0
                editar_tarefa(id, nova_descricao, concluida)
                print('')
                console.print('[bold green]Tarefa editada com sucesso![/]')
                print('')
                sleep(2)
                break
            except ValueError or NameError:
                console.print('[bold red]OPÇÃO INVÁLIDA.[/]')

    if opcao == '3':
        while True:
            try:
                while True:
                    id = int(input('Digite o ID da tarefa que deseja excluir: '))
                    mostrar_unica_tarefa(id)
                    tarefa = mostrar_unica_tarefa(id)
                    if tarefa is None:
                        console.print('[bold red]ID da tarefa não encontrado.[/]')
                    else:
                        console.print(f'[bold]ID:[/] [bold blue]{id}[/]\n[bold]Descrição:[/] [bold blue]{tarefa[0]}[/]\n[bold]Data e hora:[/] [bold blue]{tarefa[1]}[/]')
                        console.print('[bold]Status:[/] [bold blue]Concluída[/]' if tarefa[2] == 1 else '[bold]Status:[/] [bold blue]Pendente[/]')
                        break
                print('')
                while True:
                    perg = str(console.input(f'[bold]Tem certeza que deseja excluir a tarefa[/] {id}? [1]Sim | [2]Não: '))
                    if perg == '1':
                        apagar_tarefa(id)
                        console.print('[bold green]Tarefa excluída com sucesso![/]')
                        break
                    elif perg == '2':
                        print('Exclusão cancelada.')
                        break 
                    elif perg not in '12':
                        console.print('[bold red]OPÇÃO INVÁLIDA.[/]')   
                print('')
                sleep(2)
                break
            except ValueError or NameError:
                console.print('[bold red]OPÇÃO INVÁLIDA.[/]')

    if opcao == '4':
        tarefas = mostrar_tarefas()
        for campo_id, campo_descricao, campo_data, campo_status in tarefas:
            console.print(f'[bold]ID:[/] [bold blue]{campo_id}[/]')
            console.print(f'[bold]Descrição:[/] [bold blue]{campo_descricao}[/]')
            console.print(f'[bold]Data:[/] [bold blue]{campo_data}[/]')
            console.print('[bold]Status:[/] [bold blue]Concluída[/]' if campo_status == 1 else '[bold]Status: [/][bold blue]Pendente[/]')
            console.print(30 * '[bold white]==[/]')

    if opcao == '5':
        while True:
            try:
                while True:
                    id = int(input('Digite o ID da tarefa que deseja mudar o status: '))
                    mostrar_unica_tarefa(id)
                    tarefa = mostrar_unica_tarefa(id)
                    if tarefa is None:
                        console.print('[bold red]ID da tarefa não encontrado![/]')
                    else:
                        console.print(f'[bold]ID:[/] {id}\n[bold]Descrição:[/] {tarefa[0]}\n[bold]Data e hora:[/] {tarefa[1]}')
                        console.print('[bold]Status:[/] [bold blue]Concluída[/]' if tarefa[2] == 1 else '[bold]Status:[/] [bold blue]Pendente[/]')
                        break
                while True:
                    status = str(input('Deseja mudar o status dessa tarefa? [1]Concluída | [2]Pendente: '))
                    if status not in '12':
                        console.print('[bold red]OPÇÃO INVÁLIDA.[/]')
                    else:
                        break
                alterar_status(id, status)
                console.print(f'[bold white]Alterando status da tarefa[/] [bold blue]{id}[/].')
                sleep(2)
                console.print('[bold green]Status alterado com sucesso![/]')
                break
            except ValueError or NameError:
                console.print('[bold red]OPÇÃO INVÁLIDA.[/]')

    if opcao == '6':
        console.print('[bold white]Encerrando o programa![/]')
        sleep(2)
        print('')
        break
        