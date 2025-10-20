list1 = [0, 1, 2, 3, 4, 5]
list1 = list1[1:][1:]
print(list1)
# [2, 3, 4, 5]

list1 = []
for num in range(1, 6):
    list1.append(num)
print(f"{list1 = }")  # list1 = [1, 2, 3, 4, 5]

list2 = [num for num in range(1, 6)]  # list2 = [1, 2, 3, 4, 5]
list2 = [num for num in range(1, 6) if num * 2 > 5]  # list2 = [3, 4, 5]

list1 = [1, 46, 23, 67, 26, 45]
even = [e for e in list1 if e % 2 == 0]
odd = [e for e in list1 if e % 2 == 1]

print(even)
print(odd)


list1 = [[11, 2, 3], [4, 5, 6]]
ans = sum(list1, [1])  # [1, 11, 2, 3, 4, 5, 6] เออตัวหลังไปอยู่ด้านหน้า
print(ans)
