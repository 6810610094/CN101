def stat(data):
    minimum = min(data)
    maximum = max(data)
    mean = sum(data) / len(data)
    return minimum, maximum, mean


def main():
    input_list = input("Enter data: ").split()
    # data = []
    # for item in input_list:
    #    data.append(float(item))
    data = [float(n) for n in input_list]
    mn, mx, mean = stat(data)
    print(f"min = {mn}, max = {mx}, mean = {mean}")


main()
