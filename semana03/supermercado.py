class Supermercado:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def excluir_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                self.produtos.remove(produto)
                return True
        return False

    def listar_produtos(self):
        self.produtos.sort(key=lambda x: x.preco)
        for i, produto in enumerate(self.produtos, 1):
            print(f"{i}. {produto}")
            if i % 10 == 0:
                input("\nPressione Enter para continuar... ")

    def consultar_preco(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto.preco
        return None
