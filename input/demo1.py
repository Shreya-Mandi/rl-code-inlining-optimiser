def calculate_fibonacci(n):
    if n <= 1:
        return n
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

def generate_fibonacci_sequence(length):
    sequence = [calculate_fibonacci(i) for i in range(length)]
    return sequence

def main():
    length = 10
    fibonacci_sequence = generate_fibonacci_sequence(length)
    print("Fibonacci sequence:", fibonacci_sequence)

if __name__ == "__main__":
    main()
