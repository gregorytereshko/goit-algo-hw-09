import timeit

def find_coins_greedy(amount, coins):
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result

def find_min_coins(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    result = {}
    i = amount
    while i > 0:
        for coin in coins:
            if i >= coin and dp[i] == dp[i - coin] + 1:
                result[coin] = result.get(coin, 0) + 1
                i -= coin
                break
    return result


coins = [50, 25, 10, 5, 2, 1]

print(f"Жадібний алгоритм: {timeit.timeit(lambda: find_coins_greedy(100, coins), number=10)}")
print(f"Динамічне програмування: {timeit.timeit(lambda: find_min_coins(100, coins), number=10)}")