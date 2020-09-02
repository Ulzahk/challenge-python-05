import math


def square_area(side):
    """Returns the area of a square"""
    return side * side 


def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    return base * height


def triangle_area(base, height):
    """Returns the area of a triangle"""
    return (base * height) / 2


def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    return (diagonal_1 * diagonal_2) / 2


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    return height * ((base_minor + base_major) / 2)


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    return (perimeter * apothem) / 2


def circumference_area(radius):
    """Returns the area of a circumference"""
    return round((math.pi * (radius**2)), 2)


if __name__ == '__main__':
    import unittest

    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            # Initialize the needed values for the tests
            self.square_data = {
                16 : 4,
                25 : 5,
                144 : 12,
            }
            self.rectangle_data = {
                12 : [3, 4],
                36 : [6, 6],
                220 : [22, 10]
            }
            self.triangle_data = {
                24 : [6, 8],
                50 : [10, 10],
                170 : [17, 20]
            }
            self.rhombus_data = {
                7.5 : [5, 3],
                44 : [11, 8],
                110.5 : [13, 17]
            }
            self.trapezoid_data = {
                60 : [5, 10, 8],
                102 : [13, 12.5, 8],
                75.4 : [9, 20, 5.2]
            }
            self.regular_polygon_data = {
                93.75 : [25, 7.5],
                311.25 : [75, 8.3],
                210: [140, 3]
            }
            self.circumference_data = {
                28.27 : 3,
                165.13 : 7.25,
                415.48 : 11.5
            }


        def test_square_area(self):
            for key, value in self.square_data.items():
                self.assertEqual(key, square_area(value))


        def test_rectangle_area(self):
            for key, value in self.rectangle_data.items():
                self.assertEqual(key, rectangle_area(value[0], value[1]))


        def test_triangle_area(self):
            for key, value in self.triangle_data.items():
                self.assertEqual(key, triangle_area(value[0], value[1]))


        def test_rhombus_area(self):
            for key, value in self.rhombus_data.items():
                self.assertEqual(key, rhombus_area(value[0], value[1]))


        def test_trapezoid_area(self):
            for key, value in self.trapezoid_data.items():
                self.assertAlmostEqual(key, trapezoid_area(value[0], value[1], value[2]))


        def test_regular_polygon_area(self):
            for key, value in self.regular_polygon_data.items():
                self.assertEqual(key, regular_polygon_area(value[0], value[1]))


        def test_circumference_area(self):
            for key, value in self.circumference_data.items():
                self.assertEqual(key, circumference_area(value))


        def tearDown(self):
            # Delete the needed values for the tests
            del(
                self.square_data,
                self.rectangle_data,
                self.triangle_data,
                self.trapezoid_data,
                self.regular_polygon_data,
                self.circumference_data
            )


    unittest.main()
