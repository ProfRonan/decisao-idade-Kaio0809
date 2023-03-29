impossivel=False
menor=False
maior=False
velho=False


idade = int(input())
if idade < 0:
    print('Impossível!')
    impossivel = True
if idade < 18:
    print('não precisa se alistar.')
    menor = True
if 18 < idade > 65:
    print('não esqueça de votar na proxima eleição.')
    maior = True
if idade > 65:
    print('vá descansar.')
    velho = True
if not(impossivel or menor or maior or velho):
    print('eita!')