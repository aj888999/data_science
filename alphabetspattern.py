def print_pattern():
    n = 14
    for i in range(n, 0, -2):
        spaces = " " * ((n - i) // 2)
        chars = "".join(chr(96 + j) for j in range(1, i // 2 + 1))
        print(spaces + chars)

print_pattern()