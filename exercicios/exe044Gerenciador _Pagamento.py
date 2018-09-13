print('{:=^40}'.format(' LOJAS LAUDEINE '))
preço = float(input('Preço das compras: R$'))

print('Escolha a forma de pagamento!\n'
      '1 = pagamento a vista dinheiro/cheque:10% desconto\n'
      '2 = Pagamento a vista no cartão: 5% desconto\n'
      '3 = Pagamento em 2X no cartão: preço normal\n'
      '4 = Parcelado em 3X ou mais no cartão: 20% juros')

opcao = int(input('Opção:'))

if opcao == 1:
    total = preço - (preço * 10 /100)

elif opcao == 2:
    total = preço - (preço * 5 /100)

elif opcao == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${} sem juros '.format(parcela))

elif opcao == 4:
    total = preço + (preço * 20 / 100)
    tot_parcela = int(input('Deseja dividir em quantas parcelas?'))
    parcela = total /tot_parcela
    print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(tot_parcela, parcela))
else:
    total = 0
    print('OPÇÃO DE PAGAMENTO INVÁLIDA!')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço,total))
