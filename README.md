# sumfind
# A Sum Combinations Finder

This script helps you find all unique combinations of numbers that add up to a specific target sum.
/nPrompted by Lester Tax, Inc.
v0.23.11.08

## Requirements

To run this script, you need to have Python installed on your Windows 10/11 machine. You can download Python from the official website: https://www.python.org/downloads/windows/

## Usage

To use the script, follow these steps:

1. Download the `sumfind.py` script to your local machine.
2. Open Command Prompt or PowerShell.
3. Navigate to the directory where you downloaded the script.
4. Run the script using the following command:

```bash
python sumfind.py <target_sum> <number1> <number2> <number3> ... <numberN>
```

Replace `<target_sum>` with the target sum you are looking for and `<number1> <number2> <number3> ... <numberN>` with the list of numbers you want to find combinations for.

For example:

```bash
python sumfind.py 559.21 28.18 36.96 203.66 59.99 9.47 ...
```

If Python is not recognized as a command, try using the Python launcher for Windows:

```bash
py sumfind.py <target_sum> <number1> <number2> <number3> ... <numberN>
```

## Output

The script will print all unique combinations of the provided numbers that sum up to the target sum. If no combination is found, it will print "No combinations found that sum to the target."

## Note

Due to the nature of floating-point arithmetic, the script uses rounding to ensure the accuracy of the sum calculations. This means the script may not find combinations that are extremely close to the target sum but not exactly equal due to floating-point precision issues.

## License

This script is provided "as is", without warranty of any kind, express or implied. Use at your own risk.

