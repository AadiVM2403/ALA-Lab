import random
import math
import sys
from typing import Self


"""
A custom vector class implementation for educational purposes.
"""


class Vec:
    def __init__(self, src=None) -> Self:
        if src is None:
            self.elements = ()
        else:
            elements = tuple(src)

            for x in elements:
                if not isinstance(x, (int, float)):
                    raise TypeError(
                        f"Scalar must be a number: {type(x)}"
                    )

            self.elements = elements

    def __add__(self, t: Self) -> Self:
        if not isinstance(t, Vec):
            raise TypeError(f"Expected Vec: {type(t)}")

        if len(self.elements) != len(t):
            raise TypeError(
                "Type error - vectors must be of same dimensions"
            )

        return Vec(
            tuple(
                round(x + y, 5)
                for x, y in zip(self.elements, t.elements)
            )
        )

    def __rmul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(
                f"Vector multiplication with invalid type: {type(scalar)}"
            )

        return Vec(
            tuple(
                round(x * scalar, 5)
                for x in self.elements
            )
        )

    def __imul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(
                f"Vector multiplication with invalid type: {type(scalar)}"
            )

        # Tuples are immutable, so create a new tuple
        self.elements = tuple(
            round(x * scalar, 5)
            for x in self.elements
        )

        return self

    def __repr__(self) -> str:
        return repr(self.elements)

    def __len__(self) -> int:
        return len(self.elements)

    def __sub__(self, t: Self) -> Self:
        if not isinstance(t, Vec):
            raise TypeError(f"Expected Vec: {type(t)}")

        if len(self.elements) != len(t):
            raise TypeError(
                "Type error - vectors must be of same dimensions"
            )

        return Vec(
            tuple(
                round(x - y, 5)
                for x, y in zip(self.elements, t.elements)
            )
        )

    def __neg__(self) -> Self:
        return Vec(
            tuple(-x for x in self.elements)
        )

    def __radd__(self, other) -> Self:
        if other == 0:
            return self

        if not isinstance(other, Vec):
            raise TypeError(
                f"Unsupported operand type(s) for +: "
                f"'{type(other).__name__}' and 'Vec'."
            )

        return self + other

    def __iadd__(self, other) -> Self:
        if not isinstance(other, Vec):
            raise TypeError(
                f"Unsupported operand type(s) for +=: "
                f"'Vec' and '{type(other).__name__}'."
            )

        if len(self) != len(other):
            raise ValueError(
                f"Cannot in-place add vectors of mismatched dimensions: "
                f"{len(self)} and {len(other)}."
            )

        # Create a new tuple
        self.elements = tuple(
            round(a + b, 5)
            for a, b in zip(self.elements, other.elements)
        )

        return self

    @staticmethod
    def zeros(n: int) -> "Vec":
        if n <= 0:
            raise ValueError(
                f"Precondition failed: n must be > 0, got {n}."
            )

        return Vec((0.0,) * n)

    @staticmethod
    def ones(n: int) -> "Vec":
        if n <= 0:
            raise ValueError(
                f"Precondition failed: n must be > 0, got {n}."
            )

        return Vec((1.0,) * n)

    @staticmethod
    def uniform(n: int) -> "Vec":
        if n <= 0:
            raise ValueError(
                f"Precondition failed: n must be > 0, got {n}."
            )

        return Vec(
            tuple(random.random() for _ in range(n))
        )

    # Calculates the Euclidean norm (L2 norm)
    # sqrt(e[0]^2 + e[1]^2 + ... + e[n-1]^2)
    def norm(self) -> float:
        if not hasattr(self, "elements") or not self.elements:
            raise ValueError(
                "Cannot calculate norm of an empty or uninitialized vector."
            )

        return math.sqrt(
            sum(x ** 2 for x in self.elements)
        )



"""
(1) Understand the basic design of the vector abstraction. Review the implementation.
(2) Document each function.
(3) Implement all unimplemented methods.
(4) Create appropriate tests for this implementation, increasing the confidence about its correctness.
(5) Test this implementation by importing the class in a sepatate python script.

(6) Measure the performance of each of these functions on vectors of varying lengths.
    Try 2k to 64k dimension vectors and time the results.
    How would you do the measurements?
(7) Measure the performance on your machine. Check it on colab.

(8) use numpy and compare the performance.
"""


if sys.version_info < (3, 8):
    sys.exit("Error: This script requires Python 3.8 or higher.")

if __name__ == "__main__":
    #z1 = Vec.zeros(10)
    v1 = Vec([0, 1, 1.03])
    print(v1)
    v3 = 2.2 * v1
    v3 *= 5
    v3 = 1 + v3
    print(v3)
    v2 = v1 + v3
    print(v1 + v3)
    print(v2 - v3)
    print(-(v1 + v3))
    print(Vec.zeros(5))
    print(Vec.ones(4))
    print(Vec.uniform(3))
    print(v1.norm())