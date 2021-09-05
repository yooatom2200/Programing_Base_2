class Gimbab():
    Danmuji = 0
    Ham = 0
    Danggun = 0
    Shigumchi = 0
    def __init__(self):
        self.Danmuji, self.Ham, self.Danggun, self.Shigumchi = input("각 재료의 개수를 입력해주세요(단무지, 햄, 당근, 시금치) : ").split()

    def order(self):
        order_file = open("order.txt", "w")
        order_file.write("주문기록 >> 단무지 : %d | 햄 : %d | 당근 : %d | 시금치 : %d")
        order_file.close()

class Cheese(Gimbab):
    Chs = 0
    def __init__(self):
        Gimbab.__init__(self)
        self.Chs = input("치즈는 몇장 넣을까요 ? : ")
    
