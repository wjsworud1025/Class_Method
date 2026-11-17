class WorkHistory:
    def __init__(self, company, position, start_year, end_year):
        self.company = company
        self.position = position
        self.start_year = start_year
        self.end_year = end_year

    def get_years(self):
        return self.end_year - self.start_year

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

class Employee:
    def __init__(self,name,dept,salary):
        self.name = name
        self.dept = dept
        self.salary = salary     #1:1 Saraly
        self.histories = []     #WorkHistory 객체를 담을 리스트

    def add_history(self,history):
        self.histories.append(history)

    def to_string(self):
        return "{}\t{}\t{}\t{}\t{}\t{}".format(
            self.name,
            self.dept,
            self.get_career(),
            self.salary.get_total(),
            self.salary.get_tax(),
            self.salary.get_net()
        )
    def get_career(self):
        total = 0
        for h in self.histories:
            total += h.get_years()
        return total

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_payroll(self):
        total = 0
        for employee in self.employees:
            total += employee.salary.get_total()
        return total

    def get_avg_career(self):
        if len(self.employees) == 0:
            return 0
        total = 0
        for employee in self.employees:
            total += employee.get_career()
        return total / len(self.employees)

class Company:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def get_employee_count(self):
        total = 0

        for department in self.departments:
            total += len(department.employees)

        return total

    def get_payroll(self):
        total = 0

        for department in self.departments:
            total += department.get_payroll()

        return total

    def print_report(self):
        print("부서\t인원\t급여 총액\t평균 경력")

        for department in self.departments:
            print("{}\t{}명\t{}\t{:.1f}년".format(
                department.name,
                len(department.employees),
                department.get_payroll(),
                department.get_avg_career()
            ))

        print("-" * 50)
        print("{} 전체\t{}명\t{}".format(
            self.name,
            self.get_employee_count(),
            self.get_payroll()
        ))

kimminsu = Employee("김민수", "개발팀", Salary(320, 40, 30))
leejieun = Employee("이지은", "인사팀", Salary(280, 60, 10))
choiseoyeon = Employee("최서연", "영업팀", Salary(350, 30, 25))

kimminsu.add_history(
    WorkHistory("넥슨", "사원", 2015, 2018)
)
kimminsu.add_history(
    WorkHistory("네오위즈", "대리", 2018, 2022)
)

choiseoyeon.add_history(
    WorkHistory("데이터랩", "사원", 2012, 2016)
)
choiseoyeon.add_history(
    WorkHistory("클라우드원", "과장", 2016, 2020)
)
choiseoyeon.add_history(
    WorkHistory("넥스트AI", "차장", 2020, 2023)
)


company = Company("블루웨이브")

development = Department("개발팀")
human_resources = Department("인사팀")
sales = Department("영업팀")
marketing = Department("마케팅팀")

# 직원의 dept와 같은 부서에 추가
development.add_employee(kimminsu)
human_resources.add_employee(leejieun)
sales.add_employee(choiseoyeon)

company.add_department(development)
company.add_department(human_resources)
company.add_department(sales)
company.add_department(marketing)

company.print_report()