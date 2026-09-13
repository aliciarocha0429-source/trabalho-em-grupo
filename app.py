from pessoas import Pessoa, Investigador, Suspeito, Testemunhas
from classes import Caso, Evidencia, Local
from depoimentos import Depoimentos
from relatorio import Relatorio
casos = []

def cadastrar_caso():
    dados = input("\nCADASTRANDO CASO\nDigite separado pro virgula o Numero do caso, titulo, descrição, dificuldade: ").split(",")
    caso = Caso(*dados)
    casos.append(caso)
    print("CASO CADASTRADO COM SUCESSO!")

def escolher_caso():
    if len(casos) == 0:
        print("Nenhum caso registrado!")
    else:
        print("\nCASOS REGISTRADOS: ")
        for n in range(len(casos)):
            print(f"{n+1} - {casos[n].titulo}")
        caso_escolhido = (int(input("Digite o numero do caso que voce quer acessar: ")))-1
        if 0 <= caso_escolhido < len(casos):
            menu_segundo(casos[caso_escolhido])
        else:
            print("Caso nao encontrado!")
def gerenciar_investigadores(caso):
    while True:
        controle_investigadores = int(input("\nINFORMATICOS INVESTIGATION\n1 — Cadastrar investigador\n2 — Listar investigadores\n3 — Alterar cargo\n4 — Alterar departamento\n0 — Voltar "))

        if controle_investigadores == 1:
            dados = input("\nCADASTRANDO INVESTIGADOR: \nDigite separado pro virgula o nome do investigador, data de nascimento, cpf, genero, telefone, endereco, registro funcional, cargo, departamento: ").split(",")

            investigador = Investigador(*dados)

            caso.adicionar_investigador(investigador)

            print("INVESTIGADOR ADICIONADO COM SUCESSO!")

        elif controle_investigadores == 2:
            caso.mostrar_investigadores()

        elif controle_investigadores == 3:
            if len(caso.investigador) == 0:
                print("Nenhum investigador registrado!")
            else:
                print("\nINVESTIGADORES REGISTRADOS: ")
                for n in range(len(caso.investigador)):
                    print(f"{n+1} - {caso.investigador[n].get_nome_investigador()}")
                investigador_escolhido = (int(input("Digite o numero do investigador que voce quer mudar o cargo: ")))-1

                caso.investigador[investigador_escolhido].set_cargo()

        elif controle_investigadores == 4:
            if len(caso.investigador) == 0:
                print("Nenhum investigador registrado!")
            else:
                print("\nINVESTIGADORES REGISTRADOS: ")
                for n in range(len(caso.investigador)):
                    print(f"{n+1} - {caso.investigador[n].get_nome_investigador()}")

                investigador_escolhido = (int(input("Digite o numero do investigador que voce quer mudar o departamento: ")))-1

                caso.investigador[investigador_escolhido].set_departamento()
        elif controle_investigadores == 0:
            return
        else:
            print("Opção Invalida!")

def gerenciar_suspeitos(caso):
    while True:
        controle_suspeitos = int(input("\nINFORMATICOS INVESTIGATION\n1 — Cadastrar suspeito\n2 — Listar suspeitos\n3 — Alterar status de custódia\n0 — Voltar "))

        if controle_suspeitos == 1:
            dados = input("\nCADASTRANDO SUSPEITO: \nDigite separado pro virgula o nome do suspeito, data de nascimento, cpf, genero, telefone, endereco, status da custodia, caracteristicas(separado por espaço ou por ponto e virgula): ").split(",")

            suspeito = Suspeito(*dados)

            caso.adicionar_suspeito(suspeito)

            print("SUSPEITO ADICIONADO COM SUCESSO!")

        elif controle_suspeitos == 2:
            caso.mostrar_suspeitos()

        elif controle_suspeitos == 3:
            if len(caso.suspeitos) == 0:
                print("Nenhum suspeito registrado!")
            else:
                print("\nSUSPEITOS REGISTRADOS: ")
                for n in range(len(caso.suspeitos)):
                    print(f"{n+1} - {caso.suspeitos[n].get_nome_suspeito()}")
                suspeito_escolhido = (int(input("Digite o numero do suspeito que voce quer mudar o status da custodia: ")))-1

                caso.suspeitos[suspeito_escolhido].set_status_custodia()

        elif controle_suspeitos == 0:
            return
        else:
            print("Opção Invalida!")

