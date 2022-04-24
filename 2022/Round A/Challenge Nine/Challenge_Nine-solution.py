T = int(input())

for x in range(1, T + 1):

    N = int(input())

    digits = N
    sum_of_digits = 0
    index = 0
    last_index = {}
    while digits:
        digits, digit = divmod(digits, 10)
        sum_of_digits += digit
        index += 1
        last_index[digit] = index

    new_digit = sum_of_digits % 9
    if new_digit:
        new_digit = 9 - new_digit
        index = max(
            last_index.get(digit, 0)
            for digit in range(new_digit + 1, 10)
        )
    else:
        index -= 1

    power_of_10 = 10 ** index
    before, after = divmod(N, power_of_10)
    y = (
        before * power_of_10 * 10 +
        new_digit * power_of_10 +
        after
    )

    print(f"Case #{x}: {y}", flush = True)
