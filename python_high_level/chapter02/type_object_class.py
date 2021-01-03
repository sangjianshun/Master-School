# type -> int -> 1
# type -> class -> obj

# object是顶层基类
# type本身也是一个类，同时type也是对象
# 一切都继承了object，所有的都是type的对象，type自己也是type的对象。
class Student(object):
    pass
print(type(Student))
print(type(type))
print(type(object))

print("#################")
class OneStudent(Student):
    pass
person = OneStudent()
print(type(OneStudent))
print(type(person))

print("####")
print(Student.__bases__)
print(OneStudent.__bases__)
print(type.__bases__)
print(object.__bases__)

print("#############")
# class是一个对象(一切皆对象)，可以用生成的类去实例化对象，1其实是int这个类实例化的对象，
# int本身也是一个对象，是通过type实例化的。类建的类。
# object是所有的类继承的基类(包括type这个类)，是最顶层的基类。
# objecct这个对象是type这个类生成的（object是type的一个实例），object是空生成的。
# 所有的类都是type的对象，包括type自己也是type的对象，所以一切皆对象
# object这个类也是type的对象，是所有类的基类。
a = 1
print(type(1))
print(type(int))


