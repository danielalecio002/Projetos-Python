#coding: utf-8
from Produto import *
class Supermercado:		
	def __init__(self, nome):
		self.nome = nome; 
		self.Estoque = []; #lista que vai ser o Estoque de produtos
		self.ItensPedidos = {}; #lista de produtos
	#metodo responsavel por cadastrar produto no estoque					
	def adicionarProduto(self, produto):
			self.Estoque.append(produto);
	#metodo responsavel por remover produto do estoque		
	def removerProduto(self, nome):
		i = 0; # contador usado para descobrir o indice do produto no estoque
		for item in self.Estoque: #pegando os produtos que existe no estoque para comparar e verificar se o produto que eu quero remover realmente esta no estoque
			if(item.getNome() == nome): #verificando se o produto que eu quero remover realmente existe no estoque
				self.Estoque.pop(i);	#removendo produto pelo indice
			i = i + 1;   # a cada produto que o for percorre eu incremento um ao meu contador que vai representar o indice do produto na lista estoque	
	def retornarPreco(self, nome):
		for elem in self.Estoque: #percorrendo o estoque
			if (elem.getNome() == nome): #verificando se o produto existe
				return elem.getPreco(); #retornando o preco do produto
		#metodo usado para exibir o estoque 					
	def mostrarEstoque(self):
		print("==================== Estoque ========================");
		for item in self.Estoque:
			print("|Desc||Preço||Qtd|");
			print(item.getNome(),item.getPreco(), item.getQtd());
		print("=====================================================");
		#metodo usado para verificar se existe um produto com tal nome no estoque
	def verificarProduto(self, nome):
		for item in self.Estoque: #procura no estoque o produto
			if(item.getNome() == nome):#caso ele exista ele retorna o produto 
				produto = Produto(item.getNome(), item.getPreco(), item.getQtd());  	
				return produto;#retornando produto
		return False;#caso nao o produto nao exista retorna False
	def fazerPedido(self,produto,qtd,formadepagamento):
		for item in self.Estoque: # percorrendo o estoque
				if(item.getNome() == produto.getNome()): #verificando se o produto existe no estoque 
					if(qtd <= item.getQtd()): #verificando se a qtd pedida do produto esta disponivel no estoque 
						qtdAtual = item.getQtd() - qtd; #calcula a nova qtd do produto
						item.setQtd(qtdAtual);#Atualiza a qtd
						self.ItensPedidos.update({produto:qtd});#adiciona o produto na lista de pedidos
						return True; #retorna 1 simbolizando que deu certo
					else:
						return False; #retorna 2 simbolizando que a qtd pedida do produto nao esta disponivel 
		#metodo usado para exibir a lista de pedidos que é composta de produtos				
	def mostrarPedidos(self):
		print("=============== Lista de Pedidos =================");
		for item in self.ItensPedidos:
			# print(item.getNome(),"      ", item.getQtd());	#exibe o nome e a qtd do produto 
			#print(item.getNome());
			print(" |Desc| |Qtd|");
			print(item.getNome(),self.ItensPedidos[item]);
			
		print("==================================================");		 	
