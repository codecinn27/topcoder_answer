# Read input and convert to sets
set1 = set(map(int, input().strip().split(',')))
set2 = set(map(int, input().strip().split(',')))

# Check if sets are equal
if set1 == set2:
    print('invalid set')
else:
    # Calculate symmetric difference and sort
    sym_diff = sorted(set1.symmetric_difference(set2))
    # Format output with curly braces and commas
    output = '{' + ', '.join(map(str, sym_diff)) + '}'
    print(output)