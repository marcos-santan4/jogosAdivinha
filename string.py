print("Tentativa {} de {}".format(3,10))

print("Tentativa {1} de {0}".format(3,10))

print("R$ {}".format(1.59))
print("R$ {:f}".format(1.593)) #float
print("R$ {:.2f}".format(1.59)) #float com sugestao de casas decimais
print("R$ {:.2f}".format(1.5)) #float com sugestao de casas decimais
print("R$ {:.2f}".format(1234.5)) #float com sugestao de casas decimais
print("R$ {:7.2f}".format(1234.5)) #float com sugestao de casas decimais
print("R$ {:7.2f}".format(4.5)) #float com sugestao de casas decimais
print("R$ {:07.2f}".format(4.5)) #float com sugestao de casas decimais - 07 para que apareçam 0 na frente e 7 casas dec imais

print("R$ {:07d}".format(4)) #inteiro - coloque o 'd'
print("R$ {:7d}".format(4)) #inteiro - sem zeros

print("Data {:2d}/{:2d}".format(9,2)) #inteiro
print("Data {:02d}/{:02d}".format(9,2)) #inteiro

telefone = "73988024012"
nome = "Marcos Santana"

coord = {'telefone': "73988024012", 'nome': 'Marcos Santana'}
print('Coordinates: {telefone}, {nome}'.format(**coord))