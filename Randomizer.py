"""
Esse projeto é um Randomizer, ele vai pegar resultados inseridos e embaralhar eles para obter a resposta.
"""

from random import choice

print(f'Randomizer. Escreva nomes para serem sortidos')
n1 = str(input('Digite um nome: '))
n2 = str(input('Digite um 2° nome: '))
n3 = str(input('Digite um 3° nome: '))
n4 = str(input('Digite um 4° nome: '))

l = [n1, n2, n3, n4]

r = choice(l)

print(f'Analizando o resultado....')
print(f'O Nome sorteado foi {r}')

