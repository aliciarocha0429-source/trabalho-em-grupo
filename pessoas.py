

class Pessoa:

    def __init__(self, nome, data_nascimento: str, cpf, genero, telefone, endereco):
        self.__nome_pessoa = nome
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__genero = genero
        self.__telefone = telefone
        self.__endereco = endereco

    def get_nome_pessoa(self):
        return self.__nome_pessoa
    def exibir_informacoes(self):
        print("\nPESSOA")
        print(f"Nome: {self.__nome_pessoa}")
        print(f"Data de nascimento: {self.__data_nascimento}")
        print(f"CPF: {self.__cpf}")
        print(f"Gênero: {self.__genero}")

class Investigador(Pessoa):
    def __init__(self, nome, data_nascimento, cpf, genero, telefone,
                 endereco, registro_funcional, cargo, departamento):
        super().__init__(
            nome, data_nascimento, cpf, genero, telefone, endereco
        )
        self.__registro_funcional = registro_funcional
        self.__cargo = cargo
        self.__departamento = departamento

    def get_nome_investigador(self):
        return super().get_nome_pessoa() 

    def exibir_informacoes_investigador(self):
        super().exibir_informacoes()
        print(f"Cargo: {self.__cargo}")
        print(f"Departamento: {self.__departamento}")

    def set_cargo(self):
        novo_cargo = input("Digite o novo cargo: ")
        self.__cargo = novo_cargo
        print("Cargo atualizado.")

    def set_departamento(self):
        novo_departamento = input("Digite o novo departamento: ")
        self.__departamento = novo_departamento
        print("Departamento atualizado.")

class Suspeito(Pessoa):
    def __init__(self, nome, data_nascimento, cpf, genero, telefone,
                 endereco, status_custodia, caracteristicas_fisicas):
        super().__init__(
            nome, data_nascimento, cpf, genero, telefone, endereco
        )
        self.__status_custodia = status_custodia
        self.__caracteristicas = caracteristicas_fisicas

    def get_nome_suspeito(self):
        return super().get_nome_pessoa() 

    def exibir_informacoes_suspeito(self):
        super().exibir_informacoes()
        print(f"Status Custodia: {self.__status_custodia}")
        print(f"Caracteristicas: {self.__caracteristicas}")

    def set_status_custodia(self):
        novo_status = input("Digite o status da custodia: ")
        self.__status_custodia = novo_status
        print("Status atualizado.")


class Testemunhas(Pessoa):
    def __init__(self, nome, data_nascimento, cpf, genero, telefone,
                 endereco, tipo_testemunha):
        super().__init__(
            nome, data_nascimento, cpf, genero, telefone, endereco
        )
        self.__tipo_testemunha = tipo_testemunha

    def get_nome_testemunha(self):
        return super().get_nome_pessoa()

    def exibir_informacoes_testemunha(self):
        super().exibir_informacoes()
        print(f"Tipo testemunha: {self.__tipo_testemunha}")

    def get_tipo_testemunha(self):
        print("Tipo de testemunha: ", self.__tipo_testemunha)

    def set_tipo_testemunha(self):
        novo_tipo_testemunha = input("Atualize o tipo de testemunha: ")
        self.__tipo_testemunha = novo_tipo_testemunha
        print("Tipo de testemunha atualizado.")