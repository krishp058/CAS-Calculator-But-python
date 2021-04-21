

def start():
  numbers = input("what are the  numbers you want to calculate seperated by a space: ")
  return numbers


def List(rawNumbers):
  formatedNumbers = rawNumbers.split()
  try:
    formatedResult = [int(formatedNumbers) for formatedNumbers in formatedNumbers]
  except:
    print("error: Please input a number")
  return (formatedResult)
  

def operation(inputNumbers):
  operatation = input("What operation would you like?: ")

  result = 0
  #operations
  if operatation == "+":
    for number in inputNumbers:
      result += number
  print(result)     

  if operatation == "-":
    for number in inputNumbers:

      result = [ inputNumbers[number] for i in (0, -1) ]
      result -= number
      print(result)

operation(List(start()))
