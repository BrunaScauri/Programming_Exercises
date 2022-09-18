# Desafio 1
def compareTrue(v1, v2):
  if v1 == True and v2 == False:
    return False 
  elif v1 == False and v2 == False:
    return False
  else:
    return True
  
# Desafio 2
def calcArea(base, height):
  area = (base * height) / 2
  return area

# Desafio 3
def splitSentence(string):
  splitting = str.split(' ')
  return splitting

# Desafio 4
def concatName():
  arr = []
  firstIndex = arr[0]
  lastIndex = arr[arr.length -1]
  result = lastIndex + (', ') + firstIndex
  return result

# Desafio 5
def footballPoints(wins, ties):
  wins = wins * 3
  pontos = wins + ties
  return pontos

# Desafio 6
def catAndMouse(mouse, cat1, cat2):
  position1 = cat1 - mouse
  position2 = cat2 - mouse
  if position1 < 0:
    position2 *= -1
  elif position2 < 0:
    position2 *= -1
  elif position1 < position2:
    return 'cat1'
  elif position1 > position2:
    return 'cat2'
  else:
    return 'Os gatos trombam e o rato foge.'

# Desagio 7
def fizzBuzz(array):
  result = []
  i = 0
  for i in array:
    if (array[i] % 3) == 0 and (array[i] % 5) == 0:
      result.append('fizzBuzz')
    elif array[i] % 3 == 0:
      result.append('fizz')
    elif array[i] % 5 == 0:
      result.append('buzz')
    else:
      result.append('bug!')
  return result

# Desafio 9
# def encode(string):
#   encript = 'Hi there!'
#   # code = string.replace(/a/gi, 1).replace(/e/gi, 2).replace(/i/gi, 3).replace(/o/gi, 4).replace(/u/gi, 5)
#   return code
#   decript = encode(encript)

# def decode(b):
#   string_decoded = b.replaceAll(1, "a").replaceAll(2, "e").replaceAll(3, "i").replaceAll(4, "o").replaceAll(5, "u");
#   return string_decoded
#   WIP!