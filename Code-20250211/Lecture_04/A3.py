total = 0
count = 0
score = int(input("Input score [0-100], -1 to end: "))

while score < -1 or score > 100:
    print("Error: Incorrect score!")
    score = int(input("Input score [0-100], -1 to end: "))
while score != -1:  # -1 -> Sentinel value
    total += score
    score = int(input("Input score [0-100], -1 to end: "))
    count += 1
    while score < -1 or score > 100:
        print("Error: Incorrect score!")
        score = int(input("Input score [0-100], -1 to end: "))
if count > 0:
    avg = total / count
    print(f"Average: {avg:.2f}")
