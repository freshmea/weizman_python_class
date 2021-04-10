""" 이번주 과제입니다.

끝자리가 0인지 확인하는 함수를 완성하세요.
만약 끝자리에 0이 두개 있다면 2를 리턴해야 합니다.
함수가 제대로 작동하면 완성 이라는 문자가 출력 됩니다.
    """

def end_zeros(num: int) -> int:
    # 여기에 코드를 작성하세요.
    return

if __name__=='__main__':
    print("예시:")
    print(end_zeros(0))

    assert end_zeros(0) ==1
    assert end_zeros(1) ==0
    assert end_zeros(10) ==1
    assert end_zeros(101) ==0
    assert end_zeros(245) ==0
    assert end_zeros(100100) ==2
    assert end_zeros(100021300) ==2
    print ("성공!!! 수고했습니다.")