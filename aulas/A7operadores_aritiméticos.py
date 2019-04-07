#nome = input('Qual o seu nome?')
#print('Prazer em conhecer {: ^20}'.format(nome))
n1 = int(input('Um valor:'))
n2 = int(input('Outro valor'))
s = n1 + n2   # soma
sub = n1 - n2 #subtração
m = n1 * n2   #multiplicação
d = n1 / n2   #divisão
di = n1 // n2 #divisão inteira
e = n1 ** n2  #exponênciação
rd = n1 % n2  #resto da divisão
print('o resultado das operações é:')
print('soma = {}\nsubtração = {}\nmultiplicação = {}\ndivisão = {:.1f}'.format(s ,sub, m , d), end = ' ')
print('\ndivisão inteira = {:.1f}\nexponênciação = {}\nresto da divisão = {}'.format(di , e , rd))



