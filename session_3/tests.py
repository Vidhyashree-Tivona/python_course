from geometry.circle import get_circle_area, get_circle_circumference
from geometry.rectangle import get_rect_area, get_rect_perimeter

print("Selct an option")
print("1.Find area & circumference of circle \n")
print("2.Find area & perimeter of rectangle")
option = int(input("select any option 1 or 2: "))
if option == 1:
    radius = eval(input("Enter the radius value: "))

    def test_circle():
        print("Area of circle: ", get_circle_area(radius))
        print("Circumference of circle: ", get_circle_circumference(radius))
    test_circle()

elif option == 2:
    length = eval(input("Enter the value of length: "))
    breadth = eval(input("Enter the value of breadth: "))

    def test_rect():
        print("Area of rectangle: ", get_rect_area(length, breadth))
        print("Perimeter of rectangle: ", get_rect_perimeter(length, breadth))
    test_rect()

else:
    print("Invalid option selected")
