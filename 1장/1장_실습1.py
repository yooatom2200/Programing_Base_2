class Address():
    name=""
    line1=""
    line2=""
    city=""
    state=""
    zip=""

#Address 인스턴스 생성
homeAddress = Address()

#Address 속성 값 지정
homeAddress.name = "Jhon Smith"
homeAddress.line1 = "701 N. C Street"
homeAddress.line2 = "Carver Science Building"
homeAddress.city = "Indianola"
homeAddress.state = "IA"
homeAddress.zip = "50125"

#또다른 Address 인스턴스 생성
vacationHomeAddress = Address()

#Address 속성 값 지정
vacationHomeAddress.name = "Jhon Smith"
vacationHomeAddress.line1 = "1122 Main Street"
vacationHomeAddress.line2 = ""
vacationHomeAddress.city = "Panama City Beach"
vacationHomeAddress.state = "FL"
vacationHomeAddress.zip = "32407"

#주소 출력
def printAddress(address):
    print(address.name)
    #만약 라인1의 주소데이터가 있다면 출력한다
    if(len(address.line1) > 0):
        print(address.line1)
    #만약 라인2의 주소데이터가 있다면 출력한다
    if(len(address.line2) > 0):
        print(address.line2)
    print(address.city + ", " + address.state + ", " + address.zip )

printAddress(homeAddress)
print()
printAddress(vacationHomeAddress)