class Transactions():
    #속성
    price = 0.0
    credit_card = 0
    item = 0
    #메서드
    def save(self, cost, card, itm):
        self.price = cost
        self.credit_card = card
        self.item = itm
        self.save_file()
    #속성값 외부파일 저장
    def save_file(self):
        file = open("transaction.txt","a")
        file.write("%07d%16s%16s\n" % \
            (self.price*100, self.credit_card, self.item))
        file.close()

items = ["DONUT", "LATTE", "FILTER", "MUFFIN"]
prices = [1.50, 2.20, 1.80, 1.20]
running = True
while running:
    option = 1
    for choice in items:
        print(str(option) + ". " + choice)
        option = option + 1
    print(str(option) + ". Quit")
    choice = int(input("Choose an option: "))
    if choice == option:
        running = False
    else :
        card = input("Credit card number: ")
        trans = Transactions()
        trans.save(prices[choice-1], card, items[choice-1])