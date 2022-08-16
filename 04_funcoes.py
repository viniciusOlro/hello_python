# FUNÇÃO SEM RETORNO 
def hello(message):
  print(message)

hello("Hello world!")

# FUNÇÃO COM RETORNO

def numberDouble(number):
  return number * 2

print(numberDouble(10))

# PASSANDO PARÂMETROS NOMEADOS

print('Hello', 'World', sep=' | ')

# ALTERANDO VARÍAVEIS GLOBAIS DENTRO DE ESCOPO 
color = 'red'
print(color)

def changeColor():
  global color
  color = 'blue'

changeColor()

print(color)