class Katsu_Element():
    Bread = 1
    Egg = 1
    def Print_Element(self):
        print("기본재료 | 빵 : %d | 계란 : %d" % (self.Bread, self.Egg))

class Don_Katsu(Katsu_Element):
    Meat = "돼지고기"
    def __init__(self):
        self.Print_Element()
        print("돈까스 생성! 고기 : %s" % self.Meat)
    
class Hire_Katsu(Don_Katsu):
    Part = "안심"
    def __init__(self):
        self.Print_Element()
        print("히레카츠 생성! 고기 : %s | 부위 : %s" % (self.Meat, self.Part))

class Rosu_Katsu(Don_Katsu):
    Part = "등심"
    def __init__(self):
        self.Print_Element()
        print("로스카츠 생성! 고기 : %s | 부위 : %s" % (self.Meat, self.Part))

class Chicken_Katsu(Katsu_Element):
    Meat = "닭고기"
    def __init__(self):
        self.Egg = 2
        self.Print_Element()
        print("치킨까스 생성! 고기 : %s" % self.Meat)

eat1 = Don_Katsu()
eat2 = Hire_Katsu()
eat3 = Rosu_Katsu()
eat4 = Chicken_Katsu()