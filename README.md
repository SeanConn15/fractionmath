# Fraction addition program

## Running Instructions
Run `python main.py`
Type "stop" to stop running the interpreter

## Running tests
Run `pyhton -m unittest` in the main directory.

## known issues
Negative numbers do not work correctly. I realized as I was writing the code that they were not asked for. There is ambigurity in the parsing that I naively worked out between something like 1_-1/2 and -1_1/2. I could handle this but ran out of time. For all positive operands, the code is correct however.
