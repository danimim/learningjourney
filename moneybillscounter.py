valor = int(input('Digite o valor em R$ '))

if valor:
    if valor >= 100:
        celulas = valor // 100
        valor = valor - (celulas * 100)
        print('{} cédulas de 100' .format(celulas))
    if valor >= 50:
        celulas = valor // 50
        valor = valor - (celulas * 50)
        print('{} cédulas de 50' .format(celulas))
    if valor >= 20:
        celulas = valor // 20
        valor = valor - (celulas * 20)
        print('{} cédulas de 20' .format(celulas))
    if valor >= 10:
        celulas = valor // 10
        valor = valor - (celulas * 10)
        print('{} cédulas de 10' .format(celulas))
    if valor >= 5:
        celulas = valor // 5
        valor = valor - (celulas * 5)
        print('{} cédulas de 5' .format(celulas))
    if 0 < valor < 5:
        celulas = valor
        print('{} moedas de 1 que pobreza hein mana' .format(celulas))

# top
