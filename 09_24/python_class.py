"""
1. class 의 개념
    특정한 기능(멤버함수)과 속성(멤버변수) 가진 어떤 것들은 모두 class 로 정의될 수 있음.
        ex) 사람, 자동차, 컴퓨터 등
    예전에는 현실 세계에 존재 하는 것을 개념으로 삼았지만 현재는 의미가 바뀌어 모든 것들에 적용되고 있음.

2. class 의 구성
    1) class 키워드
    2) class 명
    3) 멤버 함수 ( init 함수도 포함)
    4) 멤버 변수 ( init 함수에 입려 되어 class 내부에 세팅되는 속성 값)

3. class 구현
    class Person:
        def __init__(self, name, age, phone_number):
            self.name = name
            self.age = age
            self.phone_number = phone_number

        def increase_age(self):
            self.age += 1

        def change_phone_number(self, new_number):
            self.phone_number = new_number

        @classmethod
        def test_class_method(cls):


    if __name__ == "__main__":      # 이 파일이 main 일 때만 아래의 코드를 실행

        person = Person("김영현", 30, "010-5549-7248")     # init 함수에 순서를 지켜서 입력
        person = Person(name="김영현", phone_number="010-5549-7248", age=30) # 직접 지정하는 경우 순서가 달라도 됨.

        print(f"바뀌기 전 나이: {person.age}")    # 문자열 포맷팅
        person.increase_age()
        print("바뀐 후 나이: {}".format(person.age))     # 문자열 포맷팅

        print("바뀌기 전 폰번호: ", person.phone_number)
        person.change_phone_number("010-1234-5678")     # 함수 호출, new_number 입력
        print("{0} {1}".format("바뀐 후 폰번호: ", person.phone_number)       # 문자열 포맷팅

        Person.test_class_method()  # Person().test_class_method 처럼 객체가 메모리 할당 되지 않아도 호출 가능.
"""