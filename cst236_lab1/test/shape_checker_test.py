"""
Test for source.shape_checker
"""
from source.shape_checker import get_triangle_type
from unittest import TestCase
from source.shape_checker import get_quadrilateral_type

class TestGetTriangleType(TestCase):

# Int test
    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_all_int(self):
        result = get_triangle_type(4, 4, 5)
        self.assertEqual(result, 'isosceles')

# Float test
    def test_get_triangle_equilateral_all_float(self):
        result = get_triangle_type(2.0, 2.0, 2.0)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_float(self):
        result = get_triangle_type(1.0, 2.0, 3.0)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_all_float(self):
        result = get_triangle_type(2.0, 2.0, 5.0)
        self.assertEqual(result, 'isosceles')

# Char test
    def test_get_triangle_equilateral_all_char(self):
        result = get_triangle_type('a', 'd', 'v')
        self.assertEqual(result, 'invalid')

    def test_get_triangle_scalene_all_char(self):
        result = get_triangle_type('r', 'g', 'h')
        self.assertEqual(result, 'invalid')

    def test_get_triangle_isosceles_all_char(self):
        result = get_triangle_type('q', 'r', 'n')
        self.assertEqual(result, 'invalid')

# Float/Int combination test
    def test_get_triangle_equilateral_float_int_combo(self):
        result = get_triangle_type(2, 2.0, 2.0)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_float_int_combo(self):
        result = get_triangle_type(1.0, 2, 3.0)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_float_int_combo(self):
        result = get_triangle_type(2.0, 2, 5)
        self.assertEqual(result, 'isosceles')

