class Dog():
    #속성
    age = 0
    name = ""
    weight = 0
    #메서드
    def bark(self):
        print("%s -> 멍멍" % self.name)

myDog = Dog()
myDog.name = "Merry"
myDog.weight = 20
myDog.age = 3
myDog.bark()

yourDog = Dog()
yourDog.name = "Happy"
yourDog.weight = 30
yourDog.age = 5
yourDog.bark()