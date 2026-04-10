import pytest
import math
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))
from simple_equ import algebra


@pytest.mark.parametrize(
    "base,exponent,expected",
    [
        (2, 3, 8.0),
        (2, 0, 1.0),
        (-2, 3, -8.0),
        (2, -1, 0.5),
        (0, 5, 0.0),
        (10, 2, 100.0),
        (2.5, 2, 6.25),
    ],
)
def test_power(base, exponent, expected):
    """[Summary]: Verify that power returns the base raised to the exponent.

    [Description]: Covers common cases including negative bases, negative
    exponents, and zero values to ensure robustness in standard scenarios.
    """
    assert algebra.power(base, exponent) == pytest.approx(expected, rel=1e-9)


@pytest.mark.parametrize(
    "number,expected",
    [
        (0, 1),
        (1, 1),
        (5, 120),
        (10, 3628800),
    ],
)
def test_factorial_positive(number, expected):
    """[Summary]: Verify that factorial returns the correct value for positive integers."""
    assert algebra.factorial(number) == expected


def test_factorial_negative():
    """[Summary]: Verify that factorial handles negative integers by returning 1."""
    assert algebra.factorial(-5) == 1


def test_factorial_float():
    """[Summary]: Verify that factorial correctly handles floating-point inputs."""
    assert algebra.factorial(3.0) == 6


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (48, 18, 6),
        (7, 5, 1),
        (0, 5, 5),
        (15, 0, 15),
        (-48, 18, 6),
        (48.0, 18, 6.0),
    ],
)
def test_gcd(a, b, expected):
    """[Summary]: Verify that gcd returns the greatest common divisor."""
    assert algebra.gcd(a, b) == expected


@pytest.mark.parametrize(
    "number,expected",
    [
        (0, 0.0),
        (1, 1.0),
        (25, 5.0),
        (2, pytest.approx(math.sqrt(2), rel=1e-9)),
    ],
)
def test_sqrt_positive(number, expected):
    """[Summary]: Verify that sqrt returns the square root for non-negative numbers."""
    assert algebra.sqrt(number) == expected


def test_sqrt_negative():
    """[Summary]: Verify that sqrt raises ValueError for negative inputs."""
    with pytest.raises(ValueError, match="Not a real number"):
        algebra.sqrt(-1)


@pytest.mark.parametrize(
    "x,expected",
    [
        (0, 0.0),
        (8, 2.0),
        (27, 3.0),
        (-8, -2.0),
        (1.0, 1.0),
    ],
)
def test_cbrt(x, expected):
    """[Summary]: Verify that cbrt returns the real cube root."""
    assert algebra.cbrt(x) == pytest.approx(expected, rel=1e-9)


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (1, -3, 2, (1.0, 2.0)),
        (1, 0, -1, (-1.0, 1.0)),
        (1, 2, 1, (-1.0, -1.0)),
    ],
)
def test_basic_quadratic(a, b, c, expected):
    """[Summary]: Verify that basic_quadratic returns real roots for common inputs."""
    root1, root2 = algebra.basic_quadratic(a, b, c)
    assert sorted([root1, root2]) == sorted(expected)


def test_basic_quadratic_zero_a():
    """[Summary]: Verify that basic_quadratic raises ZeroDivisionError when a is zero."""
    with pytest.raises(ZeroDivisionError):
        algebra.basic_quadratic(0, 1, 1)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, -8, 4.0),
        (1, 0, 0.0),
        (1, -3, 3.0),
    ],
)
def test_basic_linear(a, b, expected):
    """[Summary]: Verify that basic_linear returns the correct solution."""
    assert algebra.basic_linear(a, b) == expected


def test_basic_linear_zero_a():
    """[Summary]: Verify that basic_linear raises ZeroDivisionError when a is zero."""
    with pytest.raises(ZeroDivisionError):
        algebra.basic_linear(0, 1)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 5, True),
        (10, 3, False),
        (0, 5, True),
        (7, 1, True),
        (-10, 5, True),
        (10.0, 5, True),
    ],
)
def test_is_divisible(a, b, expected):
    """[Summary]: Verify that is_divisible correctly identifies divisibility."""
    assert algebra.is_divisible(a, b) == expected


def test_is_divisible_zero_divisor():
    """[Summary]: Verify that is_divisible raises ValueError when the divisor is zero."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        algebra.is_divisible(10, 0)
