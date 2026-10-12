# the car class 


class car:
    def __init__(self, brand, colour):
        self.brand=brand
        self.colour=colour
        self.isruning=False

    def start(self):
        if self.isruning:
            print(f"the{self.brand}is already runing")
        else:
            self.isruning=True
            print(f"the{self.brand}start vroooom")

    def stop(self):
        if self.isruning:
            self.isruning=False
            print("Toyota engine is turn off")
        else:
            print(f"the{self.brand}is already off")


obj=car("toyota","black")
obj=car("ford", "gray")
print(obj.brand)
print(obj.colour)
obj.start()
obj.stop()