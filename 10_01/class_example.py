class Animal:   # 부모 클래스
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("동물 소리")


class Dog(Animal):      # 자식 클래스
    def __init__(self, name):   # 생성자 호출, 이 예제에서는 생략가능.
        super().__init__(name=name)

    def speak(self):
        print("멍멍")


if __name__ == "__main__":
    dog = Dog("멍멍이")
    print(dog.name)
    dog.speak()