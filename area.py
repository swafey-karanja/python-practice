def calc_area(base, height):
    print("__name__:",__name__)
    return 1 / 2 * (base * height)


if "_main_" == __name__:
    print("i am in area.py")
    a = calc_area(20, 50)
    print("area: " , a)