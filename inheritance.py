class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

        print("created a new person")

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

class Student(Person):

    def __init__(self, name, age, year):
        self.name = name
        self.age = age
        self.year = year

        print("created a new student")

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old. I am a student")

class Teacher(Person):

    def __init__(self, name, age, is_tenured):
        super().__init__(name, age)
        self.is_tenured = is_tenured

        print("created a new teacher")


def main():
    person = Person("Bob", 20)
    student = Student("Alice", 20, "2nd")
    teacher = Teacher("Cliff", 35, True)

    person.introduce()
    student.introduce()
    teacher.introduce()


if __name__ == "__main__":
    main()
