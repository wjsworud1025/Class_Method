class Student:
    def __init__(self,name,korean,english,math,science):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math
        self.science = science

    def get_sum(self):
                  score_sum = self.korean +\
                  self.english + \
                  self.math + self.science
                  return score_sum

    def get_average(self):
        score_avg = self.get_sum()/ 4
        return score_avg

    # 학생 한명의 점수를 출력하는 함수
    def to_string(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())

students = [Student("김유미",80,90,95,70),Student("이서진",80,90,95,70),Student("나형석",80,90,95,70),Student("유재석",80,90,95,70),Student("서유미",80,90,95,70)]


# 학생명단(성적표) 출력하세요
print("이름","총점","평균",sep="\t")
for student in students:
    print(student.to_string())