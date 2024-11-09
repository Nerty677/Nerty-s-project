class Human:

    height = 170
    gladness = 0

class Student(Human):
    gladness = 40

class Worker(Human):
    gladness = 60

nick = Student()
ann = Worker()

print(nick.height)
print(ann.gladness)
print(ann.height)
print(ann.gladness)

class GrandParent:
    height = 170
    gladness = 90
    age = 70

class Parent(GrandParent):
    age = 30

class Child(Parent):
    height = 100

    def __init__(self):
        print(self.height)
        print(self.gladness)
        print(self.age)


ch = Child()

class hello_world:
    hello = 'hello'
    _hello = 'hello'
    __hello = 'hello'

    def __init__(self):
        self.world = 'world'
        self._world = '_world'
        self.__world ='__world'
    def printer(self):
        print(self.hello + self.world)
        print(self._hello + self._world)
        print(self.__hello + self.__world)


 class test(hello_world):


    def test_print(self)






        hello = hello_world()
        hello.printer()
        t = test()
        t.test_print()



class Class1:

    def __init__(self):
        print('hello')


class Class2(Class1):

   def __init__(self):
       super().__init__()
       print('World')


x = Class2()

class Class1:
   var = 20
   def __init__(self):
       self.var = 10


class Class2(Class1):

   def __init__(self):
       print(self.var)
       super().__init__()
       print(self.var)
       print(super().var)

x = Class2()


class Computer:

    def calculate(self):
        print('calculating')


class Display:
def __init__(self):
 def display(self):
        print('I show the image on the screen...')

class SmartPhone(Display, Computer):
    def info(self):
        print(self.memory)
        print(self.resolution)
iphone = SmartPhone()
iphone.display()
iphone.calculate()