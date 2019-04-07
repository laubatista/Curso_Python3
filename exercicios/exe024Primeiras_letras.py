#Verifica se o nome da cidade começa com SANTO
cidade = str(input('Digite o nome de uma cidade:')).strip()

print(cidade[:5].upper() == 'SANTO')