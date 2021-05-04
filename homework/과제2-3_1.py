"""between_markers 라는 함수는 스트링객체 하나와 한개로된 스트링 객체 두개를 입력 받는다. text 라는
스트링에서 첫 번째 문자를 찾고 두번째 문자를 찾아서 그 안쪽의 내용만 리턴을 하세요. """


def between_markers(text: str, begin: str, end: str) -> str:
    # 여기에 코드를 쓰세요.
    return 


if __name__ == '__main__':
    print('예시:')
    print(between_markers('What is >apple<', '>', '<'))

    #  함수가 완성 되었는지 체크하는 코드
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('성공!!! 수고했습니다.완성!')

