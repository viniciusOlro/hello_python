def divideBy(number):
  try:
    return 42 / number
  except:
    print('Impossível dividir por zero!', end=' ')

print(divideBy(2))
print(divideBy(10))
print(divideBy(5))
print(divideBy(0))