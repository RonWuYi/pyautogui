class People:
    sex = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def print_hello(x):
        print("hello {}".format(x))

    @classmethod
    def print_salary(cls, salary):
        print("salary is {}".format(salary))

    @property
    def get_name(self):
        return self.name


People.print_hello("fuck")
People.print_salary(1234)
p = People("NOBODAY", 4567)
print(p.get_name)