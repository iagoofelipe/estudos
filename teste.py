db_local = {
    0 : ['IAGO','123456','iago@gmail.com'],
    1 : ['IAGO felipe','321654','iago2@gmail.com'],
}

for i in db_local.values():
    nome = i[0]
    telefone = i[1]
    email = i[2]

    if 'IAGO felipe' in i:
        print(f'{nome:>20} {telefone:>20} {email:>20}')