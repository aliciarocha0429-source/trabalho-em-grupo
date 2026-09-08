from datetime import datetime

class Depoimentos: 
    def __init__(self, depoimento: str, pessoa, caso, conclusao):
        self.__depoimento = depoimento # TRANSCREVER TODO DEPOIMENTO DA PESSOA
        self.__caso = caso # CLASS CASO
        self.__pessoa = pessoa # CLASS PESSOA
        self.__linha_do_tempo = [] # SAIU DE TAL LUGAR - PARTIU PRA TAL LUGAR - CHEGOU EM TAL LUGAR
        self.__conclusao = conclusao # COLOCA TIPO: POSSIVEL INCOSSISTENCIA
        self.__horario = datetime.now()

    def get_conclusao(self):
        print(f"O CASO FOI MARCADO COMO: {self.__conclusao}.")

    def set_conclusao(self):
        c = input("Olá, defina a conclusão do caso de acordo a analise do depoimento da pessoa.\n1 - TODO O DEPOIMENTO BATE;\n2 - A MAIORIA DO DEPOIMENTO BATE;\n3 - POSSÍVEL INCONSISTÊNCIA;\n4 - INCONSISTÊNCIA.")
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

    
            