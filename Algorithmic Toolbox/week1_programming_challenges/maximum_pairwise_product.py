# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    index = 0
    total = len(numbers)
    for i in range(1, total):
        if(numbers[i] > numbers[index]):
            index = i

    numbers[index], numbers[total-1] = numbers[total-1], numbers[index]

    index = 0
    for i in range(1, total - 1):
        if(numbers[i] > numbers[index]):
            index = i

    numbers[index], numbers[total-2] = numbers[total-2], numbers[index]
    return numbers[total - 2] * numbers[total - 1]


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
