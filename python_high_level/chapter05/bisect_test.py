import bisect

inter_list = []
bisect.insort(inter_list, 4)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 7)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 10)
bisect.insort(inter_list, 4)

print(inter_list)
print(bisect.bisect(inter_list,4))
print(bisect.bisect_left(inter_list,4))
print(bisect.bisect_right(inter_list,4))



