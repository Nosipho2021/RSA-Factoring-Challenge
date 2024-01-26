import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollards_rho(n):
    if n % 2 == 0:
        return 2, n // 2

    x = 2
    y = 2
    d = 1

    f = lambda x: (x**2 + 1) % n

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)

    return d, n // d

def factorize_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            num = int(line.strip())
            p, q = pollards_rho(num)
            print(f"{num}={p}*{q}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    factorize_file(file_path)

