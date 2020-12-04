def pickingNumbers(a):
    frequency = [0] * 100
    max_value = 0
    for number in a:
        frequency[number] += 1
    for i in range(1, 100):
        max_value = max(max_value, frequency[i] + frequency[i - 1])

    return max_value


    