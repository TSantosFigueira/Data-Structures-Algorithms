# python3
import math

def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    min_coins = [0] + [math.inf] * money
    denominations = [1, 3, 4]

    for m in range(1, money + 1):
        for i in denominations:
            if m >= i:
                num_coins = min_coins[m - i] + 1
                if num_coins < min_coins[m]:
                    min_coins[m] = num_coins
    return min_coins[money]


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
