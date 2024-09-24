"""
1. 디버깅 순서 정리
    1) py 파일 왼쪽의 숫자에 마우스 올려서 원하는 break point 설정
    2) py 파일에서 마우스 오른쪽 키로 debug 실행.
    3) Fn + F8 (맥북) 을 누르면서 디버깅. 윈도우는 그냥 F8

2. Fn + F7, F8, F9
    1) F7
        함수 내부까지 들어갈 수 있음.

    2) F8
        함수 내부를 들어가지 않고 단순히 한줄 실행.

    3) F9
        그 다음 break point 가 실행되는 지점까지 건너뜀.


3. 실행 예제
    import random

    def random_value_between(a, b):     # a, b 사이의 랜덤 실수를 return
        random_val = random.uniform(a, b)       # 여기 break point 하고, Fn + F8
        return random_val


    if __name__ == "__main__":
        val_list = [1, 2, 3, 4, 5, 6]

        for i in range(len(val_list)-1):        # 여기 break 포인트. Fn + F8
            rand_val = random_value_between(val_list[i], val_list[i+1])     # 여기 break point Fn + F7 로 함수 들어감.
            print(rand_val)

"""