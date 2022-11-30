import matplotlib.pyplot as plt
import re


class CollatzConjecture():
    def __init__(self, start_number):
        self.start_number = start_number
        self.collatz_numbers = []
        self.x_values = []

    def compute_collatz_numbers(self):
        number = self.start_number
        iteration = 0
        self.collatz_numbers.append(number)
        self.x_values.append(iteration)
        while (number != 1 and number != -1 and number != -5 and number != -17) or iteration == 0:
            if number % 2 == 0:
                number = int(number/2)
            else:
                number = int(3*number + 1)
            iteration += 1
            self.collatz_numbers.append(number)
            self.x_values.append(iteration)
        print(f"Collatz numbers for the number {self.start_number}: {self.collatz_numbers}")
        print(f"Number of steps: {len(self.x_values) - 1}")
        if self.collatz_numbers[0] > 0:
            print(f"Maximum number: {max(self.collatz_numbers)}")
        else:
            print(f"Maximum number: {min(self.collatz_numbers)}")
    
    def plot_numbers(self):
        fig = plt.figure("Colatz Conjecture Graph")
        fig.clear()
        plt.plot(self.x_values, self.collatz_numbers, marker="o")
        plt.draw()
        plt.xlabel("Steps")
        plt.ylabel("Numbers after each iteration")
        plt.title("Hillstone/3n + 1 Numbers")
        plt.show()

    def run(self):
        self.compute_collatz_numbers()
        self.plot_numbers()


if __name__ == '__main__':
    print("Program that shows Collatz Conjecture and Hillstone numbers")
    numbers_string = ""
    while numbers_string == "" or numbers_string == "0":
        input_string = input("Provide a non-zero integer number: ")
        numbers_string = re.sub('[!?@#$\[\]<>%^&*()a-zA-Z]', '', input_string)
        if numbers_string == "" or numbers_string == "0":
            print("Input must be a number and not equal to 0!")
    number = int(numbers_string)
    collatz = CollatzConjecture(number)
    collatz.run()