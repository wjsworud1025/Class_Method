#딕셔너리를 리턴하는 함수를 선언
def create_student(name, korean, english, math, science):
    return{
        "name":name,
        "korean":korean,
        "english":english,
        "math":math,
        "science":science,
    }

Students = [
    create_student("김유미", 80,90,95,70),
    create_student("이서진", 80,98,95,70),
    create_student("나형석", 66,90,95,70),
    create_student("유재석", 92,100,95,98),
    create_student("서유미", 68,73,82,90),
]

# 학생 명단(성적표) 출력하세요
print("이름", "총점", "평균", sep="\t")
for student in Students:
    score_sum = student["korean"]+student["english"]+student["math"]+student["science"]
    score_avg = score_sum/4
    print(student["name"], score_sum, score_avg, sep="\t")