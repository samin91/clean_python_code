"""A simple module demonstrating basic mathematical operations"""

import math
import sys


def calculate_square_root(x: float, y: float) -> float:
    """Calculate the square root of the sum of squares of x and y."""
    return math.sqrt(float(x) ** 2 + float(y) ** 2)


def transform_positive_number(items: list[float]) -> list[float]:
    """Transform list of items: if an item is positive,
    double it; otherwise zero it.
    """
    out = [i * 2 if float(i) > 0 else 0 for i in items]
    return out


def main():
    """Main function to demonstrate the module functionality."""
    data = [1, -2, 3, -4, 5]
    transformed = transform_positive_number(data)
    hypot = calculate_square_root(3, 4)
    print("Result:", transformed)
    print("Hypot of (3,4):", hypot)

    if len(sys.argv) < 2:
        print("No argument provided!")
    else:
        value = sys.argv[1]
        print("Value is", value)


if __name__ == "__main__":
    main()
