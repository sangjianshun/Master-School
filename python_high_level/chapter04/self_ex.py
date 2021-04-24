# 自省是通过一定的机制查询到对象的内部结构

class Person:
    name = "user"

class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name

if __name__ == '__main__':
    user = Student("ssstudent")

    # 通过__dict__查询属性
    # 实例的属性
    print(user.__dict__)  # {'school_name': 'ssstudent'}，name并不是user的属性

    user.__dict__["school_name"] = "tttest"
    print(user.school_name)

    # 类的属性很多
    print(Person.__dict__) ## {'__module__': '__main__', 'name': 'user', '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
    print(user.name)

    # dir
    print(dir(user)) #['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'school_name']
