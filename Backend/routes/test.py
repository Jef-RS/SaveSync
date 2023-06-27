from userbd_config import packetU_base, packetU_bd

read_users = packetU_bd.read_users()

username = 'eusouanderson'

print(read_users)
if read_users['username'] == username:
    error = 'Usuário já cadastrado.'
    print(error)
else:
    print('Erro ao ler os usuários:')