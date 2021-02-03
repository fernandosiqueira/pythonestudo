#nome = input (" Nome do Cidadão: ")
#idade = input (" Idade do Meliant: ")

#print(f" Nome do Cidadão:{nome} Idade do Meliante:{idade} ")

#print("******************")
#print("Primeiro exercico")

#numero_inteiro = input('Digite um numero inteiro: ')

#if numero_inteiro.isdigit():
#    numero_inteiro = int(numero_inteiro)
#    if numero_inteiro % 2 == 0:
#        print('Numero é par')
#    else:
#        print('Numero é impar')

#else:
#    print("Não é um numero inteiro: ")

#print("******************")
#print("Segundo exercico")


#hora = input('Digite a hora: ')

#if hora.isdigit():
#    hora = int(hora)
#    if hora <= 11 :
#        print (" Bom dia ")
#    elif hora <= 17:
#        print('boa tarde')
#    elif hora <= 23:
#        print('Boa noite')
#    else:
#        print('Valor não é valido para hora')
#else:
#    print('Valor não é valido para hora')


print("******************")
print("Terceiro exercico")

nome = input("digite seu nome:")
tamanho = len(nome)

if tamanho <= 4:
    print('nome curto')
elif tamanho <= 6:
    print ('nome normal')
else:
    print('nome e grande')

