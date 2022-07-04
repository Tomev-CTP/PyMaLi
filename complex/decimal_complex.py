from __future__ import annotations

__author__ = "Tomasz Rybotycki"

"""
    The aim of this script is to provide an arbitrary precision complex number
    implementation. We will use Decimal to achieve that.
    
    TODO TR:    There might be problem with this implementation, as it is based on
                decimal. I imagine this can lead to some problems if decimal.Decimal
                is also used elsewhere.
"""

from decimal import Decimal


class DecimalComplex:
    """
    An implementation of arbitrary precision complex number based on Decimal.
    """

    def __init__(self, real=0, imaginary=0) -> None:

        if isinstance(real, (int, float)):
            real = Decimal(real)

        if isinstance(imaginary, (int, float)):
            imaginary = Decimal(imaginary)

        self.real = real
        self.imaginary = imaginary

    def __add__(self, other) -> DecimalComplex:

        if isinstance(other, (int, float)):
            other = DecimalComplex(other, 0)

        if isinstance(other, complex):
            other = DecimalComplex(other.real, other.imag)

        try:
            result = DecimalComplex(
                self.real + other.real, self.imaginary + other.imaginary
            )
        except Exception:
            print(type(self.real))
            print(type(other))

        return result

    def __radd__(self, other) -> DecimalComplex:
        return self.__add__(other)

    def __mul__(self, other: DecimalComplex) -> DecimalComplex:

        if isinstance(other, (int, float)):
            other = DecimalComplex(other, 0)

        if isinstance(other, complex):
            other = DecimalComplex(other.real, other.imag)

        return DecimalComplex(
            self.real * other.real - self.imaginary * other.imaginary,
            self.real * other.imaginary + self.imaginary * other.real,
        )

    def __rmul__(self, other) -> DecimalComplex:
        return self.__mul__(other)

    def __neg__(self) -> DecimalComplex:
        return DecimalComplex(-self.real, -self.imaginary)

    def __str__(self) -> str:
        return (
            f"{self.real}{' + ' if self.imaginary > 0 else ' - '}{abs(self.imaginary)}i"
        )

    def __pow__(self, power) -> DecimalComplex:
        # TODO TR: This is proof of concept. Could be optimized.
        result = DecimalComplex(1)

        for _ in range(power):
            result *= self

        return result
