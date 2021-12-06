def solution(s):
    l = s.count("<")
    salutes = 0
    for char in s:
        if char == ">":
            salutes += l
        elif char == "<":
            if l == 0: break
            l -= 1
    return salutes * 2

if __name__ == "__main__":
    print(solution("<<>><"))