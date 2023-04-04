#cada maçã custa 1,30
#a partir de 12 cada uma sai por 1,00

executar='sim'
while(executar=='sim'):
    nm_macas=int(input('digite a quantidade de maçãs: '))
    if(nm_macas<12):
        valorTotal=nm_macas*1.30
        print(' Valor a ser pago:{:,.2f}'.format(valorTotal))
    else:
        valorTotal=nm_macas*1.00
        print(' Valor a ser pago:{:.2f}'.format(valorTotal))
    executar=str.lower(input('Deseja realizar outra compra? '))