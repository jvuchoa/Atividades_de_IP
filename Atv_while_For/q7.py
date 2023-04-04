usuarios=[]
while True:
    opcao=input('Deseja realizar um cadastro?\n(s/n)')
    if opcao=='n':
        break
    elif (opcao=='s'):
        nm=input('digite seu nome: ')
        idade=int(input('digite sua idade: '))
        email=input('digite seu email: ')
        usuario={'nome': nm,'idade': idade,'email': email}
        usuarios.append(usuario)
    
    else:
        print('Opção inválida!')
print(f'\n Usuários cadastrados:')
for usuario in usuarios:
    print(f"Nome: {usuario['nome']}, Idade: {usuario['idade']}, Email:{usuario['email']}")
    
