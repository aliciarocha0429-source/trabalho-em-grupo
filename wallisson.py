from datetime import datetime

class Depoimentos: 
    def __init__(self, depoimento: str, pessoa, caso, ):
        self.__depoimento = depoimento # TRANSCREVER TODO DEPOIMENTO DA PESSOA
        self.__caso = caso # CLASS CASO
        self.__pessoa = pessoa # CLASS PESSOA
        self.__linha_do_tempo = [] # SAIU DE TAL LUGAR - PARTIU PRA TAL LUGAR - CHEGOU EM TAL LUGAR
        self.__conclusao = "" # COLOCA TIPO: POSSIVEL INCOSSISTENCIA
        self.__horario = datetime.now()

    def get_depoimento(self):
        print("DEPOIMENTO: ", self.__depoimento)

    def get_conclusao(self):
        print(f"O CASO FOI MARCADO COMO: {self.__conclusao}.")

    def set_conclusao(self):
        c = int(input("Olá, defina a conclusão do caso de acordo a analise do depoimento da pessoa.\n1 - TODO O DEPOIMENTO BATE;\n2 - A MAIORIA DO DEPOIMENTO BATE;\n3 - POSSÍVEL INCONSISTÊNCIA;\n4 - INCONSISTÊNCIA."))
        if c == 1:
            self.__conclusao = "✅ TODO DEPOIMENTO BATE."
        elif c == 2:
            self.__conclusao = "✅ O DEPOIMENTO BATE, MAS EXISTE INCONSISTÊNCIA."
        elif c == 3:
            self.__conclusao = "⚠️ POSSÍVEL INCONSISTÊNCIA"
        elif c == 4:
            self.__conclusao = "⚠️ INCONSISTÊNCIA"

    def get_linha_do_tempo(self):
        print(self.__linha_do_tempo)

    def set_linha_do_tempo(self):
        atualizacao = input("Adicione outras coisas na linha do tempo [digite 'SAIR' para parar de adicionar]: ")
        while atualizacao.upper() != "SAIR":
            self.__linha_do_tempo.append(atualizacao)
            print(f"{atualizacao} adicionada a linha do tempo")

            atualizacao = input("Adicione outras coisas na linha do tempo [digite 'SAIR' para parar de adicionar]: ")

d1 = Depoimentos("TAL TALTATLALTATLTALTLA", "1", "2")

d1.get_linha_do_tempo()
d1.set_linha_do_tempo()
d1.get_linha_do_tempo()
d1.get_informacoes_depoimentos()
d1.set_conclusao()
d1.get_informacoes_depoimentos()

lista_casos = []
n = 1

caso_da_lapa = Caso()

while True:
    alterar = int(input("\nMENU INVESTIGAÇÃO\n1 - Criar Caso\n2- Gerenciar Casos"))
    if alterar == 1:
        nome_do_caso = input("Digite o nome do caso: ")
        nome_do_caso = Caso()
        lista_casos.append(nome_do_caso)
    elif alterar == 2:
        escolher_caso = int(input(f"{lista_casos}\nDIGITE O NUMERO DO CASO, OS CASOS É NUMERADO EM ORDEM, COMEÇA DO 0. "))
        print("\nCASO ACESSADO COM SUCESSO!")

    alterar = int(input('''╔══════════════════════════════════════╗
 ║          ECHO INVESTIGATION          ║
 ╠══════════════════════════════════════╣
 ║ 1. Gerenciar caso                    ║
 ║ 2. Investigadores                    ║
 ║ 3. Suspeitos                         ║
 ║ 4. Testemunhas                       ║
 ║ 5. Evidências                        ║
 ║ 6. Depoimento                        ║
 ║ 7. Linha do tempo                    ║
 ║ 8. Analisar investigação             ║
 ║ 9. Gerar relatório                   ║
 ║ 0. Sair                              ║
 ╚══════════════════════════════════════╝
 '''))

    alterar = int(input("\nMENU INVESTIGAÇÃO\n1 - Gerenciar caso\n2- Investigadores\n3 - Suspeitos\n4 - Testemunhas\n5 - Evidências\n6 - Depoimento\n"))

    if alterar == 1: 
        pass

    elif alterar == 5:
        pass

    elif alterar == 6:
        lista_casos[escolher_caso].get_depoimento()

    elif alterar == 7:
        escolha_linha_do_tempo = int(input("VOCE DESEJA ALTERAR OU VER A LINHA DO TEMPO? 1 - Alterar; 2 - Ver: "))
        if escolha_linha_do_tempo == 1:
            lista_casos[escolher_caso].set_linha_do_tempo()
        elif escolha_linha_do_tempo == 2:
            lista_casos[escolher_caso].get_linha_do_tempo()

    elif alterar == 0:
        print("MENU FECHADO!!!")
        break

    else:
        print("Numero invalido.")

    # if alterar == 1:
