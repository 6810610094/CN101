# circle.py
PI = 3.14159  # Global Constant


def find_circle_area(radius):
    area = PI * radius**2
    return area
    # print(f"Circle area: {area:.2f}")


def find_circumference(radius):
    circumference = 2 * PI * radius
    return circumference
    # print(f"Circumference: {circumference:.2f}")


def main():
    radius = int(input("Input a radius: "))
    area = find_circle_area(radius)
    circumference = find_circumference(radius)
    print(f"Circle area: {area:.2f}")
    print(f"Circumference: {circumference:.2f}")
    pass


main()
