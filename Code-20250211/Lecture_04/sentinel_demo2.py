total = 0
count = 0

while True:
    prompt = "Input score [0-100], -1 to end: "
    score = int(input(prompt))
    if score == -1:
        break
    
    total += score
    count += 1

if count > 0:
    average = total / count
    print(f"Average: {average:.2f}")