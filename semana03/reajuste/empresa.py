class Empresa:
    
    def __init__(self):
        self.funcionario = []

    def ler_funcionario_do_arquivo(self,arquivo):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(',')
                    funcionario = Funcionario(*dados)
                    self.funcionarios.append(funcionario)
        except FileNotFoundError:
            print(f"Arquivo '{nome_arquivof}' não encontrado. Certifique-se de que o arquivo existe.")

    def reajusta_dez_porcento(self):
        for funcionario in self.funcionarios:
            funcionario.salario *= 1.1  # Aumenta o salário em 10%

