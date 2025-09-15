while True:
    password = input("Enter password (at least 6 characters): ")
    if len(password) < 6:
        print("Password too short, try again.")
        continue

    confirm = input("Confirm your password: ")
    if password != confirm:
        print("Paswrd do not match, try again.")
        continue
    print("Password accepted.")
    break
