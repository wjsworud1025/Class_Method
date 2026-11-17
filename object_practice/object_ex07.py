class Salary:
    def __init__(self,base_pay,bonus,overtime):
        self.base_py = base_pay
        self.bonus = bonus
        self.overtime = overtime

    def get_total(self):
        pay = self.base_py + self.bonus + self.overtime
        return pay

    def get_tax(self):
        tax = self.get_total() * 0.1
        return tax

    def get_net(self):
        net = self.get_total() - self.get_tax()
        return net

class WorkHistory:
    def __init__(self,company,position,start_year,end_year):
        self.company = company    #회사명
        self.position = position  #직급
        self.start_year = start_year  #입사연도
        self.end_year = end_year      #퇴사연도

    def get_years(self):
        return self.end_year - self.start_year

    def to_string(self):
        return "{}\t{}\t{}\t{}\t{}".format(
            self.company, self.position,self.start_year,
            self.end_year, self.get_years()
        )

# 사원정보 + Salary 객체를 속성으로 가진다. (has-a)
class Employee:
    def __init__(self,name,dept,salary):
        self.name = name
        self.dept = dept
        self.salary = salary     #1:1 Saraly
        self.histories = []     #WorkHistory 객체를 담을 리스트

    def add_history(self,history):
        self.histories.append(history)

    def to_string(self):
        return "{}\t{}\t{}\t{}\t{}\t{}".format(self.name,
                         self.dept,self.get_career(),
                         self.salary.get_total(),
                         self.salary.get_tax(),
                         self.salary.get_net()   )
    def get_career(self):
        total = 0
        for h in self.histories:
            total += h.get_years()
        return total

kimminsu = Employee("김민수", "개발팀", Salary(320, 40, 30))
leejieun = Employee("이지은", "운영팀", Salary(280, 60, 10))
choiseoyeon = Employee("최서연", "영업팀", Salary(350, 30, 25))

kimminsu.add_history(WorkHistory("넥슨", "사원", 2015, 2018))
kimminsu.add_history(WorkHistory("네오위즈", "대리", 2018, 2022))
choiseoyeon.add_history(WorkHistory("데이터랩", "사원", 2012, 2016))
choiseoyeon.add_history(WorkHistory("클라우드원", "과장", 2016, 2020))
choiseoyeon.add_history(WorkHistory("넥스트AI", "차장", 2020, 2023))

employees = [kimminsu, leejieun, choiseoyeon]

print("이름\t부서\t경력\t총액\t세금\t실수령액")
for e in employees:
    print(e.to_string())

print()
print("="*100)
print("\t 근 무 이 력")
for emp in employees:
    print("[{}] 총 경력 {}년" .format(emp.name, emp.get_career()))
    if len(emp.histories) == 0:
        print("이력 없음(신입)")
    for h in emp.histories:
        print(" "+ h.to_string())

