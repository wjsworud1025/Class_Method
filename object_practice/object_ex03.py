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

# 학생을 처리하는 함수
# 학생 한명의 총점을 리턴하는 함수 : student_get_sum(student)
def student_get_sum(student):
    return (
        student["korean"]
        + student["english"]
        + student["math"]
        + student["science"]
    )

# 학생 한명의 평균을 리턴하는 함수 : student_get_avg(student)
def student_get_avg(student):
    return student_get_sum(student) / 4

# 학생 한명의 점수를 출력하는 함수 : student_get_string(student)
def student_get_string(student):
    print(
        f"{student['name']}\t"
        f"{student_get_sum(student)}\t"
        f"{student_get_avg(student):.2f}"
    )

# 학생명단(성적표) 출력
print("이름\t총점\t평균")
for student in Students:
    student_get_string(student)
