class Factorial:
    def __init__(self):
        pass
    
    def fact(self, number) -> int:
        if number >= 0 and number <= 1:
            return 1
        else:
            return number * self.fact(number-1) 

if __name__ == "__main__":
    newFact = Factorial()
    print(newFact.fact(3))