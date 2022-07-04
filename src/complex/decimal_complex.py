from __future__ import annotations

__author__ = "Tomasz Rybotycki"

"""
    The aim of this script is to provide an arbitrary precision complex number
    implementation. We will use Decimal to achieve that.
    
    TODO TR:    There might be problem with this implementation, as it is based on
                decimal. I imagine 
    
"""

from decimal import Decimal


class DecimalComplex:
    """
    An implementation of arbitrary precision complex number based on Decimal.
    """

    def __init__(self, real: Decimal = 0, imaginary: Decimal = 0) -> None:
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other: DecimalComplex) -> DecimalComplex:
        return DecimalComplex(
            self.real + other.real,
            self.imaginary + other.imaginary
        )

    def __mul__(self, other: DecimalComplex) -> DecimalComplex:
        return DecimalComplex(
            self.real * other.real - self.imaginary * other.imaginary,
            self.real * other.imaginary + self.imaginary * other.real
        )

    def __neg__(self) -> DecimalComplex:
        return DecimalComplex(-self.real, - self.imaginary)

    def __str__(self) -> str:
        return f"{self.real}{' + ' if self.imaginary > 0 else ' - '}{abs(self.imaginary)}i"
