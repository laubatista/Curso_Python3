'''Faça um programa que tennha uma função chamada escreva(), que receba um texto
qualquer como parâmetro e mostre uma mensagem com o tamanho adaptável.
'''

def escreva(texto):
    tam = len(texto) + 4
    print('='* tam)
    print(f'  {texto}')
    print('=' * tam)


#Programa principal.
#mensagem = str(input('Digite algo:'))
escreva('mensagem')
escreva('O mundo é lindo e maravilhoso!')
escreva('Eu quero paz!')