def gerenciar_testemunhas(caso):
    while True:
        controle_testemunhas = int(input("\nINFORMATICOS INVESTIGATION\n1 — Cadastrar testemunha\n2 — Listar testemunha\n3 — Alterar tipo de testemunha\n0 — Voltar "))

        if controle_testemunhas == 1:
            dados = input("\nCADASTRANDO TESTEMUNHA: \nDigite separado pro virgula o nome da testemunha, data de nascimento, cpf, genero, telefone, endereco, tipo de testemunha: ").split(",")

            testemunha = Testemunhas(*dados)

            caso.adicionar_testemunha(testemunha)

            print("TESTEMUNHA ADICIONADO COM SUCESSO!")

        elif controle_testemunhas == 2:
            caso.mostrar_testemunhas()

        elif controle_testemunhas == 3:
            if len(caso.testemunhas) == 0:
                print("Nenhuma testemunha registrado!")
            else:
                print("\nTESTEMUNHA REGISTRADOS: ")
                for n in range(len(caso.testemunhas)):
                    print(f"{n+1} - {caso.testemunhas[n].get_nome_testemunha()}")
                testemunha_escolhido = (int(input("Digite o numero da testemunha que voce quer alterar o tipo: ")))-1

                caso.testemunhas[testemunha_escolhido].set_tipo_testemunha()

        elif controle_testemunhas == 0:
            return
        else:
            print("Opção Invalida!")

def gerenciar_relatorio(caso):
    if caso.relatorio is None:
        caso.relatorio = Relatorio(caso)
    relatorio_do_caso = caso.relatorio
    while True:
        controle_relatorio = int(input(f"\nRELATORIO DO CASO {caso.titulo}\n1- Ver relatorio geral\n2 - Adicionar evidencias\n3 - Adicionar local\n4 - Adicionar depoimento\n0 - Voltar "))

        if controle_relatorio == 1:
            caso.relatorio.get_gerar_relatorio()

        elif controle_relatorio == 2:
            dados = input("\nCADASTRANDO EVIDENCIAS: \nDigite separado pro virgula o codigo da evidencia, descricao, local encontrado, data e hora, relevancia: ").split(",")

            evidencia = Evidencia(*dados)

            relatorio_do_caso.evidencias.append(evidencia)

            print("EVIDENCIA ADICIONADA COM SUCESSO!")

        elif controle_relatorio == 3:
            dados = input("\nCADASTRANDO LOCAL: \nDigite separado pro virgula o codigo do local, nome, endereco, descricao").split(",")

            local = Local(*dados)

            relatorio_do_caso.local = local

            print("LOCAL ADICIONADA COM SUCESSO!")

        elif controle_relatorio == 4:
            if len(caso.testemunhas) == 0:
                print("Sem testemunha cadastrada, impossivel adicionar depoimento.")
            else:
                depoimento = input("\nDigite o depoimento")

                for n in range(len(caso.testemunhas)):
                    print(f"{n+1} - {caso.testemunhas[n].get_nome_testemunha()}")
                testemunha_escolhida = (int(input("Digite o numero da testemunha que voce quer gerar o depoimento: ")))-1

                depoimento = Depoimentos(depoimento, caso.testemunhas[testemunha_escolhida])

                relatorio_do_caso.depoimento.append(depoimento)

                print("DEPOIMENTO ADICIONADO COM SUCESSO!")

        elif controle_relatorio == 0:
            return

        else:
            print("Opção Invalida!")



def menu_primeiro():
    while True:
        escolher = int(input("\nINFORMATICOS INVESTIGATION\n1 — Cadastrar caso\n2 - Escolher caso\n3 - Ver quantidades de casos registrados "))

        if escolher == 1:
            cadastrar_caso()
        elif escolher == 2:
            escolher_caso()
        elif escolher == 3:
            print(f"Quantidade de casos registrado: ", len(casos))
        else:
            print("Opção Invalida!")

def menu_segundo(caso):
    while True:
        escolher = int(input("\nINFORMATICOS INVESTIGATION\n1 - Gerenciar Investigadores\n2 - Gerenciar Suspeitos\n3 - Gerenciar Testemunhas\n4 - Gerenciar Relatorio\n5 - Finalizar caso\n0 - Voltar "))
        if escolher == 1:
            gerenciar_investigadores(caso)
        elif escolher == 2:
            gerenciar_suspeitos(caso)
        elif escolher == 3:
            gerenciar_testemunhas(caso)
        elif escolher == 4:
            gerenciar_relatorio(caso)
        elif escolher == 5:
            caso.encerrar_caso()
        elif escolher == 0:
            return
        else:
            print("Opção Invalida!")


menu_primeiro()
