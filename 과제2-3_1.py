"""between_markers 라는 함수는 스트링객체 하나와 한개로된 스트링 객체 두개를 입력 받는다. text 라는
스트링에서 첫 번째 문자를 찾고 두번째 문자를 찾아서 그 안쪽의 내용만 리턴을 하세요. """


def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    return


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')

