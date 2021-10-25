valor = int(input('Digite o valor em R$'))


def calculaValor(val):
 valor = valor - (cedulas100 * val)
 return valor // val
 
if valor >= 100:
 cedulas100 = calculaValor(100)
 print('{} cédulas de 100' .format(cedulas100))
 
if valor >= 50:
 cedulas50 = calculaValor(50)
 print('{} cédulas de 50' .format(cedulas50))
 
if valor >= 20:
 cedulas20 = calculaValor(20)
 print('{} cédulas de 20' .format(cedulas20))
 
if valor >= 10:
 cedulas10 = calculaValor(10)
 print('{} cédulas de 10' .format(cedulas10))
 
if valor >= 5:
 cedulas5 = calculaValor(5)
 print('{} cédulas de 5' .format(cedulas5))
 
if valor:
 cedulas1 = valor
 print('{} moedas de 1 que pobreza hein mana' .format(cedulas1))
 
#top
