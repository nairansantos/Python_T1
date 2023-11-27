class Produto:
    def __init__(self, codigo, nome, preco):
        if len(codigo) != 13 or not codigo.isdigit():
            raise ValueError("Código inválido. Deve ser uma string numérica de 13 caracteres.")
        
        if not nome[0].isupper() or not nome.isalpha():
            raise ValueError("Nome inválido. Deve começar com uma letra maiúscula e conter apenas letras.")
        
        try:
            preco = float(preco)
        except ValueError:
            raise ValueError("Preço inválido. Deve ser um número decimal.")

        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"Código: {self.codigo} | Nome: {self.nome} | Preço: R${self.preco:.2f}"
