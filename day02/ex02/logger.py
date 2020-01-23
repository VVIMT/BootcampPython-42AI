import time
from random import randint

def log(func, **kwargs):
    start = time.time()

    f = open("C:\\Users\\Vincent\\source\\repos\\Bootcamp-42AI\\day02\\ex02\\machine.log", "a")
    f.write("(vinvimo):Running " + func.__name__ + "   [ exec-time = " + str(time.time() - start)) + " ] \n")
    f.close()
    return func

class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False
    
    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":

    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
