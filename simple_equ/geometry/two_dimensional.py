from . import constants
import simple_equ.algebra.algebra as algebra

def pythagoras(a: int | float, b: int | float) -> float:
    """[Summary]: Return the hypotenuse of a right triangle.

    [Description]: Squares the two provided legs, sums them, and uses the local
    square-root helper from the algebra module to compute the hypotenuse.

    [Usage]: Typical usage example:

        result = pythagoras(3, 4)
        print(result)
    """
    result = a * a + b * b
    hypotenuse = algebra.sqrt(result)
    return hypotenuse


def square_area(a: int | float):
    """[Summary]: Return the area of a square.

    [Description]: Multiplies the side length by itself to compute the area of a
    square using the standard geometric formula.

    [Usage]: Typical usage example:

        result = square_area(4)
        print(result)
    """
    return a * a


def rectangle_area(a: int | float, b: int | float):
    """[Summary]: Return the area of a rectangle.

    [Description]: Multiplies the length and width values to compute the area of
    a rectangle.

    [Usage]: Typical usage example:

        result = rectangle_area(4, 6)
        print(result)
    """
    return a * b


def circle_area(radius: int | float) -> float:
    """[Summary]: Return the area of a circle.

    [Description]: Uses the mathematical constant pi from the local constants
    module and the standard formula pi * r^2 to compute the result.

    [Usage]: Typical usage example:

        result = circle_area(5)
        print(result)
    """
    return constants.pi * (radius**2)


def trapezoid_area(base_one: int | float, base_two: int | float, height: int | float):
    """[Summary]: Return the area of a trapezoid.

    [Description]: Averages the two base lengths and multiplies that value by
    the height to compute the area of the trapezoid.

    [Usage]: Typical usage example:

        result = trapezoid_area(3, 5, 4)
        print(result)
    """
    return (base_one + base_two) / 2 * height


def triangle_area(base: int | float, height: int | float):
    """[Summary]: Return the area of a triangle.

    [Description]: Multiplies the base by the height and divides the result by
    two to compute the triangle's area.

    [Usage]: Typical usage example:

        result = triangle_area(6, 4)
        print(result)
    """
    return (base * height) / 2


def regular_polygon_area(apothem: int | float, perimeter: int | float):
    """[Summary]: Return the area of a regular polygon.

    [Description]: Multiplies the apothem by the perimeter and divides the
    result by two to compute the area of a regular polygon.

    [Usage]: Typical usage example:

        result = regular_polygon_area(4, 20)
        print(result)
    """
    return (apothem * perimeter) / 2


def calculate_radius(diameter: int | float):
    """[Summary]: Return the radius derived from a diameter.

    [Description]: Divides the given diameter by two to convert it into a
    radius.

    [Usage]: Typical usage example:

        result = calculate_radius(10)
        print(result)
    """
    return diameter / 2


def circumference(radius: int | float):
    """[Summary]: Return the circumference of a circle.

    [Description]: Uses the standard formula 2 * pi * r to compute the distance
    around a circle for the provided radius.

    [Usage]: Typical usage example:

        result = circumference(5)
        print(result)
    """
    return 2 * constants.pi * radius


def distance(a: tuple | list | list, b: tuple | list | list) -> float:
    # Convert any lists to tuples
    """[Summary]: Return the Euclidean distance between two 2D or 3D points.

    [Description]: Accepts tuples or lists as coordinates, normalizes them to
    tuples, validates the dimensionality, and computes the Euclidean distance in
    either two or three dimensions.

    [Usage]: Typical usage example:

        result = distance((0, 0), (3, 4))
        print(result)
    """
    a, b = tuple(a), tuple(b)

    if not all(isinstance(x, tuple) for x in (a, b)):
        raise TypeError("Must input tuples or lists as coordinates for points")

    if len(a) == 2 and len(b) == 2:
        formula = ((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2)
        result = algebra.sqrt(formula)
        return result
    elif len(a) == 3 and len(b) == 3:
        formula = ((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2) + ((a[2] - b[2]) ** 2)
        result = algebra.sqrt(formula)
        return result
    raise ValueError("Inputs must be either 2d or 3d coordinates")


def slope(point_one: tuple, point_two: tuple) -> float:
    """[Summary]: Return the slope between two 2D points.

    [Description]: Validates that both inputs represent two-dimensional points
    and then computes the slope using the change in y over the change in x.

    [Usage]: Typical usage example:

        result = slope((1, 2), (3, 6))
        print(result)
    """
    if len(point_one) != 2 or len(point_two) != 2:
        raise ValueError("Points must be 2D coordinates")
    return (point_two[1] - point_one[1]) / (point_two[0] - point_one[0])
