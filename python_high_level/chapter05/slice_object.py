import numbers


class Group():
    def __init__(self, group_name,company_name,staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        return self.staffs.reverse()
    def __getitem__(self, item): #实现切片的关键,没有的话会报错TypeError: 'Group' object is not subscriptable
        # return self.staffs[item] # item可以是slice，也可以是int
        cls = type(self)
        if isinstance(item, slice):
            return cls(self.group_name,self.company_name,self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(self.group_name,self.company_name,[self.staffs[item]])

    def __len__(self):
        return len(self.staffs)
    def __iter__(self):
        return iter(self.staffs)
    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False

staffs = ["s1","s2","s3"]
group = Group(company_name="company_test", group_name="group_test",staffs = staffs)
sub_group = group[:2]
sub_group = group[0]

print(len(group))
if "s1" in group:
    print("s1")
for user in group:
    print(user)

print(group.staffs)
reversed(group)
print(group.staffs)
