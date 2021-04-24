class A:
    pass

class B(A):
    pass

b = B()

print(type(b))  # <class '__main__.B'>
print(isinstance(b,B)) # True
print(isinstance(b,A)) # True
print(isinstance(b,object)) # True