import time

username = 'leo'
password = 'senhasecreta'

username_input = input('Username: ')
password_input = input('Password: ')

if username_input == username and password_input == password:
    print('Acesso concedido')
    print('Aguarde')
    time.sleep(5)
    print('Ok... Carregando...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    print('Tudo bem, você tem habilitação de segurança. Puxando o mainframe secreto.')
elif username_input == username and password_input != password:
    print('Senha incorreta')
elif username_input != username and password_input == password:
    print('Usuário incorreta')
else:
    print('Você pode verificar ambos os campos...')