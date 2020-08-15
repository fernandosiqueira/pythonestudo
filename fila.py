import heapq

class FilaDePrioridade:

	def __init__(self):
		self.fila = []
		self.indice = 0

	def inserir (self, item, prioridade):
		heapq.heappush(self.fila, (-prioridade, self.indice +1, item))

	def remover(self):
		return heapq.heappop(self.fila)[-1]

class Item:
	def __init__(self, nome):
		self.nome = nome	
	
	def __repr__(self):
		return self.nome

fila = FilaDePrioridade()
fila.inserir(Item('Fernando'), 24)
fila.inserir(Item('Lucas'), 20)
fila.inserir(Item('Adulto Ney'), 28)
print(fila)
print(fila.remover)

