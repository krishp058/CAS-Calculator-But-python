

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
    elif operatation == "-":
        for number in inputNumbers:
            result_minus = number[0]
            result_minus -= number[1:] 
operation(List(start()))
