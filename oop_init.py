class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Привет! Меня зовут", self.name)

p = Person("Alex")
p.say_hi()

# Предыдущие две строки можно
# Person('Swaroop').say_hi()