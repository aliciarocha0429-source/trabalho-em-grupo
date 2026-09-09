class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, genero, telefone, endereco):
        self.__nome_pessoa = nome
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__genero = genero
        self.__telefone = telefone
        self.__endereco = endereco
        
    def get_telefone(self):
        print(f"Numero de telefone: {self.__telefone}")
        
    def set_telefone(self):
        telefone_novo = input("Digite o novo numero de telefone: ")
        if len(telefone_novo) >= 11:
            self.__telefone = telefone_novo
            print("Telefone atualizado.")
        else:
            print("Telefone Invalido.")
            
    def get_endereco(self):
        print("O endereço é: ", self.__endereco)
        
    def set_endereco(self):
        novo_endereco = input("Digite seu endereco: ")
        self.__endereco = novo_endereco
        print("Endereço atualizado.")

class Investigador(Pessoa):
    def __init__(self, nome, data_nascimento, cpf, genero, telefone, endereco, registro_funcional, cargo, departamento):
        super().__init__(nome, data_nascimento, cpf, genero, telefone, endereco)
        self.__registro_funcional = registro_funcional
        self.__cargo = cargo
        self.__departamento = departamento
        
    def get_cargo(self):
        print("Cargo do Investigador: ", self.__cargo)

    def set_cargo(self):
        novo_cargo = input("Digite o novo cargo: ")
        self.__cargo
        print("cargo atualizado.")
        
    def get_departamento(self):
        print("Departamento do Investigador: ", self.__departamento)
        
    def set_departamento(self):
        novo_departamento = input("Digite o novo departamento: ")
        self.__departamento = novo_departamento
        print("Departamento atualizado.")
            
class Suspeito(Pessoa):
    def __init__(self, nome, data_nascimento, cpf, genero, telefone, endereco, status_custodia, caracteristicas_fisicas):
        super().__init__(nome, data_nascimento, cpf, genero, telefone, endereco)
        self.__status_custodia = status_custodia
        self.__caracteristicas = caracteristicas_fisicas
        
    def get_status_custodia(self):
        print("Status da custodia: ", self.__status_custodia)
        
    def set_status_custodia(self):
        novo_status = input("Digite o status da custodia: ")
        self.__status_custodia = novo_status
        print("Status atualizado.")
        
class Testemunhas(Pessoa):
    def __init__(self, nome, data_nascimento, cpf, genero, telefone, endereco, tipo_testemunha):
        super().__init__(nome, data_nascimento, cpf, genero, telefone, endereco)
        self.__tipo_testemunha = tipo_testemunha
        
    def get_tipo_testemunha(self):
        print("Tipo de testemunha: ", self.__tipo_testemunha)
        
    def set_tipo_testemunha(self):
        novo_tipo_testemunha = input("Atualize o tipo de testemunha: ")
        self.__tipo_testemunha = novo_tipo_testemunha
        print("Tipo de testemunha atualizado.")
        
    
