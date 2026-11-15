lst = ["apple", "banana", "cherry", "kiwi"]
print("Length of list:", len(lst))
print("First element:", lst[0])
print("Last element :", lst[-1])

lst.append("papaya")
print("updated list:", lst)

lst.remove("banana")
print("updated list:", lst)

lst.sort()
print("sorted list:", lst)

lst.pop(1)
print("updated list:", lst)

lst.reverse()
print("reversed list:", lst)

print("multiplication of list:", lst*2)

lst = lst[:4]
print("sliced list:", lst)

lst.clear()
print("cleared list:", lst)
