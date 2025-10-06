ans = "y"
running_count = 0
while ans == "y":
    start = int(input("Enter start number: "))
    end = int(input("How hight shoud I go? "))
    if start >= end:
        print("Error: Starting number must be less than ending number.")
    else:
        print("-" * 16)
        print(f"{'Number':^8}{'Square':^8}")
        print("-" * 16)
        for num in range(start, end + 1):
            num_spuare = num**2
            print(f"{num:^8}{num_spuare:^8}")
        running_count += 1
        
        ans = input("Do you want to run again? (enter y for yes) ")
print("thank you")
