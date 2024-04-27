def generate_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

def main():
    start = 10
    end = 30
    prime_numbers = generate_primes(start, end)
    print("Prime numbers between", start, "and", end, ":", prime_numbers)

if __name__ == "__main__":
    main()
