class Transactions():
    #속성
    price = 0.0
    credit_card = 0
    item = 0
    #생성자
    def __init__(self, cost, card, itm):
        self.price = cost
        self.credit_card = card
        self.item = itm
    #메서드
    def save(self):
        file = open("transactions.txt","a")
        file.write("%07d%16s%16s\n" %\
             (self.price * 100, self.credit_card, self.item))
        file.close()

#자식클래스
class Discount_trans(Transactions):
    #생성자
    def __init__(self, cost, card, itm):#명시적 호출?
        Transactions.__init__(self, cost, card, itm)
    #메서드
    def save(self):
        file = open("transactions.txt","a")
        file.write("%07d%16s%16s\n" %\
            (self.price * 100 * 0.9, self.credit_card, self.item))
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
        if input("Starbuzz card?") == "Y" :
            trans = Discount_trans(prices[choice-1],\
                 card, items[choice-1])
            trans.save()
        else:
            trans = Transactions(prices[choice-1],\
                 card, items[choice-1])
            trans.save()
