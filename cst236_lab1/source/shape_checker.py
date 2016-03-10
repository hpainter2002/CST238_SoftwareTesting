"""
:mod:`source.source1` -- Example source code
============================================

The following example code determines if a set of 3 sides of a triangle is equilateral, scalene or iscoceles
"""


def get_triangle_type(a=0, b=0, c=0):
    """
    Determine if the given triangle is equilateral, scalene or Isosceles

    :param a: line a
    :type a: float or int or tuple or list or dict

    :param b: line b
    :type b: float

    :param c: line c
    :type c: float

    :return: "equilateral", "isosceles", "scalene" or "invalid"
    :rtype: str
    """
    if isinstance(a, (tuple, list)) and len(a) == 3:
        c = a[2]
        b = a[1]
        a = a[0]

    if isinstance(a, dict) and len(a.keys()) == 3:
        values = []
        for value in a.values():
            values.append(value)
        a = values[0]
        b = values[1]
        c = values[2]

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        return "invalid"

    if a <= 0 or b <= 0 or c <= 0:
        return "invalid"

    if a == b and b == c:
        return "equilateral"

    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"

def get_rectangle_type(a=0, b=0, c=0, d=0):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)) and isinstance(c
            , (int, float))):
        return "invalid"

    if a <= 0 or b <= 0 or c <= 0 or d <= 0:
        return "invalid"

    if a == b and a == c and a == d:
        return "square"

    elif a == b and c == d or a == c and b == d or a == d and b == c:
        return "rectangle"
    else:
        return "invalid"

def get_quadrilateral_type(side1=0, side2=0, side3=0, side4=0, ang1=0, ang2=0, ang3=0, ang4=0):
    if not (isinstance(side1, (int, float)) and isinstance(side2, (int, float)) and isinstance(side3, (int, float)) and
            isinstance(side4, (int, float)) and isinstance(ang1, (int, float)) and isinstance(ang2, (int, float))
            and isinstance(ang3, (int, float)) and isinstance(ang4, (int, float))):
        return "invalid"

    if side1 <= 0 or side2 <= 0 or side3 <= 0 or side4 <= 0 or ang1 <= 0 or ang2 <= 0 or ang3 <= 0 or ang4 <= 0:
        return "invalid"

    if ang1 == 90 and ang2 == 90 and ang3 == 90 and ang4 == 90:
        return get_rectangle_type(side1, side2, side3, side4)

    elif (ang1 + ang2 + ang3 + ang4) == 360:
        return "rhombus"
    else:
        return "disconnected"

