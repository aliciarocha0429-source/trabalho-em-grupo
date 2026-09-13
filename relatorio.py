class Relatorio:

    def __init__(self, caso):
        self.caso = caso
        self.evidencias = []
        self.local = None
        self.depoimento = []

    def get_gerar_relatorio(self):
        print(f"\n{'=-=' * 15}")
        print("RELATÓRIO DO CASO")
        print(f"DATA: {self.caso.data}")
        print(f"{'=-=' * 15}")

        print(f"Caso respectivo: {self.caso.titulo}")
        print(f"Número: {self.caso.numero}")
        print(f"Status do caso: {self.caso.status}")
        print(f"Dificuldade: {self.caso.dificuldade}")

        print(f"Investigadores: \n{len(self.caso.investigador)}")
        print(f"Suspeitos: \n{len(self.caso.suspeitos)}")
        print(f"Testemunhas: \n{len(self.caso.testemunhas)}")
        print(f"Evidências: \n")
        for n in self.evidencias:
            n.exibir_informacoes()
        print(f"Local: \n")
        if self.local is not None:
            self.local.exibir_informacoes()
        else:
            print("Nenhum local cadastrado.")
        print(f"Depoimento: \n")
        for n in self.depoimento:
            n.get_depoimento()


        print(f"{'=-=' * 15}")