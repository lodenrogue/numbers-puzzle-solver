import itertools
import sys

def evaluate_expression(expression):
    # Evaluate the expression and return the result
    try:
        return eval(expression)
    except (SyntaxError, ZeroDivisionError):
        return None

def find_closest_expression(numbers, goal):
    closest_value = float('inf')
    closest_expression = ""

    # Generate all possible permutations of numbers
    for permutation in itertools.permutations(numbers):
        # Generate all possible combinations of operations
        operators = itertools.product("+-*/", repeat=len(numbers) - 1)

        for ops in operators:
            expression = ""
            
            for i in range(len(numbers) - 1):
                expression += str(permutation[i]) + ops[i]
            expression += str(permutation[-1])

            result = evaluate_expression(expression)
            
            if result is not None and abs(result - goal) < abs(closest_value - goal):
                closest_value = result
                closest_expression = expression

    return closest_expression


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python numbers.py <numbers> <goal>")
        sys.exit(1)

    # Retrieve command-line arguments
    numbers_str = sys.argv[1]
    goal_str = sys.argv[2]

    # Check if both numbers and goal are provided
    if not numbers_str or not goal_str:
        print("Please provide both numbers and goal.")
        sys.exit(1)

    # Convert the string of numbers into a list of integers
    numbers = list(map(int, numbers_str.split()))

    # Convert the goal value to float
    try:
        goal = float(goal_str)
    except ValueError:
        print("Invalid goal value. Please provide a valid numeric value.")
        sys.exit(1)

    # Find the closest expression
    closest_expression = find_closest_expression(numbers, goal)

    # Display the result
    print(closest_expression)