# Tuples test
    def test_get_triangle_equilateral_tuple(self):
        tup1 = (2, 2, 2)
        result = get_triangle_type(tup1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_tuple(self):
        tup1 = (1.0, 2, 3)
        result = get_triangle_type(tup1)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_all_tuple(self):
        tup1 = (2, 2.0, 5)
        result = get_triangle_type(tup1)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_invalid_tuple(self):
        tup1 = (1, 2.0, 5, 43)
        result = get_triangle_type(tup1)
        self.assertEqual(result, 'invalid')

# List test
    def test_get_triangle_equilateral_list(self):
        tup1 = [2, 2, 2]
        result = get_triangle_type(tup1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_list(self):
        tup1 = [1.0, 2, 3]
        result = get_triangle_type(tup1)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_all_list(self):
        tup1 = [2, 2.0, 5]
        result = get_triangle_type(tup1)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_invalid_list(self):
        tup1 = [1, 2.0, 5, 43]
        result = get_triangle_type(tup1)
        self.assertEqual(result, 'invalid')

# Dicionary test
    def test_get_triangle_equilateral_dic(self):
        dic1 = {'one' : 1, 'two' : 1, 'three' : 1}
        result = get_triangle_type(dic1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_dic(self):
        dic1 = {'one' : 1, 'two' : 2, 'three' : 3}
        result = get_triangle_type(dic1)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_all_dic(self):
        dic1 = {'one' : 1, 'two' : 1, 'three' : 4}
        result = get_triangle_type(dic1)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_invalid_dic(self):
        dic1 = {'one' : 1, 'two' : 1, 'three' : 1, 'four' : 5}
        result = get_triangle_type(dic1)
        self.assertEqual(result, 'invalid')

# Zero and negative test
    def test_get_triangle_zero_neg(self):
        result = get_triangle_type(0, -5, 2)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_two_zero(self):
        result = get_triangle_type(0, 4, 0)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_all_zero(self):
        result = get_triangle_type(0, 0, 0)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_all_neg(self):
        result = get_triangle_type(-6, -4, -3)
        self.assertEqual(result, 'invalid')


class TestGetQuadrilateralType(TestCase):

# Int test
    def test_get_quadrilateral_type_all_int(self):
        result = get_quadrilateral_type(2, 2, 2, 2, 90, 90, 90, 90)
        self.assertEqual(result, 'square')

    def test_get_quad_invalid_all_int(self):
        result = get_quadrilateral_type(1, 2, 3, 4, 90, 90, 90, 90)
        self.assertEqual(result, 'invalid')

    def test_get_quad_rect_type_all_int(self):
        result = get_quadrilateral_type(1, 2, 1, 2, 90, 90, 90, 90)
        self.assertEqual(result, 'rectangle')

    def test_get_quad_disconnected_all_int(self):
        result = get_quadrilateral_type(1, 2, 1, 2, 270, 90, 90, 90)
        self.assertEqual(result, 'disconnected')

    def test_get_quad_rhombus_all_int(self):
        result = get_quadrilateral_type(1, 2, 1, 4, 180, 45, 45, 90)
        self.assertEqual(result, 'rhombus')

# Float test
    def test_get_quadrilateral_type_all_float(self):
        result = get_quadrilateral_type(2.0, 2.0, 2.0, 2.0, 90.0, 90.0, 90.0, 90.0)
        self.assertEqual(result, 'square')

    def test_get_quad_invalid_all_float(self):
        result = get_quadrilateral_type(1.0, 2.0, 3.0, 4.0, 90.0, 90.0, 90.0, 90.0)
        self.assertEqual(result, 'invalid')

    def test_get_quad_rect_type_all_float(self):
        result = get_quadrilateral_type(1.0, 2.0, 1.0, 2.0, 90.0, 90.0, 90.0, 90.0)
        self.assertEqual(result, 'rectangle')

    def test_get_quad_disconnected_all_float(self):
        result = get_quadrilateral_type(1.0, 2.0, 1.0, 2.0, 270.0, 90.0, 90.0, 90.0)
        self.assertEqual(result, 'disconnected')

    def test_get_quad_rhombus_all_float(self):
        result = get_quadrilateral_type(1.0, 2.0, 1.0, 4.0, 180.0, 45.0, 45.0, 90.0)
        self.assertEqual(result, 'rhombus')

# Char test
    def test_get_quadrilateral_type_all_char(self):
        result = get_quadrilateral_type('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
        self.assertEqual(result, 'invalid')

    def test_get_quad_invalid_some_char(self):
        result = get_quadrilateral_type(1.0, 2.0, 3.0, 'f', 90.0, 90.0, 'b', 90.0)
        self.assertEqual(result, 'invalid')

    def test_get_quad_rect_type_some_char(self):
        result = get_quadrilateral_type(1.0, 2.0, 'k', 2.0, 90.0, 90.0, 'b', 90.0)
        self.assertEqual(result, 'invalid')

    def test_get_quad_disconnected_some_char(self):
        result = get_quadrilateral_type(1.0, 2.0, 'k', 2.0, 'f', 'v', 90.0, 90.0)
        self.assertEqual(result, 'invalid')

    def test_get_quad_rhombus_all_char(self):
        result = get_quadrilateral_type('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
        self.assertEqual(result, 'invalid')

# Float/Int combination test
    def test_get_quadrilateral_type_int_float_combo(self):
        result = get_quadrilateral_type(2, 2.0, 2, 2.0, 90, 90.0, 90, 90.0)
        self.assertEqual(result, 'square')

    def test_get_quad_invalid_int_float_combo(self):
        result = get_quadrilateral_type(1, 2.0, 3.0, 4, 90.0, 90, 90.0, 90)
        self.assertEqual(result, 'invalid')

    def test_get_quad_rect_type_int_float_combo(self):
        result = get_quadrilateral_type(1.0, 2, 1, 2.0, 90, 90.0, 90, 90.0)
        self.assertEqual(result, 'rectangle')

    def test_get_quad_disconnected_int_float_combo(self):
        result = get_quadrilateral_type(1.0, 2, 1, 2.0, 270, 90.0, 90, 90.0)
        self.assertEqual(result, 'disconnected')

    def test_get_quad_rhombus_int_float_combo(self):
        result = get_quadrilateral_type(1.0, 2.0, 1, 4, 180, 45, 45.0, 90.0)
        self.assertEqual(result, 'rhombus')

# Zero and negative test
    def test_get_quadrilateral_type_neg_zero_combo(self):
        result = get_quadrilateral_type(0, 2.0, 2, -90, 90, -90.0, 0, 90.0)
        self.assertEqual(result, 'invalid')

    def test_get_quad_invalid_all_zeros(self):
        result = get_quadrilateral_type(0, 0, 0, 0, 0, 0, 0, 0)
        self.assertEqual(result, 'invalid')

    def test_get_quad_rect_type_all_neg(self):
        result = get_quadrilateral_type(-2.0, -7, -9, -89, -65, -90.0, -180, -90.0)
        self.assertEqual(result, 'invalid')

