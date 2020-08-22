class Funcionario:
	"""docstring for Funionario"""
	def __init__(self, nome, salario, cpf):
		self.nome = nome
		self.salario = salario
		self.cpf = cpf

	def get_Bonificacao(self):
		return self.salario * 0.50
		
class Gerente(Funcionario):
	def __init__(self, nome, salario, cpf, senha):
		super().__init__(nome, salario, cpf)
		self.senha = senha

	def get_Bonificacao(self):
		return super().get_Bonificacao() + 1000

g = Gerente('Adulto Ney', 3000, '43509422899', '123456789')
print (g.nome)
print (g.salario)
print (g.cpf)
print (g.get_Bonificacao())
print (g.senha)