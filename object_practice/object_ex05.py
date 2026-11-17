class Employee:
    def __init__(self, name, base_pay, bouns, overtime):
        self.name = name
        self.base_pay = base_pay
        self.bouns = bouns
        self.overtime = overtime

    def get_total(self):
        total = self.base_pay + self.bouns + self.overtime
        return total
    
    def get_tax(self):
        tax = self.get_total() * 0.1
        return tax
    
    def get_net(self):
        net = self.get_total() - self.get_tax()
        return net
    
    def to_string(self):
        return "{}\t{}\t{}\t{}".format(self.name, self.get_total(), self.get_tax(), self.get_net())

employees = [
        Employee("김민수", 300, 50, 20),
        Employee("김민수", 320, 40, 30),
        Employee("김민수", 280, 60, 10),
        Employee("김민수", 350, 30, 25),
        Employee("김민수", 300, 70, 15),
    ]

print("이름","총액","세금", "실수령액", sep="\t")
for e in employees:
    print(e.to_string())