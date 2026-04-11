from setuptools import setup, Extension

extensions = [
    Extension(
        "geometry.trigonometry",
        sources=["simple_equ/geometry/trigonometry.c"],
    )
]

setup(
    package_dir={"": "simple_equ"},
    ext_modules=extensions,
)