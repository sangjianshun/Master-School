new_list = ["list1","list2"]
new_dict = dict.fromkeys(new_list, "value")
print(new_dict)
print(new_dict.get("list3"))

default_value = new_dict.setdefault("list_default", "value_default")
new_dict.update(list3 = "value_list3")
print(default_value)
print(new_dict)