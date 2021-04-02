number_to_word = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
                  5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
successive_word = {2: "double", 3: "triple", 4: "quadruple", 5: "quintuple",
                   6: "sextuple", 7: "septuple", 8: "octuple", 9: "nonuple",
                   10: "decuple"}

T = int(input())
for x in range(1, T + 1):
    N, F = input().split()
    numbers = list(map(int, N))
    y = []
    for divider in map(int, F.split('-')):
        division = numbers[:divider]
        previous = division.pop(0)
        count = 1
        for number in division + [-1]:
            if number == previous:
                count += 1
                continue
            if count == 1 or count > 10:
                y.extend([number_to_word[previous]] * count)
            else:
                y.append(successive_word[count])
                y.append(number_to_word[previous])
            previous = number
            count = 1
        numbers = numbers[divider:]
    y = ' '.join(y)
    print(f"Case #{x}: {y}", flush=True)
