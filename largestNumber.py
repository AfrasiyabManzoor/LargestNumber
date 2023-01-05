
def solution(numbers):
    if(len(numbers) == 0):
        return 0
    max = numbers[0];
    for n in numbers:
        if n > max:
            max = n
    return max
