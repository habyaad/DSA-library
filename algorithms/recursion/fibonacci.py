### 1,1,2,3,5,8,13...
class Fibonacci:
    def __init__(self):
        pass
    
    def fib(self, number) -> int:
        if number > 0 and number<=2:
            return 1
        else:
            return self.fib(number-1)  + self.fib(number-2) 
    def fibList(self, number) -> list:
        fib_list = [1,1]
        if number ==1:
            return [1]
        elif number ==2:
            return fib_list
        else:
            for i in range(number-2):
                fib_list.append(fib_list[i]+fib_list[i+1])

            return fib_list
        

if __name__ == "__main__":
    newFib = Fibonacci()
    print(newFib.fib(7))
    print(newFib.fibList(2))