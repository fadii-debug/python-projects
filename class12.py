# public------name, account number
# protected-------amount
# private---------pin code
class A:
    def __init__(self, name, amount, pin):
        self.name=name
        self._amount=amount
        self.__pin=pin



obj=A("fahad", 2222222222, 1978)
print(obj.name)
print(obj._amount)
print(obj._A__pin)