

idade = int(input())
if idade < 0:
    print('Impossível!')
else:
    if idade >= 0 and idade < 18:
        print('Não precisa se alistar.')

    elif 18 < idade < 65:
        print('Não esqueça de votar na próxima eleição.')

    elif idade > 65:
        print('Vá descansar.')

    else:
        print('Eita!')