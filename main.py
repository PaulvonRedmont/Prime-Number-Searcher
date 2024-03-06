import time

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes():
    count = 0
    prime_count = 0
    total_prime_count = 0
    start_time = time.time()
    while True:
        count += 1
        if is_prime(count):
            prime_count += 1
            total_prime_count += 1
            # Calculate the number of digits in the prime number
            num_digits = len(str(count))
            if total_prime_count % 50000 == 0:
                print(f"Found {total_prime_count} prime numbers")
            if prime_count == 50000:
                print(f"Prime number: {count}, Digits: {num_digits}")
                prime_count = 0
            if time.time() - start_time >= 5:
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Prime numbers found: {total_prime_count}, Primes per second: {prime_count / elapsed_time:.2f}")
                start_time = end_time
                prime_count = 0

if __name__ == "__main__":
    find_primes()
