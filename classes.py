class Caso:
    total_de_casos = 0


    def __init__(self, numero, titulo, descricao, data, status, dificuldade):
        self.numero = numero
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.status = status
        self.dificuldade = dificuldade
        self.local = None
        self.evidencias = []
        Caso.total_de_casos += 1

    def alterar_informacoes(self, titulo=None, descricao=None, data=None, dificuldade=None):
        if titulo:
            self.titulo = titulo


        if descricao:
            self.descricao = descricao


        if data:
            self.data = data


        if dificuldade:
            self.dificuldade = dificuldade

    def encerrar_caso(self):
        self.status = "Encerrado"


    def adicionar_local(self, local):
        self.local = local


    def adicionar_evidencia(self, evidencia):
        self.evidencias.append(evidencia)


    def listar_evidencias(self):
        if not self.evidencias:
            print("Nenhuma evidência cadastrada!")
            return

        print(f"\nEvidências do Caso #{self.numero}:")

        for evidencia in self.evidencias:
            evidencia.exibir_informacoes()


    def exibir_informacoes(self):
        print("\n========== CASO ==========")
        print(f" Número: #{self.numero} ")
        print(f" Título: {self.titulo} ")
        print(f" Descrição: {self.descricao} ")
        print(f" Data: {self.data} ")
        print(f" Status: {self.status} ")
        print(f" Dificuldade: {self.dificuldade} ")

        if self.local:
            print(f" Local: {self.local.nome} ")
        else:
            print("Local: Não cadastrado")

        print(f" Quantidade de evidências: {len(self.evidencias)} ")

    @classmethod
    def quantidade_de_casos(cls):
        return cls.total_de_casos



class Evidencia:
    def __init__(self, codigo, descricao, local_encontrada, data_hora, relevancia):
        self.codigo = codigo
        self.descricao = descricao
        self.local_encontrada = local_encontrada
        self.data_hora = data_hora
        self.relevancia = relevancia


    def alterar_relevancia(self, nova_relevancia):
        self.relevancia = nova_relevancia


    def exibir_informacoes(self):
        print("\n----- EVIDÊNCIA -----")
        print(f" Código: {self.codigo} ")
        print(f" Descrição: {self.descricao} ")
        print(f" Local encontrada: {self.local_encontrada} ")
        print(f" Data/Hora: {self.data_hora} ")
        print(f" Relevância: {self.relevancia} ")



class Local:
    def __init__(self, codigo, nome, endereco, descricao):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.descricao = descricao


    def alterar_informacoes(self, nome=None, endereco=None, descricao=None):
        if nome:
            self.nome = nome


        if endereco:
            self.endereco = endereco


        if descricao:
            self.descricao = descricao


    def exibir_informacoes(self):
        print("\n========== LOCAL ==========")
        print(f" Código: {self.codigo} ")
        print(f" Nome: {self.nome} ")
        print(f" Endereço: {self.endereco} ")
        print(f" Descrição: {self.descricao} ")


    