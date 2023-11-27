from funcionario import Funcionario
from empresa import Empresa

def main():
    empresa = Empresa()


    empresa.ler_funcionarios_do_arquivo('funcionario.txt')

    print("\nLista de Funcionários ANTES do Reajuste:")
    for funcionario in empresa.funcionarios:
        print(funcionario)

    # Reajusta salários em 10%
    empresa.reajusta_dez_porcento()

    print("\nLista de Funcionários DEPOIS do Reajuste:")
    for funcionario in empresa.funcionarios:
        print(funcionario)

if __name__ == "__main__":
    main()

