import math

# Positive integers only
digit_len = lambda k: int(math.log10(k))


def digit_to_list(given):
    ori_len = digit_len(given)
    acc = []
    for _ in reversed(range(ori_len + 1)):  # TODO Over flow !
        if given is 0:
            break

        curr_len = digit_len(given)
        d = 10 ** curr_len
        k = given // d
        given -= d * k
        acc.append(k)

        # prevent domain error
        if given is not 0:
            next_len = digit_len(given)
            len_cnt = curr_len - next_len
            while len_cnt > 1:
                acc.append(0)
                len_cnt -= 1

    while len(acc) <= ori_len:
        acc.append(0)
    return acc


def is_palindrome(dist):
    ori_len = len(dist)
    pivot = math.ceil(ori_len / 2) - 1
    acc, rcc = [], []

    for i, d in enumerate(dist):
        if i > pivot:
            rcc.append(d)
        else:
            acc.append(d)

    if ori_len % 2 != 0:
        acc.pop(int(pivot))

    return acc == list(reversed(rcc))


print(is_palindrome(digit_to_list(int(input()))))
