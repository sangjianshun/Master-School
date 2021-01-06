class School():
    def __init__(self,teacher_list):
        self.teacher = teacher_list
    def __getitem__(self, item):
        print(item)
        return self.teacher[item]
    def __len__(self):
        return 1000000
    def __repr__(self):
        return "repre hello world"

# # 字典行不通
# teacher = {"Jane":1, "Baby":2}
# school = School(teacher)

school = School(["Jane","Baby"])
print(school[1])

print(len(school))
print(repr(school))

class MyVector():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        res = MyVector(self.x + other.x, self.y +other.y)
        return res
    def __str__(self):
        return ("x:{},y:{}").format(self.x,self.y)
vec1 = MyVector(1,2)
vec2 = MyVector(3,4)
print(vec1 + vec2)