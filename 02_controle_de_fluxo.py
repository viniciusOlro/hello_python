# USO DE IF-ELSE
userValue = input('Digite um número: ')

if (int(userValue) > 10):
  print('Maior que dez.')

elif(int(userValue) == 10):
  print('Igual a dez!')

else:
  print('Menor que dez.')

# USO DE WHILE

counter = 0

while(counter < 5):
  counter = counter + 1
  print(counter)

yourName = ''

while(yourName != 'your name'):
  yourName = input('Type your name: ')

# TODO: USAR BREAK E CONTINUE

# FOR IN RANGE

total = 0

for num in range(101):
  total = total + num
  
print(total)

for num in range(-10, 12, 2):
  print(num)