def solution(numbers):
    str_numbers = []
    for number in numbers:
        str_numbers.append(str(number)) # numbers = list(map(str, numbers))
    str_numbers.sort(key=lambda x: x * 5, reverse=True)
    return str(int("".join(str_numbers)))
