def generate_fibonacci_sequence(length):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < length:
        next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fib)
    return fibonacci_sequence[:length]

def main():
    length = 10
    fibonacci_sequence = generate_fibonacci_sequence(length)
    print("Fibonacci sequence:", fibonacci_sequence)

if __name__ == "__main__":
    main()