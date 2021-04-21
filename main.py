class CasCalc:
    '''Format list'''
    def List(self, rawNumbers):
        formatedNumbers = rawNumbers.split()
        try:
            formatedResult = [int(formatedNumbers) for formatedNumbers in formatedNumbers]
        except:
            print("error: Please input a number")
        return (formatedResult)
    
    '''Perform operations'''
    def operation(self, inputNumbers):
        operatation = input("What operation would you like? (+, -, *, /): ")
        result = 0
        result_minus = inputNumbers[0]
        result_times = 1
        result_divide = inputNumbers[0]
        try:
            if operatation == "+":
                for number in inputNumbers:
                    result += number
                print('Result: {}'.format(result))

            elif operatation == "-":
                for number in inputNumbers[1:]:
                    result_minus -= number
                print('Result: {}'.format(result_minus))

            elif operatation == "*":
                for number in inputNumbers:
                    result_times *= number
                print('Result: {}'.format(result_times))

            elif operatation == "/":
                for number in inputNumbers:
                    result_divide /= number
                print('Result: {]'.format(result_times))
        except Exception as e:
            print("Error: Please enter proper operations or refer back to the list.")

    '''Main method.'''
    def main(self):
        numbers = input("What are the numbers do you want to calculate (please seperated by a space): ")
        self.operation(self.List(numbers))

if __name__ == '__main__':
    cascalc = CasCalc()
    cascalc.main()