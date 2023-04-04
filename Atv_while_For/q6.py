# criando a lista de convidados e convites
convidados=['Neymar','Estevão','Pedro','Cr7','Messi','Vini']
convite='Olá {}, você foi convidado para festa do João, levem sua bebida!'
for convidado in convidados:
    print(convite.format(convidado))
desistentes=['Estevão']
print(f'Infelizmente, {desistentes} não poderá comparecer a festa!')
convidados.remove('Estevão')
convidados.append('Luciano')
for convidado in convidados:
    print(convite.format(convidado))
