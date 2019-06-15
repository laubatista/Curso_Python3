
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'grátis', 'estudar', 'praticar', 'trabalhar', 'mercado',
            'programador', 'futuro')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos', end=' ')
    for letra in palavra:
        if letra.lower() in 'a, e, i, o, u':
            print(letra, end=' ')