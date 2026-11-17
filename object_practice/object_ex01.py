# 학생 리스트(Students)를 선언해 주세요. 5명의 학생정보를 아래 속성으로 저장하세요
# 학생은 이름(name)과 4과목의 점수 데이터를 갖는다.
# 국어(korean), 영어(english), 수학(math), 과학(science) 속성을 갖는다.

Students = [
    {"name": "민수", "korean": 100, "english":90, "math": 95, "science": 70},
    {"name": "지영", "korean": 90, "english": 80, "math": 72, "science": 100},
    {"name": "서준", "korean": 70, "english": 66, "math": 80, "science": 90},
    {"name": "수빈", "korean": 50, "english": 70, "math": 88, "science": 88},
    {"name": "도윤", "korean": 80, "english": 85, "math": 84, "science": 84},
]
# 학생 명단(성적표) 출력하세요
print("이름", "총점", "평균", sep="\t")
for student in Students:
    score_sum = student["korean"]+student["english"]+student["math"]+student["science"]
    score_avg = score_sum/4
    print(student["name"], score_sum, score_avg, sep="\t")