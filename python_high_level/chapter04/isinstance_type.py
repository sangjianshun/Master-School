class A:
    pass

class B(A):
    pass

b = B()

print(type(b))  # <class '__main__.B'>
print(isinstance(b,B))
print(isinstance(b,A))
