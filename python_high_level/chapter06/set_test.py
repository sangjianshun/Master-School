s = set("abcd")
print(s)
s = set(["a","b","c","d"])
print(s)

s = {"a","b"}
print(type(s))

s = frozenset("abcd") # 不可变，可以作为dict的key



#update
another_set = set("def")
s.update(another_set) # 相当于 s | another_set
print(s)

# difference和-是一样的
s1 = {"a","b"}
s2 = set("bde")
print(s1.difference(s2)) #相当于s1-s2

