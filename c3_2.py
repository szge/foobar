def solution(n):
    sum = 0
    for h in range(1, n):
        sum += solve(h, n)
    return sum

# h: height
# b: number of bricks
# returns: number of ways to create a staircase of height h from b bricks
memo = {}
def solve(h, b):
    if b > h * (h + 1) / 2: return 0
    if b < h: return 0
    if b == h: return 1
    if (h, b) in memo: return memo[(h, b)]
    sum = 0
    for h1 in range(1, h):
        sum += solve(h1, b - h)
    memo[(h, b)] = sum
    return(sum)

if __name__ == "__main__":
    print(solution(200))
    # print(memo)