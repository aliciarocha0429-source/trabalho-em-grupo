from datetime import datetime



class Depoimentos:

    def __init__(self, depoimento: str, pessoa):

        self.__depoimento = depoimento
        self.__pessoa = pessoa
        self.__horario = datetime.now()

    def get_depoimento(self):
        print(f"Testemunha: {self.__pessoa.get_nome_testemunha()}")
        print(f"HORARIO: {self.__horario}")
        print("DEPOIMENTO:", self.__depoimento)