nome = "Fernando"
idade = 25
altura = 1.84
peso = 80.50
ano_atual = 2021
ano_nascimento = ano_atual-idade
imc = peso / (altura*altura)

print(f'{nome} tem {idade} anos, nasceu em {ano_nascimento}, mede {altura}m de altura e {peso}kg, com o IMC de {imc:.2f}')