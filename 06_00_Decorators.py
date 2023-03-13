'''A decorator is a design pattern in Python that allows a user to add new functionality to an existing
object without modifying its structure. Decorators are usually called before the definition of a function
you want to decorate.'''
def Mydec(func1):
    def demoexe():
        print("1")
        func1()
        print("2")
    return demoexe

@Mydec
def MyNameIs():
    print("My Name Is :Nitin")

MyNameIs()