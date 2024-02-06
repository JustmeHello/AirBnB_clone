# Import necessary modules
import math
import random


def calculate_hypotenuse(a, b):
    """Calculate the length of the hypotenuse of a right triangle."""
    return math.sqrt(a**2 + b**2)


def generate_random_numbers(n):
    """Generate a list of n random numbers."""
    return [random.randint(1, 100) for _ in range(n)]


def main():
    """Main function to demonstrate the usage of the other functions."""
    # Generate random numbers
    random_numbers = generate_random_numbers(5)

    # Print the generated random numbers
    print("Generated random numbers:", random_numbers)

    # Calculate the hypotenuse of a right triangle with sides 3 and 4
    hypotenuse = calculate_hypotenuse(3, 4)

    # Print the calculated hypotenuse
    print("Hypotenuse of a right triangle with sides 3 and 4:", hypotenuse)


if __name__ == "__main__":
    main()
