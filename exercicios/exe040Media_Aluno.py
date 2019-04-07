# Média de alunos.

nota1 = float(input('Digite a 1º nota:'))
nota2 = float(input('Digite a 2º nota:'))

media = (nota1 + nota2) / 2
print('Terando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))


if media < 5.0:
    print('O aluno está REPROVADO!')

elif media > 5.0 and media < 7.0:
    print('O aluno está em RECUPARAÇÃO!')

elif media > 7.0:
    print('O aluno está APROVADO!!!')