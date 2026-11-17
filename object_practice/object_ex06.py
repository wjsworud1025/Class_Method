
class Salary:                   #급여 계산 전용 class
    def __init__(self, base_pay, bonus, overtime):
        self.base_pay = base_pay
        self.bonus = bonus
        self.overtime = overtime

    def get_total(self):
        total = self.base_pay + self.bonus + self.overtime
        return total
    
    def get_tax(self):
        tax = self.get_total() * 0.1
        return tax
    
    def get_net(self):
        net = self.get_total() - self.get_tax()
        return net
        
# 사원정보(Employee)가 급여정보(Salary) 객체를 속성으로 같는다.
class Employee:
    def __init__(self, name, dept, salary):
        self.name = name
        self.dept = dept
        self.salary = salary

    def to_string(self):
        return "{}\t{}\t{}\t{:.1f}\t{:.1f}".format(
            self.name,
            self.dept,
            self.salary.get_total(),
            self.salary.get_tax(),
            self.salary.get_net(),
            )
    
employees = [
        Employee("김민수", "영업팀", Salary(300, 50, 20)),
        Employee("이지은", "개발팀", Salary(320, 40, 30)),
        Employee("박준호", "운영팀", Salary(280, 60, 10)),
        Employee("최서연", "영업팀", Salary(350, 30, 25)),
        Employee("한도윤", "개발팀", Salary(300, 70, 15)),
    ]

print("이름", "부서", "총액","세금", "실수령액", sep="\t")
for e in employees:
    print(e.to_string())