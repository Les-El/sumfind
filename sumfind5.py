import time

import sys
from itertools import combinations

def find_combinations_to_target(numbers, target_sum):
    found_combinations = []
    for r in range(1, len(numbers) + 1):
        for combo in combinations(numbers, r):
            if round(sum(combo), 2) == target_sum:
                # Calculate the "total distance" for the combination
                distance = sum(numbers.index(x) for x in combo)
                found_combinations.append((combo, distance))
    # Sort the combinations by their total distance
    found_combinations.sort(key=lambda x: x[1])
    # Return only the combinations without distances
    return [combo for combo, distance in found_combinations]

def main():
    start_time = time.time()
    # The first command line argument is the target sum
    target_sum = float(sys.argv[1])
    
    # The rest of the arguments are the numbers to check
    numbers = list(map(float, sys.argv[2:]))
    
    # Find combinations
    combinations_found = find_combinations_to_target(numbers, target_sum)
    
    # Output the results
    if combinations_found:
        print("\nCombinations found that sum to the target:")
        for combo in combinations_found:
            print("Combination: ", "   ".join(map(str, combo)), " = ", round(sum(combo), 2))
    else:
        print("No combinations found that sum to the target.")

if __name__ == "__main__":
    main()
