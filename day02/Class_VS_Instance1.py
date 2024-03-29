# 클래스 변수 - 인스턴스간 공유됨
class Dog:
    tricks = []  # 클래스 변수 선언 - 파이썬 만의 특징. 객체들 간의 공유할 데이터는 클래스 변수로

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)  # 클래스 변수에 값 추가


dog1 = Dog('마음이')
dog2 = Dog('진돌이')

dog1.add_trick('구르기')
dog2.add_trick('두발로 서기')
dog2.add_trick('죽은척 하기')

print(dog1.name, ':', dog1.tricks)
print(dog2.name, ':', dog2.tricks)

# 우리의 의도와는 다름