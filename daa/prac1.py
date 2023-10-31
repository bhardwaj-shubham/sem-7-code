def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def non_recursive_fibonacci(n):
    first = 0
    second = 1
    print(first)
    print(second)
    for i in range(n - 2, 0, -1):
        third = first + second
        first = second
        second = third
        print(third)


if __name__ == "__main__":
    n = int(input("Enter the number: "))

    print("\nRecursive Fibonacci: ")
    for i in range(n):
        print(recursive_fibonacci(i))

    print("\nNon-Recursive Fibonacci: ")
    non_recursive_fibonacci(n)
