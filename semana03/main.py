from produto import Produto
from supermercado import Supermercado

def main():
    supermercado = Supermercado()

    while True:
        print("=== Supermercado ===")
        print("1. Inserir novo produto")
        print("2. Excluir produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar preço de um produto")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            codigo = input("Digite o código do produto: ")
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            produto = Produto(codigo, nome, preco)
            supermercado.inserir_produto(produto)
            print(f"\nProduto '{nome}' cadastrado com sucesso!\n")
        elif opcao == '2':
            codigo_para_excluir = input("Digite o código do produto a ser excluído: ")
            if supermercado.excluir_produto(codigo_para_excluir):
                print(f"\nProduto excluído com sucesso!\n")
            else:
                print("\nProduto não encontrado.\n")
        elif opcao == '3':
            supermercado.listar_produtos()
        elif opcao == '4':
            codigo_para_consultar = input("Digite o código do produto para consultar o preço: ")
            preco = supermercado.consultar_preco(codigo_para_consultar)
            if preco is not None:
                print(f"\nO preço do produto é R${preco:.2f}\n")
            else:
                print("\nProduto não encontrado.\n")
        elif opcao == '0':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
