def solution(start, length):
    cum = 0 # cumulative
    a = start
    for l in range(length, 0, -1):
        cum ^= f(a, a + l - 1)
        a += length
    return str(cum)

# returns the value of a^(a+1)^...^b
# works for a <= b, a >= 1
def f(a, b):
    return f_0(b) ^ f_0(a - 1)

# returns the value of 0^1^...^n
def f_0(n):
    r = n % 4
    if r == 0: return n
    if r == 1: return 1
    if r == 2: return n + 1
    if r == 3: return 0

if __name__ == "__main__":
    print(solution(17, 4))