#atribuição sem o menu
from classes import Caso
class Relatorio(Caso):

    def __init__(self,caso, numero, status, dificuldade,
    investigador_Res):
        super().__init__(self,caso, numero, status)
        self.dificuldade = dificuldade
        self.investigador_Res = investigador_Res

    def set_analisarrel(self):  
        pass  #so por enquanto

    def get_gerar_relatorio(self):
        print(f"{'=-='*15}")
        print(f"Caso respectivo: {self.caso}")
        print(f"Número: {self.numero}")
        print(f"Status do caso: {self.status}")
        print(f"Dificuldade: {self.numero}")
        print(f"Investigador: {self.status}")
        print(f"{'=-='*15}")





#pessoas  o depoimento
pessoa1 = Pessoa("alicia","emailexemplo@.")
pessoa2 = Pessoa("wallisson","emailexemplo@2.")

pessoa1.set_coclusao(1) #aqui teoricamente deve retornar {todo depoimento bate}
pessoa2.set_conclusao(2)
