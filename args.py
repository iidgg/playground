# a cs50 watching the lecture while coding / 2023 week -6 python
import sys

if len(sys.argv) <= 1:
    print("Missing command-line argument")
    sys.exit(1)

for arg in sys.argv[1:]: # the [1:] makes the array start from index 1
    print(arg)

sys.exit(0)
