import pytest
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))
from simple_equ import algebra


# ==============================================================================
# tests for simple_equ.algebra.cmath module
# ==============================================================================

@pytest.mark.parametrize(
    "real,imag,expected",
    [
        (3, 4, (3, 4)),
        (1.5, -2, (1.5, -2)),
        (0, 0, (0, 0)),
    ],
)
def test_complex_num(real, imag, expected):
    """[Summary]: Verify that complex_num creates a complex tuple."""
    assert algebra.complex_num(real, imag) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ((1, 2), (3, 4), (4, 6)),
        ((1.5, -0.5), (0.5, 2.5), (2.0, 2.0)),
    ],
)
def test_add(a, b, expected):
    """[Summary]: Verify that add correctly sums two complex tuples."""
    assert algebra.add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ((5, 7), (2, 3), (3, 4)),
        ((1, 1), (1, 1), (0, 0)),
    ],
)
def test_sub(a, b, expected):
    """[Summary]: Verify that sub correctly subtracts two complex tuples."""
    assert algebra.sub(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ((1, 2), (3, 4), (-5, 10)),
        ((1, 1), (1, -1), (2, 0)),
    ],
)
def test_mul(a, b, expected):
    """[Summary]: Verify that mul correctly multiplies two complex tuples."""
    assert algebra.mul(a, b) == expected


@pytest.mark.parametrize(
    "a,expected",
    [
        ((3, 4), 5.0),
        ((0, 0), 0.0),
        ((1, 0), 1.0),
        ((0, 1), 1.0),
    ],
)
def test_magnitude(a, expected):
    """[Summary]: Verify that magnitude returns the Euclidean norm of a complex tuple."""
    assert algebra.magnitude(a) == pytest.approx(expected, rel=1e-9)


# ==============================================================================
# tests for cubic equations (basic_qubic from algebra module)
# ==============================================================================

@pytest.mark.parametrize(
    "a,b,c,d,expected",
    [
        (1, -6, 11, -6, [1.0, 2.0, 3.0]),
        (1, 0, 0, 0, [0.0, 0.0, 0.0]),
    ],
)
def test_basic_qubic_real(a, b, c, d, expected):
    """[Summary]: Verify that basic_qubic returns correct real roots."""
    roots = algebra.basic_qubic(a, b, c, d)
    # Extract real roots for comparison
    real_roots = sorted([r for r in roots if isinstance(r, (int, float))])
    assert real_roots == pytest.approx(expected, rel=1e-9)


def test_basic_qubic_complex():
    """[Summary]: Verify that basic_qubic returns complex roots when delta >= 0.

    [Description]: Tests an equation with one real and two complex roots.
    Equation: x^3 - 1 = 0 => roots: 1, -0.5 + 0.866j, -0.5 - 0.866j
    """
    roots = algebra.basic_qubic(1, 0, 0, -1)
    
    # Sort roots: real first, then complex by imaginary part
    def root_sort_key(r):
        if isinstance(r, (int, float)):
            return (0, r, 0)
        return (1, r.real, r.imag)
        
    sorted_roots = sorted(roots, key=root_sort_key)
    
    # 1 is the real root
    # -0.5 +/- sqrt(3)/2 j are complex roots
    assert sorted_roots[0] == pytest.approx(1.0, rel=1e-9)
    assert sorted_roots[1].real == pytest.approx(-0.5, rel=1e-9)
    assert abs(sorted_roots[1].imag) == pytest.approx(0.86602540378, rel=1e-9)
    assert sorted_roots[2].real == pytest.approx(-0.5, rel=1e-9)
    assert abs(sorted_roots[2].imag) == pytest.approx(0.86602540378, rel=1e-9)
    assert sorted_roots[1].imag == -sorted_roots[2].imag
