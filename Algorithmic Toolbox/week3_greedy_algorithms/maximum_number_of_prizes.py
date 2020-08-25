# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []
    k = n
    l = 1

    while k > 0:
        if k <= 2 * l:
            summands.append(k)
            k -= k
        else:
            summands.append(l)
            k -= l
        l += 1
    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
