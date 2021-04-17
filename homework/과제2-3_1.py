def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    start = -1
    end2 = -1
    for k, i in enumerate(text):
        if i == begin and start == -1:
            start = k
        if i == end and start != -1:
            end2 = k
    return text[start+1:end2]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')


def sum_numbers(text: str) -> int:
    # your codehere
    a = text.split()
    b = 0
    for i in a:
        if i.isdigit():
            b += int(i)

    return b


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
                       'painting by Danish artist Anna '
                       'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")


def checkio(array: list) -> int:
    """
        sums even-indexes elements and multiply at the last
    """
    re = 0
    for i in array[::2]:
        re += i
    if array == []:
        return 0
    return re * array[-1]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))

    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
