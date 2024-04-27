def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(start, end):
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes

def main():
    start = 10
    end = 30
    prime_numbers = generate_primes(start, end)
    print("Prime numbers between", start, "and", end, ":", prime_numbers)

if __name__ == "__main__":
    main()
