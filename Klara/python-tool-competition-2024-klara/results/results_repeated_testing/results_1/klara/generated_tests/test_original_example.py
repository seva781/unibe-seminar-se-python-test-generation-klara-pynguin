import original_example


def test_triangle_0():
    assert original_example.triangle(0, 0, 0) == 'Equilateral triangle'
    assert original_example.triangle(0, 0, 1) == 'Isosceles triangle'
    assert original_example.triangle(2, 0, 1) == 'Scalene triangle'
