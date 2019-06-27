#classe que define o que e um produto
class Produto:
	#construtor
	def __init__(self,nome, preco, qtd):
		#atributos do produto
		self.nome = nome
		self.preco = preco
		self.qtd = qtd

	#criando gets e sets
	def getNome(self):
		return self.nome

	def getPreco(self):
		return self.preco	

	def getQtd(self):
	    return self.qtd
	
	def setNome(self, nome):
		self.nome = nome
	
	def setPreco(self, preco):
		self.preco = preco
	
	def setQtd(self, qtd):
		self.qtd = qtd
