# PyCalc

PyCalc is a versatile calculator library and command-line tool written in Python. It supports basic arithmetic operations and essential mathematical functions, making it a handy tool for quick calculations or a reusable library for your Python projects.

## Features

- **Basic Operators**: Addition (+), Subtraction (-), Multiplication (*), Division (/), Power (pow)
- **Mathematical Functions**: Square root (sqrt), Sine (sin), Cosine (cos), Tangent (tan), Arctangent (atan)
- **Command-Line Interface**: Perform calculations directly from your terminal
- **Library Integration**: Import PyCalc into your Python code for seamless computation

## Installation

```commandline
pip install git+https://github.com/awtb/pycalc
```

## Usage

### Using command-line interface

```bash
python -m pycalc --expression 2 + 2 / 4
```

Want a repl?
```bash
python -m pycalc
```

### Using programming interface
```python
from pycalc.calculator import calc

expression = "2 + 4 / 2"
result = calc(expression)

print(result)
```

