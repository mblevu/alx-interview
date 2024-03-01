# Making change

## problem

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total

## approach

1. **Check if the total is less than or equal to 0**: If the total is less than or equal to 0, we return 0. This is because we don't need any coins to make change for a total of 0 or less.

```python
if total <= 0:
    return 0
```

2. **Sort the coins in descending order**: We sort the coins in descending order so that we can start making change with the highest denomination. This helps in minimizing the number of coins used.

```python
coins.sort(reverse=True)
```

3. **Initialize a counter for the number of coins**: We initialize a counter, `num_coins`, to keep track of the number of coins used.

```python
num_coins = 0
```

4. **Iterate over the coins**: For each coin, we keep subtracting its value from the total and incrementing the counter until the total is less than the coin's value.

```python
for coin in coins:
    while total >= coin:
        total -= coin
        num_coins += 1
```

5. **Check if change can be made**: If after going through all the coins, the total is not 0, it means change cannot be made for the given total with the provided coin denominations. In this case, we return -1.

```python
if total != 0:
    return -1
```

6. **Return the number of coins**: If change can be made, we return the number of coins used.

```python
return num_coins
```

This approach works well for most cases. However, it may not always return the optimal solution if the coin denominations are not standard. For example, if the coin denominations are [1, 3, 4] and the total is 6, the optimal solution is two 3-coin pieces, but this approach will return one 4-coin piece and two 1-coin pieces. For such cases, a dynamic programming approach would be more suitable.