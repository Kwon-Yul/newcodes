class Dog:
    def __init__(self,name):
        self.name = name
        
    def bark(self):
        print("내 이름은 {} 멍멍".format(self.name))
        
my_dog = Dog('jindo')
my_dog.bark()