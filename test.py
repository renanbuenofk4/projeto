def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

if __name__ == "__main__":
    n = 10
    fib_sequence = fibonacci(n)
    print(f"Fibonacci sequence up to the {n}th term:")
    print(fib_sequence)