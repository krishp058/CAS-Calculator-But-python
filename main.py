def start():
    numbers = input("What are the numbers do you want to calculate (please seperated by a space): ")
    return numbers


def List(rawNumbers):
    formatedNumbers = rawNumbers.split()
    try:
        formatedResult = [int(formatedNumbers) for formatedNumbers in formatedNumbers]
    except:
        print("error: Please input a number")
    return (formatedResult)


def operation(inputNumbers):
    operatation = input("What operation would you like? (+, -, *, /): ")

    result = 0
    result_minus = inputNumbers[0]
    result_times = 1
    result_divide = inputNumbers[0]

    # Operations
    try:
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
            for number in inputNumbers[1:]:
                result_divide /= number
            print(result_divide)
    except:
        print("Error: Please enter proper operations or refer back to the list.")


operation(List(start()))
