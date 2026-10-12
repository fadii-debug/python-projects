# oop
class Ac:
    def behave(winter):
        print("in winter Ac use as inverter to provide hot air")

class Ac_inverter:
    def behave(summer):
        print("in summer Ac provide cold air")

obj1=Ac()
obj2=Ac_inverter()

def perform(cold):
    return(cold.behave())

perform(obj1)
perform(obj2)
