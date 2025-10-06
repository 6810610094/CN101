total = 0
for num in range(1, 900):
    if num % 3 != 0:
        total += num
print(f"{total = :,}")
