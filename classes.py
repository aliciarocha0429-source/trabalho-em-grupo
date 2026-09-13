from datetime import datetime

class Caso:

    total_de_casos = 0

    def __init__(self, numero, titulo, descricao, dificuldade):

        self.suspeitos = []
        self.investigador = []
        self.testemunhas = []

        self.numero = numero
        self.titulo = titulo
        self.descricao = descricao
        self.data = datetime.today()
        self.status = "Em andamento"
        self.dificuldade = dificuldade

        self.relatorio = None
        Caso.total_de_casos += 1

    def adicionar_suspeito(self, suspeito):
        self.suspeitos.append(suspeito)

    def mostrar_suspeitos(self):

        if not self.suspeitos:
            print("Nenhum suspeito cadastrado neste caso.")


        print(f"\n===== SUSPEITOS DO CASO #{self.numero} =====")

        for suspeito in self.suspeitos:
            suspeito.exibir_informacoes_suspeito()

    def adicionar_investigador(self, investigador):
        self.investigador.append(investigador)

    def mostrar_investigadores(self):

        if not self.investigador:
            print("Nenhum investigador cadastrado neste caso.")


        print(f"\n===== INVESTIGADORES DO CASO #{self.numero} =====")

        for investigador in self.investigador:
            investigador.exibir_informacoes_investigador()

    def adicionar_testemunha(self, testemunha):
        self.testemunhas.append(testemunha)

    def mostrar_testemunhas(self):

        if not self.testemunhas:
            print("Nenhuma testemunha cadastrada neste caso.")

        print(f"\n===== TESTEMUNHAS DO CASO #{self.numero} =====")

        for testemunha in self.testemunhas:
            testemunha.exibir_informacoes_testemunha()

    def encerrar_caso(self):
        self.status = "Encerrado"
        print("\nCaso finalizado")

    def exibir_informacoes(self):

        print("\n========== CASO ==========")
        print(f"Número: #{self.numero}")
        print(f"Título: {self.titulo}")
        print(f"Descrição: {self.descricao}")
        print(f"Data: {self.data}")
        print(f"Status: {self.status}")
        print(f"Dificuldade: {self.dificuldade}")

    @classmethod
    def quantidade_de_casos(cls):
        return cls.total_de_casos


class Evidencia:

    def __init__(self, codigo, descricao, local_encontrada,
                 data_hora, relevancia):

        self.codigo = codigo
        self.descricao = descricao
        self.local_encontrada = local_encontrada
        self.data_hora = data_hora
        self.relevancia = relevancia

    def exibir_informacoes(self):

        print("\n----- EVIDÊNCIA -----")
        print(f"Código: {self.codigo}")
        print(f"Descrição: {self.descricao}")
        print(f"Local encontrada: {self.local_encontrada}")
        print(f"Data/Hora: {self.data_hora}")
        print(f"Relevância: {self.relevancia}")


class Local:

    def __init__(self, codigo, nome, endereco, descricao):

        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.descricao = descricao


    def exibir_informacoes(self):

        print("\n========== LOCAL ==========")
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")
        print(f"Descrição: {self.descricao}")