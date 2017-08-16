from Model.Pessoa import Pessoa
from Model.Cliente import Cliente
from Model.Funcionario import Funcionario
from Model.Maratona import Maratona

def main():

    funcionario = Funcionario("José")
    cliente = Cliente("Maria")
    maratona = Maratona()

    maratona.correr(cliente)
    maratona.correr(funcionario)


if (__name__ == "__main__"):
    main()
