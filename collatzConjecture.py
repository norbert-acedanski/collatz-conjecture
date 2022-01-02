import matplotlib.pyplot as plt
import re

class CollatzConjecture():
    def __init__(self, startNumber):
        self.startNumber = startNumber
        self.collatzNumbers = []
        self.xValues = []

    def computeCollatzNumbers(self):
        number = self.startNumber
        iteration = 0
        self.collatzNumbers.append(number)
        self.xValues.append(iteration)
        while (number != 1 and number != -1 and number != -5 and number != -17) or iteration == 0:
            if number % 2 == 0:
                number = int(number/2)
            else:
                number = int(3*number + 1)
            iteration += 1
            self.collatzNumbers.append(number)
            self.xValues.append(iteration)
        print("Collatz numbers for the number " + str(self.startNumber) + ": " + str(self.collatzNumbers))
        print("Number of steps: " + str(len(self.xValues) - 1))
        if self.collatzNumbers[0] > 0:
            print("Maximum number: " + str(max(self.collatzNumbers)))
        else:
            print("Maximum number: " + str(min(self.collatzNumbers)))
    
    def plotNumbers(self):
        fig = plt.figure("Colatz Conjecture Graph")
        fig.clear()
        plt.plot(self.xValues, self.collatzNumbers, marker="o")
        plt.draw()
        plt.xlabel("Steps")
        plt.ylabel("Numbers after each iteration")
        plt.title("Hillstone/3n + 1 Numbers")
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