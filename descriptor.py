class DefaultNumber():
    def __set_name__(self, obj, name):
        print("set name")
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, obj, owner):
        print("get name activated")
        return getattr(obj, self.private_name)
	
    def __set__(self, obj, value):
        print("set activated")
        setattr(obj, self.private_name, value)


class SomeRandomClass():
    special_number = 228
    another_number = DefaultNumber()

    def __init__(self, first, second):
        self.special_number = first
        self.another_number = second


temp = SomeRandomClass(322, 228)
print(vars(temp))
print(temp.another_number)