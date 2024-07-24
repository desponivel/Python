nota1 =float (input('Primeira nota: '))
nota2 =float (input('Segunda nota: '))
media = (nota1 + nota2) / 2

print('Media:',media)

if media>9.0:
    print('Aprovado com louvor')

elif media>=7.0:
    print('Aprovado')

else:
    print('Reprovado')