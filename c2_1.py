def solution(xs):
    pos = []
    neg = []
    zero = False
    for num in xs:
        if num == 0:
            zero = True
        elif num > 0:
            pos.append(num)
        else:
            neg.append(num)

    if len(pos) == 0 and len(neg) == 0:
        # if there are only zeroes in the list return zero
        return "0"
    elif len(pos) == 0 and len(neg) == 1:
        # edge case, list containing zeroes except one negative value
        if zero: return "0"
        else: return str(neg[0])
    else:
        prod = 1
        for num in pos: prod *= num
        for num in neg: prod *= num
        if prod > 0:
            return str(prod)
        else:
            return str(prod // max(neg))

if __name__ == "__main__":
    print(solution([-2, -3, 4, -5]))