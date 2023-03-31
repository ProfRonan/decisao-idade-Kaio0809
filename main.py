

idade = int(input())
if idade < 0:
    print('impossível!')
    
if idade < 18:
    print('não precisa se alistar.')

elif 18 < idade < 65:
    print('Não esqueça de votar na proxima eleição.')

elif idade > 65:
    print('Vá descansar.')

else:
    print('eita!')