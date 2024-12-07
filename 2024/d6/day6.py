# Open the file and read the content
with open('input.txt') as file:
    content = file.read()

# Parse the equations into a list of lists
equs = [
    [int(eq.split(': ')[0])] + [int(i) for i in eq.split(': ')[1].split(' ')]
    for eq in content.split('\n') if eq.strip()
]

# Function to evaluate an equation with potential operator combinations
def evaluate(equation):
    test_value = equation[0]
    numbers = equation[1:]
    t = len(numbers)

    # Total possible operator combinations (2^(t-1) for (t-1) positions)
    total_combinations = 2**(t-1)
    
    # Try all operator combinations (0 for addition, 1 for multiplication)
    for op_comb in range(total_combinations):
        result = numbers[0]
        for i in range(t-1):
            # Check if the i-th bit of op_comb is 1 (multiplication) or 0 (addition)
            if (op_comb >> i) & 1:
                result *= numbers[i+1]
            else:
                result += numbers[i+1]
        
        # If the result matches the test value, return the result
        if result == test_value:
            return test_value

    # If no valid result, return 0
    return 0

valid_eqs = []  # To store valid equations (those that evaluate to non-zero)
somme = 0

# Process each equation: Evaluate, filter, and accumulate results
for eq in equs:
    result = evaluate(eq)
    if result != 0:
        somme += result
    else:
        valid_eqs.append(eq)

# Output the result
print(f"Part 1: {somme}")


import itertools

# Function to evaluate an expression with different operators
def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(1, len(numbers)):
        if operators[i-1] == 0:
            result += numbers[i]
        elif operators[i-1] == 1:
            result *= numbers[i]
        elif operators[i-1] == 2:
            # Concatenation: Convert both numbers to string, concatenate, then convert back to integer
            result = int(str(result) + str(numbers[i]))
    return result

# Function to process equations and find valid ones
def process_equations(equations):
    total_sum = 0
    
    for equation in equations:
        # Split the equation into test value and numbers
        test_value, numbers = equation[0], equation[1:]
        num_count = len(numbers)
        
        # Generate all possible combinations of the three operators: '+', '*', '||'
        operator_combinations = itertools.product([0, 1, 2], repeat=num_count - 1)
        
        # Check each combination of operators
        for operators in operator_combinations:
            if evaluate_expression(numbers, operators) == test_value:
                total_sum += test_value
                break  # No need to check further operators once we find a valid match
    
    return total_sum


result = process_equations(valid_eqs)
print(f"Part 2 - preprocess: {result}")
print(f"Part 2: {result+somme}")







