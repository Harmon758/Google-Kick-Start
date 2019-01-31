numbers = {0: [True, True, True, True, True, True, False],
           1: [False, True, True, False, False, False, False],
           2: [True, True, False, True, True, False, True],
           3: [True, True, True, True, False, False, True],
           4: [False, True, True, False, False, True, True],
           5: [True, False, True, True, False, True, True],
           6: [True, False, True, True, True, True, True],
           7: [True, True, True, False, False, False, False],
           8: [True, True, True, True, True, True, True],
           9: [True, True, True, True, False, True, True]}

T = int(input())
for x in range(1, T + 1):
    states = input().split()
    N = int(states.pop(0))
    possible = {number: [None] * 7 for number in range(10)}
    for n, state in enumerate(states):
        for number, segments in possible.copy().items():
            current_possible = (number - n) % 10
            for segment, value in enumerate(map(int, state)):
                if value:
                    if (not numbers[current_possible][segment]
                            or segments[segment] == False):
                        del possible[number]
                        break
                    else:
                        possible[number][segment] = True
                elif numbers[current_possible][segment]:
                    if segments[segment]:
                        del possible[number]
                        break
                    else:
                        possible[number][segment] = False
    y = ""
    for number, segments in possible.items():
        number = (number - N) % 10
        state = ""
        for segment in range(7):
            if numbers[number][segment] and segments[segment] is None:
                state = "ERROR!"
                break
            state += str(int(numbers[number][segment] and segments[segment]))
        if not y:
            y = state
        if state == "ERROR!" or y != state:
            y = "ERROR!"
            break
    if not y:
        y = "ERROR!"
    print(f"Case #{x}: {y}")
