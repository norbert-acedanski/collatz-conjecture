import matplotlib.pyplot as plt
import re

class CollatzConjecture():
    def __init__(self, startNumber):
        self.startNumber = startNumber
        self.collatzNumbers = []
        self.xValues = []

    def computeCollatzNumbers(self):
        self.collatzNumbers.append(self.startNumber)
        number = self.startNumber
        i = 0
        self.xValues.append(i)
        while number != 1:
            if number % 2 == 0:
                number = int(number/2)
            else:
                number = int(3*number + 1)
            i += 1
            self.collatzNumbers.append(number)
            self.xValues.append(i)
        print("Collatz numbers for the number " + str(self.startNumber) + ": " + str(self.collatzNumbers))
        print("Number of steps: " + str(len(self.xValues)))
        print("Maximum number: " + str(max(self.collatzNumbers)))
    
    def plotNumbers(self):
        fig = plt.figure()
        fig.clear()
        plt.plot(self.xValues, self.collatzNumbers)
        plt.draw()
        plt.xlabel("Steps")
        plt.ylabel("Numbers after each iteration")
        plt.title("Measurements")
        plt.show()

    def run(self):
        self.computeCollatzNumbers()
        self.plotNumbers()

if __name__ == '__main__':
    print("Program that shows Collatz Conjecture and Hillstone numbers")
    numbersString = ""
    while numbersString == "" or numbersString == "0":
        inputString = input("Provide the number not equal to 0 and an integer: ")
        numbersString = re.sub('[!?@#$\[\]<>%^&*()a-zA-Z]', '', inputString)
        if numbersString == "" or numbersString == "0":
            print("Input must be a number and not equal to 0!")
    number = int(numbersString)
    collatz = CollatzConjecture(number)
    collatz.run()