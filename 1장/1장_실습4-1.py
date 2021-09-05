
class Person():
    name=""
    def __init__(self):#생성자
        print("Person Created")

class Employee(Person):#Person 클래스 상속
    job_title=""
    def __init__(self):
        Person.__init__(self)
        print("Employee created")
    
class Customer(Person):#Person 클래스 상속
    email=""
    def __init__(self):
        Person.__init__(self)
        print("Customer created")

johnSmith = Person()
janeEmployee = Employee()
bobCustomer = Customer()