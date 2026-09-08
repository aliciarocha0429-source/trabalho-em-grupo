from datetime import datetime

class Depoimentos: 
    def __init__(self, depoimento: str, pessoa, caso, linha, conclusao):
        self.__depoimento = depoimento # TRANSCREVER TODO DEPOIMENTO DA PESSOA
        self.__caso = caso # CLASS CASO
        self.__pessoa = pessoa # CLASS PESSOA
        self.__linha_do_tempo = linha # SAIU DE TAL LUGAR - PARTIU PRA TAL LUGAR - CHEGOU EM TAL LUGAR
        self.__conclusao = conclusao # COLOCA TIPO: POSSIVEL INCOSSISTENCIA
        self.__horario = datetime.now()




        