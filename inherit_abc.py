from abc import *

from inherit import member


class SchoolMember(metaclass=ABCMeta):
    """Представляет любого человека в школе."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.format(self.name))

    @abstractmethod
    def tell(self):
        """Вывести информацию."""
        print('Имя: "{0}" Возраст: "{1}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    """Представляет преподавателя."""
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        print('(Создан Teacher: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))

class Student(SchoolMember):
    """Представляет студента."""
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

#m = SchoolMember('abc', 10)
# Это приведёт к ошибке: "TypeError: Can't instantiate abstract class
# SchoolMember with abstract methods tell"

print() # печатает пустую строку

members = [t, s]
for member in members:
    member.tell() # работает как для преподавателя, так и для студента
