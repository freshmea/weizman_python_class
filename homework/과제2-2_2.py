""" 이번주 과제입니다.

리스트를 하나 받는 함수가 있습니다.
받은 리스트의 첫 번째 객체를 맨 뒤로 옮기는 함수를 완성 하세요.
리스트가 없다면 없는 리스트를 리턴하세요.
함수가 제대로 작동하면 완성 이라는 문자가 출력 됩니다.
    """


from typing import Iterable


def replace_first(items: list) -> Iterable:
    # 여기에 코드를 쓰세요



if __name__ == '__main__':
    print("예시:")
    print(list(replace_first([1, 2, 3, 4])))

    #함수가 완성 되었는지 체크하는 코드
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("성공!!! 수고했습니다.완성!")
