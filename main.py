import secrets
import string

caracteres_num = int(input('Quantos caracteres? '))

itens = (string.ascii_uppercase + string.ascii_letters+ string.ascii_lowercase + 
         string.digits)

senha = [secrets.choice(itens) for i in range(caracteres_num)]

for i in senha:
    print(f'{i}', end='')