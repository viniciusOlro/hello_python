animals = ['cat', 'dog', 'bird', 'fish']
print(animals[0]) #print 'cat'

peoples = [['vinícius', 20], ['suelen', 21]]
print(peoples[0][0])
print(peoples[1][0])
# valores negativos contam a partir do final do array
print(peoples[-1][0])

# slice => exibir intervalo do array
print(animals[1:2])
print(animals[1:])
print(animals[:3])

#excluir pelo índice
#para excluir pelo conteúdo, utiliza-se a remove() function
del animals[-1]
print(animals)

if('cat' in animals):
  print('Tem gato na lista.')

animals.append('Snake')
print(animals)

animals.insert(0, 'Chicken')
print(animals)

## sort() => ordenado crescentemente ASCII
## sort(reverse=True) => ordenado decrescentemente ASCII

## tuplas => arrays com (), representam uma lista imutável

## converter arrays em tuplas
## list(), tuple()

