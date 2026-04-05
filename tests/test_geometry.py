import pytest
import math
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
from simple_equ.math_general import geometry as geo
from simple_equ.math_general import constants



@pytest.mark.parametrize("a,b,expected", [
    (3, 4, 5.0),
    (5, 12, 13.0),
    (0.0, 5.0, 5.0),
    (1.5, 2.5, math.hypot(1.5, 2.5)),
])
def test_pythagoras(a, b, expected):
    assert geo.pythagoras(a, b) == pytest.approx(expected, rel=1e-9)

def test_pythagoras_negative():
    # Negatives ok since squared
    assert geo.pythagoras(-3, 4) == pytest.approx(5.0)

@pytest.mark.parametrize("a,expected", [
    (4, 16.0),
    (0, 0.0),
    (2.5, 6.25),
])
def test_square_area(a, expected):
    assert geo.square_area(a) == expected

@pytest.mark.parametrize("a,expected", [
    (2, 8.0),
    (0, 0.0),
])
def test_cube_area(a, expected):
    assert geo.cube_area(a) == expected

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6.0),
    (0, 5, 0.0),
])
def test_rectangle_area(a, b, expected):
    assert geo.rectangle_area(a, b) == expected

@pytest.mark.parametrize("radius,expected", [
    (1, constants.pi),
    (0, 0.0),
    (5, 25 * constants.pi),
])
def test_circle_area(radius, expected):
    assert geo.circle_area(radius) == expected

@pytest.mark.parametrize("b1,b2,h,expected", [
    (2, 4, 3, 9.0),
    (0, 0, 5, 0.0),
])
def test_trapezoid_area(b1, b2, h, expected):
    assert geo.trapezoid_area(b1, b2, h) == expected

@pytest.mark.parametrize("base,h,expected", [
    (4, 5, 10.0),
    (0, 10, 0.0),
])
def test_triangle_area(base, h, expected):
    assert geo.triangle_area(base, h) == expected

@pytest.mark.parametrize("l,w,h,expected", [
    (1, 1, 1, pytest.approx(3.236, rel=1e-3)),
])
def test_pyramid_surface(l, w, h, expected):
    assert geo.pyramid_surface(l, w, h) == expected

@pytest.mark.parametrize("h,l,w,expected", [
    (3, 3, 3, 9.0),
    (0, 5, 5, 0.0),
])
def test_pyramid_volume(h, l, w, expected):
    assert geo.pyramid_volume(h, l, w) == expected

@pytest.mark.parametrize("d,expected", [
    (10, 5.0),
    (0, 0.0),
])
def test_calculate_radius(d, expected):
    assert geo.calculate_radius(d) == expected

@pytest.mark.parametrize("r,expected", [
    (1, 2 * constants.pi),
    (0, 0.0),
])
def test_circumference(r, expected):
    assert geo.circumference(r) == expected

@pytest.mark.parametrize("p1,p2,expected", [
    ((0,0), (3,4), 5.0),
    ([1.0,1.0], [4.0,5.0], 5.0),
    ((0,0,0), (3,4,0), 5.0),
    ((0,0,0), (1,1,1), math.sqrt(3)),
])
def test_distance(p1, p2, expected):
    assert geo.distance(p1, p2) == pytest.approx(expected, rel=1e-9)

def test_distance_invalid_type():
    with pytest.raises(ValueError):
        geo.distance([1,2], "invalid")

def test_distance_invalid_dim():
    with pytest.raises(ValueError):
        geo.distance((1,2,3,4), (1,2,3,4))

@pytest.mark.parametrize("angle_deg,expected", [
    (0, pytest.approx(0.0, rel=1e-2)),
    (30, pytest.approx(0.5, rel=1e-2)),
])
def test_sin(angle_deg, expected):
    assert geo.sin(angle_deg) == expected

@pytest.mark.parametrize("angle_deg,expected", [
    (0, pytest.approx(1.0, rel=1e-2)),
    (60, pytest.approx(0.5, rel=1e-2)),
])
def test_cosin(angle_deg, expected):
    assert geo.cosin(angle_deg) == expected

@pytest.mark.parametrize("angle_deg,expected", [
    (45, pytest.approx(1.0, rel=1e-2)),
    (0, pytest.approx(0.0, rel=1e-2)),
])
def test_tan(angle_deg, expected):
    assert geo.tan(angle_deg) == expected

def test_tan_90():
    with pytest.raises(ZeroDivisionError):
        geo.tan(90)

@pytest.mark.parametrize("r,expected", [
    (1, 4 * constants.pi),
    (0, 0.0),
])
def test_sphere_surface(r, expected):
    assert geo.sphere_surface(r) == expected

@pytest.mark.parametrize("p1,p2,expected", [
    ((0,0), (3,4), 4/3),
])
def test_slope(p1, p2, expected):
    assert geo.slope(p1, p2) == expected

def test_slope_vertical():
    with pytest.raises(ZeroDivisionError):
        geo.slope((1,1), (1,5))

def test_slope_invalid_dim():
    with pytest.raises(ValueError):
        geo.slope((1,2,3), (4,5,6))
