

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
    result_minus = 0
    result_times = 1
    
    result_minus = inputNumbers[0]
    #operations
    if operatation == "+":
        for number in inputNumbers:
            result += number
        print(result)

    elif operatation == "-":
        for number in inputNumbers[1:]:
            result_minus -= number
        print(result_minus)

    elif operatation == "*":
        for number in inputNumbers:
            result_times *= number 
        print(result_times)

    elif operatation == "/":
        for number in inputNumbers:
            result_times = inputNumbers[0] / inputNumbers[1] 
        print(result_times)

operation(List(start()))
