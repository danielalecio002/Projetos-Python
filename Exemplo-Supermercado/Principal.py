#coding: utf-8
from Produto import *
from Supermercado import *


import sys
supermercado = Supermercado("Mercadinho");


print("==============================================================");
print("|                     Supermercado                           |");
print("==============================================================\n");
print("========================Comandos================================");
print("addProd - Para adicionar um produto no Estoque\nrm - Para remover um Produto do Estoque\nestoque - Para exibir o Estoque");
print("addPedido - Para adicionar um Pedido\npedidos - para mostrar a lista de Pedidos ");
print("sair - Para encerrar o sistema\n");
print("==============================================================");
op = " ";
 
while(op != "sair"):
	if sys.version_info.major == 2:
    	 op = raw_input("Digite um comando:")
	elif sys.version_info.major == 3:
    	 op = input("Digite um comando:");
	
	print("==============================================================");
	if(op == "addProd"):
		print("====================Cadastrando Produtos=====================");
		# para não ficar precisando colocar aspas nos valores que sao 
		# string usei a funcao raw_input, porem ela não funciona no 
		# python 3 ja que o input em si ja trás essa funcionalidade 
		# de não precisá passsar as string entre aspas,porém o 
		# raw_input nao funciona caso a versao instalada serja a 3,
		# por isso foi criado a condicao que verifica a versão 
		#instalada e usa a forma de entrada adequada para cada versão
		if sys.version_info.major == 2:
			 Nome = raw_input("Nome do Produto:");
		elif sys.version_info.major == 3:
    		 Nome = input("Digite um comando:");	
		Preco = float(input("Preco do Produto:"));
		Qtd = int(input("Quantidade do Produto:"));
		supermercado.adicionarProduto(Produto(Nome,Preco,Qtd));
		print("==============================================================");
	elif(op == "rm"):
		print("====================Removendo Produtos=====================");
		if sys.version_info.major == 2:
			 Nome = raw_input("Nome do Produto:");
		elif sys.version_info.major == 3:
    		 Nome = input("Digite um comando:");	
		supermercado.removerProduto(Nome);
		print("==============================================================");
	elif(op == "estoque"):
		print("====================Cadastrando Produtos=====================");
		supermercado.mostrarEstoque();
		print("==============================================================");
	elif(op == "pedidos"):
		print("==============================================================");
		supermercado.mostrarPedidos();	
		print("==============================================================");
	elif(op == "addPedido"):
		print("==============================================================");
		if sys.version_info.major == 2:
			 Nome = raw_input("Nome do Produto:");
		elif sys.version_info.major == 3:
    		 Nome = input("Digite um comando:");	
		Qtd = input("Qtd do produto:");
		if sys.version_info.major == 2:
			Pagamento = raw_input("Forma de Pagamento:");
		elif sys.version_info.major == 3:
    		 Pagamento = input("Forma de Pagamento:");	
		produto = supermercado.verificarProduto(Nome);
		if(produto == False):
			print("produto não existe");
		else:	
			if(supermercado.fazerPedido(produto, Qtd, Pagamento)):
				print("Pedido Aceito");
			elif(supermercado.fazerPedido(produto, Qtd, Pagamento) == False):
				print("qtd indisponivel");	
				
		print("==============================================================");	
	elif(op == "sair"):
		sys.exit();
	else:
	 	print("Comando inexistente !!!");		
