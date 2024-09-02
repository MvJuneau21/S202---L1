from dataset.datasetMercado import dataset
class ProductAnalyzer:
    def __init__(self, dataset):
        self.dataset = dataset

    def total_vendas_por_dia(self):
        vendas_por_dia = {}
        for compra in self.dataset:
            data = compra["data_compra"]
            total = sum(produto["quantidade"] * produto["preco"] for produto in compra["produtos"])
            if data in vendas_por_dia:
                vendas_por_dia[data] += total
            else:
                vendas_por_dia[data] = total
        return vendas_por_dia

    def produto_mais_vendido(self):
        vendas_por_produto = {}
        for compra in self.dataset:
            for produto in compra["produtos"]:
                descricao = produto["descricao"]
                quantidade = produto["quantidade"]
                if descricao in vendas_por_produto:
                    vendas_por_produto[descricao] += quantidade
                else:
                    vendas_por_produto[descricao] = quantidade
        produto_mais_vendido = max(vendas_por_produto, key=vendas_por_produto.get)
        return produto_mais_vendido

    def cliente_que_mais_gastou(self):
        maior_gasto = 0
        cliente_id = None
        for compra in self.dataset:
            total = sum(produto["quantidade"] * produto["preco"] for produto in compra["produtos"])
            if total > maior_gasto:
                maior_gasto = total
                cliente_id = compra["cliente_id"]
        return cliente_id

    def produtos_com_quantidade_acima_de_1(self):
        produtos_quantidade_acima_de_1 = set()
        for compra in self.dataset:
            for produto in compra["produtos"]:
                if produto["quantidade"] > 1:
                    produtos_quantidade_acima_de_1.add(produto["descricao"])
        return list(produtos_quantidade_acima_de_1)

# Exemplo de uso:
if __name__ == "__main__":
    analyzer = ProductAnalyzer(dataset)
    
    # 1. Total de vendas por dia
    print("Total de vendas por dia:")
    print(analyzer.total_vendas_por_dia())
    
    # 2. Produto mais vendido
    print("\nProduto mais vendido:")
    print(analyzer.produto_mais_vendido())
    
    # 3. Cliente que mais gastou em uma única compra
    print("\nCliente que mais gastou em uma única compra:")
    print(analyzer.cliente_que_mais_gastou())
    
    # 4. Produtos com quantidade vendida acima de 1 unidade
    print("\nProdutos com quantidade vendida acima de 1 unidade:")
    print(analyzer.produtos_com_quantidade_acima_de_1())
