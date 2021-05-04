""" 이번주 과제입니다.

리스트와 숫자를 하나 입력 받는 함수가 있습니다.
리스트 안에서 입력 받는 숫자가 있으면 그 전까지의 객체를 모두 삭제하고 남은 리스트를
돌려주는 함수는 완성하세요.
함수가 제대로 작동하면 완성 이라는 문자가 출력 됩니다.
    """

from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    # 여기에 코드를 쓰세요
    return items


if __name__ == '__main__':
    print("예시:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

    #함수가 완성 되었는지 체크하는 코드
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    print("성공!!! 수고했습니다.완성!")