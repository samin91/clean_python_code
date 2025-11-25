"""
Calculate the area of a circle given its radius.
"""

from typing import Union as union
import math


def calculate_circle_area(a: union[int, float]) -> float:
    """
    Calculate the area of a circle given its radius.

    Parameters:
        radius (int | float): The radius of the circle. Must be positive.

    Returns:
        float: Area of the circle. Returns 0 if radius is non-positive.
    """
    pi = math.pi
    try:
        area = pow(float(a), 2) * pi
    except ValueError as exc:
        raise ValueError(
            f"Invalid input: {a} is not a valid radius.Radius must be a number."
        ) from exc

    return area


def main():
    """Main function to demonstrate circle area calculation."""
    radius = 10
    result = calculate_circle_area(radius)
    print("The area of the circle is", result)


if __name__ == "__main__":
    main()
